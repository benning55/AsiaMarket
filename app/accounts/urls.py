from django.urls import path

from accounts import views

urlpatterns = [
    path('register/', views.CreateUser.as_view(), name='register')
]
