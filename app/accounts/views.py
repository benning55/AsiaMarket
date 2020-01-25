from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView

from accounts.models import User, Profile
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
    permission_classes = (IsAdminUser, )


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
            profile = Profile.objects.all()
            serializer = serializers.ProfileSerializer(profile, many=True)
            return Response({"profiles": serializer.data}, status=status.HTTP_200_OK)
        else:
            profile = get_object_or_404(Profile.objects.all(), pk=pk)
            serializer = serializers.ProfileSerializer(profile)
            return Response({"profile": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        """
        Update user profile
        """
        pk = self.kwargs.get('pk')
        profile = get_object_or_404(Profile.objects.all(), pk=pk)
        data = request.data
        profile.profile_status = True
        serializer = serializers.ProfileSerializer(instance=profile, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            profile_save = serializer.save()
        return Response({"updated": serializer.data}, status=status.HTTP_200_OK)


class AddressApiView(APIView):
    """
    Address of user view
    """
