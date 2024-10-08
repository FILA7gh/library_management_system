from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    ListAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated

from apps.authors.models import Author
from apps.authors.serializers.crud import (
    DetailAuthorSerializer,
    ListAuthorSerializer,
    CreateUpdateAuthorSerializer,
)


class CreateAuthorAPIView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = CreateUpdateAuthorSerializer
    permission_classes = (IsAuthenticated,)


class DeleteAuthorAPIView(DestroyAPIView):
    queryset = Author.objects.all()
    permission_classes = (IsAuthenticated,)


class DetailAuthorAPIView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = DetailAuthorSerializer
    permission_classes = (IsAuthenticated,)


class ListAuthorAPIView(ListAPIView):
    queryset = Author.objects.only(
        "first_name", "last_name", "date_of_birth", "date_of_death"
    )
    serializer_class = ListAuthorSerializer
    permission_classes = (IsAuthenticated,)


class UpdateAuthorAPIView(UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = CreateUpdateAuthorSerializer
    permission_classes = (IsAuthenticated,)
