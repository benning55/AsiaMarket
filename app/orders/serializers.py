from rest_framework import serializers
from core.models import Order, OrderDetail
from products.serializers import ProductDataSerializer


class OrderSerializer(serializers.ModelSerializer):
    """ Validate data for Order object """
    class Meta:
        model = Order
        fields = ('id', 'user', 'address', 'total_price', 'payment_type', 'payment_status')
        extra_kwargs = {
            'id': {'read_only': True}
        }

    def create(self, validated_data):
        order = Order.objects.create(
            user=validated_data['user'],
            address=validated_data['address'],
            total_price=validated_data['total_price'],
            payment_type=validated_data['payment_type'],
            payment_status=validated_data['payment_status']
        )
        return order


class OrderDetailSerializer(serializers.ModelSerializer):
    """ Validate data for OrderDetail object """
    product = ProductDataSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'order', 'product', 'quantity')
        extra_kwargs = {
            'id': {'read_only': True}
        }


class ShowOrderData(serializers.Serializer):
    order = OrderSerializer(many=True)
    order_detail = OrderDetailSerializer(many=True)
