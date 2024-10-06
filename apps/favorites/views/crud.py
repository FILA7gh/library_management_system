from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    ListAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.favorites.serializers.crud import (
    CreateFavoriteBookSerializer,
    DetailFavoriteBookSerializer,
    ListFavoriteBookSerializer,
)
from apps.favorites.models import FavoriteBook


class CreateFavoriteBookAPIView(CreateAPIView):
    queryset = FavoriteBook.objects.all()
    serializer_class = CreateFavoriteBookSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        """
        adds to favorites only for the current user
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = request.user.id
        serializer.save(user_id=user_id)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class DeleteFavoriteBookAPIView(DestroyAPIView):
    queryset = FavoriteBook.objects.all()
    permission_classes = (IsAuthenticated,)


class DetailFavoriteBookAPIView(RetrieveAPIView):
    queryset = FavoriteBook.objects.all()
    serializer_class = DetailFavoriteBookSerializer
    permission_classes = (IsAuthenticated,)


class ListFavoriteBookAPIView(ListAPIView):
    serializer_class = ListFavoriteBookSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        shows the favorites list of only the current user
        """
        user_id = self.request.user.id
        queryset = (
            FavoriteBook.objects.select_related("book", "user")
            .filter(user_id=user_id)
            .only("id", "book", "user")
        )
        return queryset
