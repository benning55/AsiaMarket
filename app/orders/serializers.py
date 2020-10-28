from rest_framework import serializers

from core.models import Order, OrderDetail, PaymentBill, ShippingRate
from products.serializers import ProductDataSerializer


class OrderSerializer(serializers.ModelSerializer):
    """ Validate data for Order object """
    receipt = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Order
        fields = ('id', 'user', 'address', 'price', 'shipping_fee', 'total_price', 'payment_type', 'payment_status', 'tracking_no', 'code', 'receipt', 'country')
        extra_kwargs = {
            'id': {'read_only': True},
            'code': {'read_only': True}
        }

    def create(self, validated_data):
        order = Order.objects.create(
            user=validated_data['user'],
            address=validated_data['address'],
            price=validated_data['price'],
            shipping_fee=validated_data['shipping_fee'],
            total_price=validated_data['total_price'],
            payment_type=validated_data['payment_type'],
            payment_status=validated_data['payment_status'],
            country=validated_data['country']
        )
        return order

    def update(self, instance, validated_data):
        instance.payment_type = validated_data.get('payment_type', instance.payment_type)
        instance.payment_status = validated_data.get('payment_status', instance.payment_status)
        instance.save()
        return instance

    def get_receipt(self, obj):
        order_id = obj.id
        queryset = PaymentBill.objects.all()
        queryset = queryset.filter(order_id=order_id)
        if len(queryset) == 0:
            return False
        else:
            return True


class OrderForUseSerializer(serializers.ModelSerializer):
    """ Validate data for Order object """
    pic1 = serializers.SerializerMethodField(read_only=True)
    receipt = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'address', 'total_price', 'payment_type', 'payment_status', 'delivery_status', 'tracking_no', 'created', 'pic1', 'receipt', 'country')
        extra_kwargs = {
            'id': {'read_only': True}
        }

    def get_pic1(self, obj):
        order_id = obj.id
        queryset = OrderDetail.objects.all().filter(order_id=order_id)
        if len(queryset) == 0:
            return None
        else:
            product_pic = str(queryset.first().product.pic1)
            return product_pic

    def get_receipt(self, obj):
        order_id = obj.id
        queryset = PaymentBill.objects.all()
        queryset = queryset.filter(order_id=order_id)
        if len(queryset) == 0:
            return False
        else:
            return True


class OrderDetailSerializer(serializers.ModelSerializer):
    """ Validate data for OrderDetail object """
    product = ProductDataSerializer(read_only=True)

    class Meta:
        model = OrderDetail
        fields = ('id', 'order', 'product', 'quantity')
        extra_kwargs = {
            'id': {'read_only': True}
        }


class ShowOrderData(serializers.Serializer):
    order = OrderSerializer(many=True)
    order_detail = OrderDetailSerializer(many=True)


class PaymentBillSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentBill
        fields = ('id', 'order', 'pic', 'time_transfer')
        extra_kwargs = {
            'id': {'read_only': True}
        }

    def create(self, validated_data):
        obj = PaymentBill.objects.create(
            order=validated_data['order'],
            pic=validated_data['pic'],
            time_transfer=validated_data['time_transfer']
        )
        return obj


class ShippingRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShippingRate
        fields = ('id', 'price', 'country')
        extra_kwargs = {
            'id': {'read_only': True}
        }
