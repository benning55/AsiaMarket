import sys
from django.core import exceptions
from accounts.models import User, Profile, Address
from rest_framework import serializers
import django.contrib.auth.password_validation as validators


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')

    def validate(self, data):
        user = User(**data)

        password = data.get('password')
        errors = dict()

        try:
            validators.validate_password(password=password, user=User)
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return data

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        profile = Profile.objects.create(user_id=user.id)
        profile.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for Profile model"""

    class Meta:
        model = Profile
        fields = ('user_id', 'tel', 'dob', 'sex', 'profile_status')
        extra_kwargs = {
            'profile_status': {'read_only': True}
        }

    def update(self, instance, validated_data):
        instance.tel = validated_data.get('tel', instance.tel)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.sex = validated_data.get('sex', instance.sex)

        instance.save()
        return instance


# class AddressSerializer(serializers.ModelSerializer):
#     """Serializer for address model"""
#
#     class Meta:
#         model = Address
#         fields = ('user_id', 'address', 'street', 'city', 'post_code')
