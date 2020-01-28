from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView

from core.models import User, Profile, Address
from rest_framework.decorators import api_view, permission_classes
from accounts import serializers


class CreateUser(generics.CreateAPIView):
    """ Create User in System"""
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny,)


class GetAllUser(generics.ListAPIView):
    """ Get all list data """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAdminUser,)


@api_view(['GET', 'DELETE', ])
@permission_classes([IsAuthenticated, ])
def user_view(request):
    """
    Get the request user data
    """
    if request.method == 'GET':
        """
        Get All User Detail
        """
        serializer = serializers.UserSerializer(request.user)
        profile = get_object_or_404(Profile.objects.all(), pk=serializer.data['id'])
        profile_serializer = serializers.ProfileSerializer(profile)
        return Response({
            "user": serializer.data,
            "profile": profile_serializer.data
        }, status.HTTP_200_OK)
    elif request.method == 'DELETE':
        """
        Delete Request User
        """
        user_id = request.user.id
        user = get_object_or_404(User.objects.all(), pk=user_id)
        user.delete()
        return Response({"message": "User has been delete"}, status=status.HTTP_200_OK)
    return Response(status.HTTP_400_BAD_REQUEST)


class ProfileApiView(APIView):
    """
    Profile API View
    """
    serializer_class = serializers.ProfileSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        """
        Get all the data of Profile
        """
        pk = self.kwargs.get('pk')
        if pk is None:
            user_id = request.user.id
            profile = get_object_or_404(Profile.objects.all(), pk=user_id)
            serializer = serializers.ProfileSerializer(profile)
            return Response({"profile": serializer.data}, status=status.HTTP_200_OK)
        else:
            if request.user.id != pk:
                return Response({"error": "You have no permission"}, status=status.HTTP_403_FORBIDDEN)
            else:
                profile = get_object_or_404(Profile.objects.all(), pk=pk)
                serializer = serializers.ProfileSerializer(profile)
                return Response({"profile": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        """
        Update user profile
        """
        data = request.data
        profile = get_object_or_404(Profile.objects.all(), pk=data['user_id'])
        profile.profile_status = True
        serializer = serializers.ProfileSerializer(instance=profile, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            profile_save = serializer.save()
        return Response({"updated": serializer.data}, status=status.HTTP_200_OK)


class UserAddressApiView(APIView):
    """
    Address of user view need to have an user id first
    """
    serializer_classes = serializers.AddressSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Get Address of user
        """
        pk = self.request.user.id
        address = Address.objects.all()
        user_address = address.filter(user_id=pk)
        serializer = serializers.AddressSerializer(user_address, many=True)
        return Response({"address": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Post address of the user
        """
        pk = self.request.user.id
        user = get_object_or_404(User.objects.all(), pk=pk)
        data = request.data

        if data['recipient'] == '':
            data['recipient'] = user.last_name
            data['user_id'] = user.id
        else:
            data['user_id'] = user.id

        serializer = serializers.AddressSerializer(data=data)

        if serializer.is_valid():
            address = serializer.create(validated_data=serializer.validated_data)
            address.user_id = user.id
            address.save()
            return Response({"address": serializer.validated_data}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        """
        Update user address data
        """
        user_id = self.request.user.id
        data = request.data
        address = get_object_or_404(Address.objects.all(), pk=data['id'])

        if user_id != address.user_id:
            return Response({"error": "You dont have permission to change."}, status=status.HTTP_200_OK)
        else:
            serializer = serializers.AddressSerializer(instance=address, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status.HTTP_200_OK)
            return Response({"updated": "fucked"}, status=status.HTTP_200_OK)


@api_view(['POST', ])
@permission_classes([AllowAny, ])
def address_register(request):
    """
    User Address on register
    """
    if request.method == 'POST':
        """
        Add user address on register
        """
        data = request.data
        user = get_object_or_404(User.objects.all(), pk=data['user_id'])

        if data['recipient'] == '':
            data['recipient'] = user.username
        serializer = serializers.AddressSerializer(data=data)

        if serializer.is_valid():
            address = serializer.create(validated_data=serializer.validated_data)
            address.user_id = data['user_id']
            address.save()
            return Response({"address": serializer.validated_data}, status=status.HTTP_200_OK)

        return Response({"Error": "Somethings Wrong"}, status=status.HTTP_400_BAD_REQUEST)
