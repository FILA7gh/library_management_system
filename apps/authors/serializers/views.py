from rest_framework import serializers

from authors.models import Author


class AuthorViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorListViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'date_of_birth', 'date_of_death')
