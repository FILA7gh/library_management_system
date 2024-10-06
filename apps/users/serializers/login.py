from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework import serializers

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = User.objects.filter(username=username).first()

        if user is None:
            raise ValidationError("User not found!")

        if not user.check_password(password):
            raise ValidationError("Invalid password!")

        return attrs
