from django.urls import path
from apps.authors.views import crud


urlpatterns = [
    path("", crud.ListAuthorAPIView.as_view(), name="author-list"),
    path("create/", crud.CreateAuthorAPIView.as_view(), name="author-create"),
    path("<int:pk>/", crud.DetailAuthorAPIView.as_view(), name="author-detail"),
    path("<int:pk>/update/", crud.UpdateAuthorAPIView.as_view(), name="author-update"),
    path("<int:pk>/delete/", crud.DeleteAuthorAPIView.as_view(), name="author-delete"),
]
