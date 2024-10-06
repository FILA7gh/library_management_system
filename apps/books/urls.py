from django.urls import path
from apps.books.views import crud


urlpatterns = [
    path("", crud.ListBookAPIView.as_view(), name="book-list"),
    path("create/", crud.CreateBookAPIView.as_view(), name="book-create"),
    path("<int:pk>/", crud.DetailBookAPIView.as_view(), name="book-detail"),
    path("<int:pk>/update/", crud.UpdateBookAPIView.as_view(), name="book-update"),
    path("<int:pk>/delete/", crud.DeleteBookAPIView.as_view(), name="book-delete"),
]
