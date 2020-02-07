from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import Product, Category
from products import serializers


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
