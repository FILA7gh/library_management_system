from rest_framework.viewsets import ModelViewSet

from authors.models import Author
from authors.serializers.views import AuthorListViewSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorListViewSerializer
