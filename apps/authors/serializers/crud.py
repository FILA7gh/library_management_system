from apps.authors.serializers.base import BaseAuthorSerializer


class CreateUpdateAuthorSerializer(BaseAuthorSerializer):
    class Meta(BaseAuthorSerializer.Meta):
        fields = ('first_name', 'last_name', 'biography', 'date_of_birth', 'date_of_death')


class DetailAuthorSerializer(BaseAuthorSerializer):
    class Meta(BaseAuthorSerializer.Meta):
        pass


class ListAuthorSerializer(BaseAuthorSerializer):
    class Meta(BaseAuthorSerializer.Meta):
        fields = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
