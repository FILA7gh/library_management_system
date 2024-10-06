from rest_framework import serializers

from apps.books.models import Book


class BaseBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        """
        Either fields or exclude must be implemented
        """
        ...
