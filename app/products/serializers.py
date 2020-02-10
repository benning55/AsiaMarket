from core.models import Category, Product
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    type = serializers.CharField()

    class Meta:
        model = Category
        fields = ('id', 'type')


class ProductSerializer(serializers.ModelSerializer):
    """serializer for product model"""
    title = serializers.CharField(max_length=255, allow_blank=True)

    class Meta:
        model = Product
        fields = ('id', 'category_name', 'category_color', 'title', 'pic1', 'pic2', 'pic3', 'url', 'description', 'price', 'quantity')

    category_name = serializers.SerializerMethodField('get_type_name')
    category_color = serializers.SerializerMethodField('get_color')

    def get_type_name(self, obj):
        return obj.category.type

    def get_color(self, obj):
        return obj.category.color

class ProductDataSerializer(serializers.ModelSerializer):
    """serializer for product model"""
    title = serializers.CharField(max_length=255, allow_blank=True)

    class Meta:
        model = Product
        fields = ('id', 'category_name', 'title', 'url', 'description', 'price', 'quantity')

    category_name = serializers.SerializerMethodField('get_type_name')

    def get_type_name(self, obj):
        return obj.category.type


class ProductImageSerializer(serializers.ModelSerializer):
    """serializer for product model"""

    class Meta:
        model = Product
        fields = ('id', 'pic1', 'pic2', 'pic3')
