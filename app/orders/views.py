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

from core.models import Product, Category, Cart, CartDetail, Code, Order, OrderDetail
from orders import serializers

Timeline = namedtuple('Timeline', ('order', 'order_detail'))


class OrderApiView(APIView):
    """ Order api view """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Get All of user order
        """
        user = request.user
        return Response({'data': f'Hello {user.first_name}'}, status=status.HTTP_200_OK)

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
                for cart_product in cart_detail:
                    product_obj = Product.objects.get(pk=cart_product.product.id)
                    quantity_left = product_obj.quantity - cart_product.quantity
                    product_obj.quantity = quantity_left
                    product_obj.save()
                    OrderDetail.objects.create(
                        order_id=order.id,
                        product_id=cart_product.id,
                        quantity=cart_product.quantity
                    )
                    cart_product.delete()
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
