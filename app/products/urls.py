from django.urls import path
from rest_framework.routers import DefaultRouter

from products import views

app_name = 'products'

router = DefaultRouter()
router.register('product', views.ProductApiView.as_view(), base_name='product_viewset')
router.register('cart', views.CartApiView.as_view(), base_name='cart-viewset')
router.register('cart-detail', views.CartDetailApiView.as_view(), base_name='cart-detail')

urlpatterns = [
    path('product/', views.ProductApiView.as_view(), name='product'),
    path('product/<int:pk>/', views.ProductApiView.as_view()),
    path('new/', views.new_products),
    path('recommend/', views.recommend_products),
    path('cart/', views.CartApiView.as_view(), name='cart'),
    path('cart-detail/', views.CartDetailApiView.as_view(), name='cart-detail')
]
