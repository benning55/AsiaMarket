from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from accounts.models import User
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer


class CreateUser(generics.CreateAPIView):
    """ Create User in System"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class GetAllUser(generics.ListAPIView):
    """ Get all list data """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, )


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
def user_view(request):
    """ Get the request user d ata"""
    if request.method == 'GET':
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status.HTTP_200_OK)
    return Response(status.HTTP_400_BAD_REQUEST)
