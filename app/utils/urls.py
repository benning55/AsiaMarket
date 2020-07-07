from django.urls import path
from rest_framework.routers import DefaultRouter

from products import views

app_name = 'utils'

urlpatterns = [
    path('information/', views.ProductApiView.as_view(), name='product'),
]