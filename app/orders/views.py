import random
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from collections import namedtuple
import json

from core.models import Product, Category, Cart, CartDetail, Code, Order, OrderDetail, PaymentBill
from orders import serializers

Timeline = namedtuple('Timeline', ('order', 'order_detail'))


class OrderApiView(APIView):
    """ Order api view """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Get All of user order
        """
        pk = self.kwargs.get("pk")
        user = request.user
        if pk is None:
            order_query = Order.objects.all().filter(user_id=user.id).order_by('-id')
            serializer = serializers.OrderForUseSerializer(order_query, many=True)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            order = get_object_or_404(Order.objects.all(), pk=pk)
            if order.user_id != user.id:
                return Response({'error': 'You dont have permission to look'}, status=status.HTTP_403_FORBIDDEN)
            else:
                order_detail = OrderDetail.objects.all().filter(order_id=order.id)
                timeline = Timeline(
                    order=Order.objects.all().filter(pk=pk),
                    order_detail=order_detail
                )
                serializer = serializers.ShowOrderData(timeline)
                return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Turn cart and cart detail to order
        """
        user, data = request.user, request.data
        address, user_id = data['address'], user.id
        cart = get_object_or_404(Cart.objects.all(), pk=user_id)
        cart_detail = CartDetail.objects.all().filter(cart_id=cart.user_id)
        payload = {
            "user": user.id,
            "address": address,
            "total_price": data['total_price'],
            "payment_type": data['payment_type'],
            "payment_status": data['payment_status']
        }
        serializer = serializers.OrderSerializer(data=payload)
        if serializer.is_valid():
            if len(cart_detail) != 0:
                order = serializer.create(serializer.validated_data)
                for pro_in_cart in cart_detail:
                    product = Product.objects.get(pk=pro_in_cart.product.id)
                    quantity_left = product.quantity - pro_in_cart.quantity
                    product.quantity = quantity_left
                    product.save()
                    order_details = OrderDetail.objects.create(
                        order_id=order.id,
                        product_id=product.id,
                        quantity=pro_in_cart.quantity
                    )
                    pro_in_cart.delete()
                if cart.code is not None:
                    code = Code.objects.get(pk=cart.code.id)
                    code.quantity = code.quantity - 1
                    code.save()
                    cart.code = None
                    cart.save()
                return Response({'data': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'data': 'There is no product in cart.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class PaymentBillUpload(APIView):
    """ Get bill from banktransfer """
    parser_classes = (MultiPartParser,)
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        print(request.data)
        print(request.FILES['pic'])

        # serializer = serializers.PaymentBillSerializer(data=request.data)
        #
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_200_OK)
        # else:
        return Response({'data': 'test'}, status=status.HTTP_200_OK)
