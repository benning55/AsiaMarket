from django.urls import path
from rest_framework.routers import DefaultRouter

from utils import views

app_name = 'utils'

urlpatterns = [
    path('information/', views.get_information, name='information'),
    path('information/<str:key>/', views.get_information)
]