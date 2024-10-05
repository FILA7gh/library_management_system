from rest_framework import serializers

from apps.authors.models import Author


class BaseAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
