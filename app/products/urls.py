from django.urls import path
from rest_framework.routers import DefaultRouter

from products import views

app_name = 'products'

router = DefaultRouter()
router.register('product', views.ProductApiView.as_view(), base_name='product_viewset')

urlpatterns = [
    path('product/', views.ProductApiView.as_view(), name='product'),
    path('product/<int:pk>/', views.ProductApiView.as_view()),
    path('new/', views.new_products),
    path('recommend/', views.recommend_products)
]
