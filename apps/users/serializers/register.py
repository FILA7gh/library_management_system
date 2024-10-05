from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework import serializers

from apps.users.serializers.base import BaseUserSerializer

User = get_user_model()


class RegisterSerializer(BaseUserSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmed = serializers.CharField(write_only=True)

    class Meta(BaseUserSerializer.Meta):
        fields = ('username', 'password', 'password_confirmed', 'email', 'first_name', 'last_name')

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirmed']:
            raise ValidationError("Passwords don't match")
        return attrs

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
