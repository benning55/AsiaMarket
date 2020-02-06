from core.models import Category, Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    """serializer for product model"""
    title = serializers.CharField(max_length=255, allow_blank=True)

    class Meta:
        model = Product
        fields = ('id', 'category_id', 'title', 'pic1', 'pic2', 'pic3', 'url', 'description', 'price', 'quantity')

    # def to_representation(self, instance):
    #     resdata = {
    #         'id': instance.id,
    #         'category_id': instance.category_id,
    #         'title': instance.title,
    #         'image': {
    #             'pic1': instance.pic1,
    #             'pic2': instance.pic2,
    #             'pic3': instance.pic3
    #         },
    #         'url': instance.url,
    #         'description': instance.description,
    #         'price': instance.price,
    #         'quantity': instance.quantity
    #     }
    #
    #     return resdata

class ProductDataSerializer(serializers.ModelSerializer):
    """serializer for product model"""
    title = serializers.CharField(max_length=255, allow_blank=True)

    class Meta:
        model = Product
        fields = ('id', 'category_id', 'title', 'url', 'description', 'price', 'quantity')


class ProductImageSerializer(serializers.ModelSerializer):
    """serializer for product model"""

    class Meta:
        model = Product
        fields = ('id', 'pic1', 'pic2', 'pic3')
