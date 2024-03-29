import sys
from django.core import exceptions
from core.models import User, Profile, Address
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

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        instance.save()
        return instance


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for Profile model"""

    class Meta:
        model = Profile
        fields = ('user_id', 'tel', 'dob', 'sex', 'profile_status')
        extra_kwargs = {
            'profile_status': {'read_only': True},
        }

    def update(self, instance, validated_data):
        instance.tel = validated_data.get('tel', instance.tel)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.sex = validated_data.get('sex', instance.sex)

        instance.save()
        return instance


class ProfileRegisterSerializer(serializers.ModelSerializer):
    """Serializer for Profile model"""

    class Meta:
        model = Profile
        fields = ('tel', 'dob', 'sex')


class AddressSerializer(serializers.ModelSerializer):
    """Serializer for address model"""
    recipient = serializers.CharField(allow_blank=True)

    class Meta:
        model = Address
        fields = ('id', 'user_id', 'recipient', 'street', 'house_number', 'post_code', 'city')
        extra_kwargs = {
            'id': {'read_only': True}
        }

    def create(self, validated_data):
        address, created = Address.objects.update_or_create(
            recipient=validated_data['recipient'],
            house_number=validated_data['house_number'],
            street=validated_data['post_code'],
            defaults={
                'street': validated_data['street'],
                'city': validated_data['city']
            }
        )
        return address

    def update(self, instance, validated_data):
        instance.recipient = validated_data.get('recipient', instance.recipient)
        instance.street = validated_data.get('street', instance.street)
        instance.house_number = validated_data.get('house_number', instance.house_number)
        instance.post_code = validated_data.get('post_code', instance.post_code)
        instance.city = validated_data.get('city', instance.city)

        instance.save()
        return instance


class AddressRegisterSerializer(serializers.ModelSerializer):
    """Serializer for address model"""

    class Meta:
        model = Address
        fields = ('street', 'house_number', 'post_code', 'city')


class RegisterSerializer(serializers.Serializer):
    user = UserSerializer()
    profile = ProfileRegisterSerializer()
    address = AddressRegisterSerializer()
