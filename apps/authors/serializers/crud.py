from apps.authors.serializers.base import BaseAuthorSerializer


class CreateUpdateAuthorSerializer(BaseAuthorSerializer):
    class Meta(BaseAuthorSerializer.Meta):
        exclude = ("id",)


class DetailAuthorSerializer(BaseAuthorSerializer):
    class Meta(BaseAuthorSerializer.Meta):
        fields = "__all__"


class ListAuthorSerializer(BaseAuthorSerializer):
    class Meta(BaseAuthorSerializer.Meta):
        fields = ("id", "first_name", "last_name", "date_of_birth", "date_of_death")
