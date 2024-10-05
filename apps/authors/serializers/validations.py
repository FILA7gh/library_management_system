from rest_framework import serializers

from authors.models import Author


class AuthorValidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = ('id',)
