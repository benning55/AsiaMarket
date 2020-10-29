from core.models import Category, Product, Cart, Code, CartDetail, CarouselImage, FooterData, Banner
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    type = serializers.CharField()

    class Meta:
        model = Category
        fields = ('id', 'type', 'color')


class ProductSerializer(serializers.ModelSerializer):
    """serializer for product model"""
    title = serializers.CharField(max_length=255, allow_blank=True)

    class Meta:
        model = Product
        fields = ('id', 'category_id', 'category_name', 'category_color', 'title', 'pic1', 'pic2', 'pic3', 'url', 'description', 'price', 'quantity', 'is_active')

    category_id = serializers.SerializerMethodField('get_id')
    category_name = serializers.SerializerMethodField('get_type_name')
    category_color = serializers.SerializerMethodField('get_color')

    def get_id(self, obj):
        return obj.category.id

    def get_type_name(self, obj):
        return obj.category.type

    def get_color(self, obj):
        return obj.category.color


class ProductDataSerializer(serializers.ModelSerializer):
    """serializer for product model"""
    title = serializers.CharField(max_length=255, allow_blank=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'pic1', 'price', 'quantity', 'is_active')


class ProductForCartSerializer(serializers.ModelSerializer):
    """serializer for product model"""

    class Meta:
        model = Product
        fields = ('id', 'quantity')


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


class CartDetailForAddSerializer(serializers.ModelSerializer):
    """ Serializer for cart detail """
    product = ProductForCartSerializer(read_only=True)

    class Meta:
        model = CartDetail
        fields = ('id', 'cart_id', 'quantity', 'price', 'product')
        extra_kwargs = {
            'id': {'read_only': True}
        }


class CartDetailSerializer(serializers.ModelSerializer):
    """ Serializer for cart detail """
    product = ProductDataSerializer(read_only=True)

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
        product_id = validated_data['product'].id
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


class CarouselImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselImage
        fields = ('id', 'picture')
        extra_kwargs = {
            'id': {'read_only': True}
        }


class FooterDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterData
        fields = ('id', 'phone', 'email', 'address')
        extra_kwargs = {
            'id': {'read_only': True}
        }


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('id', 'description')
        extra_kwargs = {
            'id': {'read_only': True}
        }
