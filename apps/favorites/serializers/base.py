from rest_framework import serializers

from apps.favorites.models import FavoriteBook


class BaseFavoriteBookSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y%m%d %H:%M", required=False)

    class Meta:
        model = FavoriteBook
        """
        Either fields or exclude must be implemented
        """
        ...
