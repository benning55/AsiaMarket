import random
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from collections import namedtuple
import json

from core.models import Product, Category, Cart, CartDetail, Code
from products import serializers

Timeline = namedtuple('Timeline', ('cart', 'cart_detail', 'code'))


class ProductApiView(APIView):
    """
    Product API view
    """
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        """
        Get all the product in system and product detail
        """
        pk = self.kwargs.get('pk')
        if pk is None:
            queryset = Product.objects.all().order_by('-id')
            serializer = serializers.ProductSerializer(queryset, many=True)
            return Response({
                "data": serializer.data
            }, status=status.HTTP_200_OK
            )
        else:
            queryset = get_object_or_404(Product.objects.all().order_by('-id'), pk=pk)
            serializer = serializers.ProductSerializer(queryset)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Post request for filter category
        """
        category_id = request.data['category_id']
        queryset = Product.objects.all()
        queryset_cat = queryset.filter(category_id=category_id).order_by('-id')
        if len(queryset_cat) == 0:
            return Response({"data": "There is no category here"}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = serializers.ProductSerializer(queryset_cat, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET', ])
@permission_classes([AllowAny, ])
def new_products(request):
    """
    New 10 Product in system
    """
    if request.method == 'GET':
        queryset = Product.objects.all().order_by('-id')
        if len(queryset) < 10:
            return Response({"error": 'Data not enough'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            queryset = queryset[:10]
            serializer = serializers.ProductSerializer(queryset, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET', ])
@permission_classes([AllowAny, ])
def recommend_products(request):
    """
    Random 10 recommend product
    """
    if request.method == 'GET':
        queryset = Product.objects.all()
        if len(queryset) < 10:
            return Response({"error": 'Data not enough'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            random_items = random.sample(list(queryset), 10)
            serializer = serializers.ProductSerializer(random_items, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)


class CartApiView(APIView):
    """
    Cart api view
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """ Get all about user cart detail"""
        user = request.user
        cart = get_object_or_404(Cart.objects.all(), user_id=user.id)
        cart_detail = CartDetail.objects.all()
        cart_detail = cart_detail.filter(cart_id=user.id)

        if cart.code_id is None:
            timeline = Timeline(
                cart=Cart.objects.all().filter(user_id=user.id),
                cart_detail=cart_detail,
                code=None
            )
        else:
            timeline = Timeline(
                cart=Cart.objects.all().filter(user_id=user.id),
                cart_detail=cart_detail,
                code=Code.objects.all().filter(pk=cart.code_id)
            )
        serializer = serializers.PersonalCartSerializer(timeline)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)


class CartDetailApiView(APIView):
    """
    Cart Detail Api view
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """ Get user product """
        user = request.user
        cart_detail = CartDetail.objects.all()
        cart_detail = cart_detail.filter(cart_id=user.id)
        serializer = serializers.CartDetailForAddSerializer(cart_detail, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """ Add product to detail """
        user, data = request.user, request.data
        product_id, quantity = data['product_id'], data['quantity']
        product = get_object_or_404(Product.objects.all(), pk=product_id)
        total_price = product.price * quantity
        payload = {
            'cart': user.id,
            'quantity': quantity,
            'price': total_price,
            'product': product_id
        }
        serializer = serializers.CartDetailSaveSerializer(data=payload)
        if serializer.is_valid():
            detail = serializer.create(serializer.validated_data)
            detail_json = serializers.CartDetailForAddSerializer(detail)
            return Response({'data': detail_json.data}, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """ Delete product from cart """
        user, pk = request.user, self.kwargs.get('pk')
        cart_id = user.id
        query = CartDetail.objects.all().filter(cart_id=cart_id, product_id=pk)
        if len(query) == 0:
            return Response({'error': 'Data Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            data = query[0]
            data.delete()
            return Response({'success_delete': data.product_id}, status=status.HTTP_200_OK)
