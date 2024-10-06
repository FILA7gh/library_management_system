from rest_framework import serializers

from apps.books.serializers.crud import ListBookSerializer
from apps.favorites.serializers.base import BaseFavoriteBookSerializer


class CreateFavoriteBookSerializer(BaseFavoriteBookSerializer):
    class Meta(BaseFavoriteBookSerializer.Meta):
        exclude = ("id", "user")

    def create(self, validated_data):
        favorite_book = self.Meta.model.objects.create(**validated_data)
        return favorite_book


class DetailFavoriteBookSerializer(BaseFavoriteBookSerializer):
    book = ListBookSerializer(many=False)

    class Meta(BaseFavoriteBookSerializer.Meta):
        fields = "__all__"


class ListFavoriteBookSerializer(BaseFavoriteBookSerializer):
    book = serializers.CharField(source="book.title")

    class Meta(BaseFavoriteBookSerializer.Meta):
        fields = ("id", "book")
