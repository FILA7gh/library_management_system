from django.urls import path
from apps.favorites.views import crud


urlpatterns = [
    path("", crud.ListFavoriteBookAPIView.as_view(), name="favorite-book-list"),
    path(
        "create/", crud.CreateFavoriteBookAPIView.as_view(), name="favorite-book-create"
    ),
    path(
        "<int:pk>/",
        crud.DetailFavoriteBookAPIView.as_view(),
        name="favorite-book-detail",
    ),
    path(
        "<int:pk>/delete/",
        crud.DeleteFavoriteBookAPIView.as_view(),
        name="favorite-book-delete",
    ),
]
