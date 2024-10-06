from django.db.models import QuerySet
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    ListAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated

from apps.books.query_params import BookFilter, BookSearch, BookSort
from apps.books.models import Book
from apps.books.serializers.crud import (
    DetailBookSerializer,
    ListBookSerializer,
    CreateUpdateBookSerializer,
)


class CreateBookAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = CreateUpdateBookSerializer
    permission_classes = (IsAuthenticated,)


class DeleteBookAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    permission_classes = (IsAuthenticated,)


class DetailBookAPIView(RetrieveAPIView):
    queryset = Book.objects.prefetch_related("authors")
    serializer_class = DetailBookSerializer
    permission_classes = (IsAuthenticated,)


class ListBookAPIView(ListAPIView):
    serializer_class = ListBookSerializer
    filter_class = BookFilter
    search_class = BookSearch
    sort_class = BookSort
    permission_classes = (IsAuthenticated,)

    def get_queryset(self) -> QuerySet:
        """
        Depending on the query params, it searches, filters and sorts.

        :return: queryset
        """
        queryset = Book.objects.all()
        query_params = self.request.query_params
        if query_params:
            queryset = self.filter_class.get_filtered_queryset(query_params, queryset)
            queryset = self.search_class.get_searched_queryset(query_params, queryset)
            queryset = self.sort_class.get_sorted_queryset(query_params, queryset)
        return queryset


class UpdateBookAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = CreateUpdateBookSerializer
    permission_classes = (IsAuthenticated,)
