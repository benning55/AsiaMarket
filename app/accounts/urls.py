from django.urls import path

from accounts import views

urlpatterns = [
    path('register/', views.CreateUser.as_view(), name='register'),
    path('list-all-user/', views.GetAllUser.as_view(), name='getAllUser'),
    path('user/', views.user_view)
]
