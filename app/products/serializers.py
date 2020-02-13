from core.models import Category, Product, Cart, Code, CartDetail
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


class CodeSerializer(serializers.ModelSerializer):
    """ serializer for cart """

    class Meta:
        model = Code
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    """ serializer for cart """

    class Meta:
        model = Cart
        fields = '__all__'


class CartDetailSerializer(serializers.ModelSerializer):
    """ Serializer for cart detail """
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartDetail
        fields = ('id', 'cart_id', 'quantity', 'price', 'product')
        extra_kwargs = {
            'id': {'read_only': True}
        }


class CartDetailSaveSerializer(serializers.ModelSerializer):
    """ Serializer for cart detail """

    class Meta:
        model = CartDetail
        fields = '__all__'

    def create(self, validated_data):
        cart_id = Cart.objects.get(user=validated_data['cart']).user_id
        product_id = Product.objects.get(title=validated_data['product']).id
        cart_detail, created = CartDetail.objects.update_or_create(
            cart_id=cart_id,
            product_id=product_id,
            defaults={
                'quantity': validated_data['quantity'],
                'price': validated_data['price']
            }
        )
        return cart_detail


class PersonalCartSerializer(serializers.Serializer):
    cart = CartSerializer(many=True)
    cart_detail = CartDetailSerializer(many=True)
    code = CodeSerializer(required=False, many=True)
