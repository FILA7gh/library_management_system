from rest_framework import serializers

from apps.authors.models import Author


class BaseAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        """
        Either fields or exclude must be implemented
        """
        ...
