from apps.authors.serializers.crud import ListAuthorSerializer
from apps.books.serializers.base import BaseBookSerializer


class CreateUpdateBookSerializer(BaseBookSerializer):
    class Meta(BaseBookSerializer.Meta):
        exclude = ("id",)


class DetailBookSerializer(BaseBookSerializer):
    authors = ListAuthorSerializer(many=True)

    class Meta(BaseBookSerializer.Meta):
        fields = "__all__"


class ListBookSerializer(BaseBookSerializer):
    class Meta(BaseBookSerializer.Meta):
        fields = ("id", "title", "genre", "publication_date")
