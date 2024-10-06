from typing import Dict

from django.db.models import QuerySet


class BookFilter:
    @staticmethod
    def get_filtered_queryset(query_params: Dict, queryset: QuerySet) -> QuerySet:
        """
        Filters the queryset based on the provided query parameters.

        :param query_params: Book filter query params
        :param queryset: Book queryset
        :return: Filtered queryset
        """
        for key, value in query_params.items():
            if key == "author_id":
                queryset = queryset.filter(authors__id__in=value)
            elif key == "genre":
                queryset = queryset.filter(genre=value)
            elif key == "publication_date":
                queryset = queryset.filter(publication_date=value)
        return queryset


class BookSearch:
    @staticmethod
    def get_searched_queryset(query_params: Dict, queryset: QuerySet) -> QuerySet:
        """
        Searches the queryset based on the provided query parameters.

        :param query_params: Book search query params
        :param queryset: Book queryset
        :return: Searched queryset
        """
        for key, value in query_params.items():
            if key == "search_title":
                queryset = queryset.filter(title__icontains=value)
            elif key == "search_author_last_name":
                queryset = queryset.filter(authors__last_name__icontains=value)
        return queryset


class BookSort:
    @staticmethod
    def get_sorted_queryset(query_params: Dict, queryset: QuerySet) -> QuerySet:
        """
        Sorts the queryset based on the provided query parameters.

        :param query_params: Book sorting query params
        :param queryset: Book queryset
        :return: Sorted queryset
        """
        sort_order = query_params.get("sort")

        if sort_order:
            if sort_order == "author_name":
                queryset = queryset.order_by("authors__first_name")
            elif sort_order == "publication_date":
                queryset = queryset.order_by("publication_date")
            elif sort_order == "genre":
                queryset = queryset.order_by("genre")
        return queryset
