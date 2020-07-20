from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from collections import namedtuple

from core.models import Product, Category, Cart, CartDetail, Code, Order, OrderDetail, PaymentBill, ShippingRate, \
    NotifyEmail
from orders import serializers

Timeline = namedtuple('Timeline', ('order', 'order_detail'))


def order_notify(order):
    """
    Send an notify email to admin everytime that have order
    """
    admin_email = []
    emails = NotifyEmail.objects.all()
    for email in emails:
        admin_email.append(email.email)
    product_order = OrderDetail.objects.all().filter(order_id=order.id)
    message = render_to_string('notify_order.html', {
        'order': order,
        'products': product_order
    })
    send_mail(
        'We have new order!!',
        message,
        'new-order@thaimarket.express',
        admin_email,
        html_message=message,
        fail_silently=False
    )


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
            "price": data['price'],
            "shipping_fee": data['shipping_fee'],
            "payment_type": data['payment_type'],
            "payment_status": data['payment_status'],
            "country": data['country']
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
                        quantity=pro_in_cart.quantity,
                        price=(product.price * pro_in_cart.quantity)
                    )
                    pro_in_cart.delete()
                if cart.code is not None:
                    code = Code.objects.get(pk=cart.code.id)
                    code.quantity = code.quantity - 1
                    code.save()
                    order.code = code.name
                    order.save()
                    cart.code = None
                    cart.save()
                order_notify(order)
                order_serialize = serializers.OrderSerializer(order)
                return Response({'data': order_serialize.data}, status=status.HTTP_200_OK)
            else:
                return Response({'data': 'There is no product in cart.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        """ Update order object """
        user = request.user
        data = request.data
        order = get_object_or_404(Order.objects.all(), pk=data['id'])
        if order.user_id != user.id:
            return Response({'error': 'You dont have permission'}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = serializers.OrderSerializer(instance=order, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            order_updated = serializer.save()
            print(order_updated)
        return Response({"updated": serializer.data}, status=status.HTTP_200_OK)


class PaymentBillUpload(APIView):
    """ Get bill from banktransfer """
    parser_classes = (MultiPartParser,)
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        order = get_object_or_404(Order.objects.all(), pk=request.data['order'])
        if order.payment_type == "PayPal":
            return Response({'error': 'This type of order is paypal.'})
        else:
            data = {
                'order': request.data['order'],
                'pic': request.FILES['pic'],
                'time_transfer': request.data['time_transfer'],
            }
            serializer = serializers.PaymentBillSerializer(data=data)

            if serializer.is_valid():
                obj = serializer.create(serializer.validated_data)
                order = Order.objects.get(pk=obj.order.id)
                order.payment_type = 'BankTransfer'
                order.save()
                obj_serialize = serializers.PaymentBillSerializer(obj)
                return Response(obj_serialize.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_200_OK)


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
def Shipping_Fee(request, *args, **kwargs):
    """
    New 10 Product in system
    """
    if request.method == 'GET':
        country = kwargs.get("country")
        queryset = ShippingRate.objects.all()
        if country is None:
            if len(queryset) == 0:
                return Response({"error": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
            elif len(queryset) > 0:
                serilaizer = serializers.ShippingRateSerializer(queryset, many=True)
                return Response(serilaizer.data, status=status.HTTP_200_OK)
        else:
            queryset = queryset.filter(country=country)
            if len(queryset) == 0:
                return Response({"error": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
            else:
                serilaizer = serializers.ShippingRateSerializer(queryset, many=True)
                return Response(serilaizer.data, status=status.HTTP_200_OK)
