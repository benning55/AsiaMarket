from django.urls import path, include
from rest_framework.routers import DefaultRouter

from orders import views

app_name = 'orders'

router = DefaultRouter()
router.register('order', views.OrderApiView.as_view(), base_name='order_viewset')
router.register('payment-bill', views.PaymentBillUpload.as_view(), base_name='payment-bill')

urlpatterns = [
    path('order/', views.OrderApiView.as_view(), name='order'),
    path('order/<int:pk>/', views.OrderApiView.as_view()),
    path('payment-bill/', views.PaymentBillUpload.as_view(), name='payment-bill')
]
