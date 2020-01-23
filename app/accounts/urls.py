from django.urls import path
from rest_framework.routers import DefaultRouter

from accounts import views

router = DefaultRouter()
router.register('profile', views.ProfileApiView, base_name='profile-viewset')

urlpatterns = [
    path('register/', views.CreateUser.as_view(), name='register'),
    path('list-all-user/', views.GetAllUser.as_view(), name='getAllUser'),
    path('profile/', views.ProfileApiView.as_view()),
    path('profile/<int:pk>/', views.ProfileApiView.as_view()),
    path('user/', views.user_view)
]
