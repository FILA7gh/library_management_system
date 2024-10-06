from unittest.mock import patch

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from django.test import TestCase

from apps.authors.models import Author
from apps.authors.serializers.crud import DetailAuthorSerializer, ListAuthorSerializer
from apps.users.models import CustomUser


class AuthorModelTestCase(TestCase):
    @patch(
        "apps.authors.models.Author.save"
    )
    def test_author_creation(self, mock_save):
        author = Author(first_name="John", last_name="Doe", date_of_birth="1990-01-01")
        author.save()
        mock_save.assert_called_once()

    def test_author_str(self):
        author = Author(first_name="John", last_name="Doe", date_of_birth="1990-01-01")
        self.assertEqual(str(author), "John")

    def test_author_update(self):
        author = Author(
            first_name="John",
            last_name="Doe",
            date_of_birth="1990-01-01",
            date_of_death="1990-01-01",
        )
        author.save()
        author.last_name = "Smith"
        author.save()
        self.assertEqual(author.last_name, "Smith")

    def test_author_delete(self):
        author = Author(
            first_name="John",
            last_name="Doe",
            date_of_birth="1990-01-01",
            date_of_death="1990-01-01",
        )
        author.save()
        author.delete()
        self.assertEqual(Author.objects.count(), 0)


class AuthorAPITestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="testuser", password="testpass"
        )

    @patch("apps.authors.models.Author.objects.create")
    def test_create_author(self, mock_create):
        self.client.force_authenticate(user=self.user)

        mock_create.return_value = Author(
            first_name="Jane",
            last_name="Doe",
            date_of_birth="1995-01-01",
            date_of_death="1995-02-02",
        )
        url = reverse("author-create")
        data = {"first_name": "Jane", "last_name": "Doe", "date_of_birth": "1995-01-01"}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        mock_create.assert_called_once_with(**data)

    @patch("apps.authors.models.Author.objects.get")
    @patch("apps.authors.models.Author.delete")
    def test_delete_author(self, mock_delete, mock_get):
        self.client.force_authenticate(user=self.user)

        mock_get.return_value = Author(first_name="John", last_name="Doe")
        url = reverse("author-delete", kwargs={"pk": 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        mock_delete.assert_called_once()

    @patch("apps.author.models.Author.objects.get")
    def test_detail_author(self, mock_get):
        mock_get.return_value = Author(
            first_name="John", last_name="Doe", date_of_birth="1990-01-01"
        )
        url = reverse("author-detail", kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = DetailAuthorSerializer(mock_get.return_value)
        self.assertEqual(
            response.data, serializer.data
        )  # Проверяем соответствие данных

    @patch("apps.authors.models.Author.objects.all")
    def test_list_authors(self, mock_all):
        mock_all.return_value = [Author(first_name="John", last_name="Doe")]
        url = reverse("author-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = ListAuthorSerializer(mock_all.return_value, many=True)
        self.assertEqual(
            response.data, serializer.data
        )  # Проверяем соответствие данных

    @patch("apps.authors.models.Author.objects.get")
    def test_update_author(self, mock_get):
        mock_author = Author(
            first_name="John", last_name="Doe", date_of_birth="1990-01-01"
        )
        mock_get.return_value = mock_author
        url = reverse("author-update", kwargs={"pk": 1})
        data = {
            "first_name": "John",
            "last_name": "Smith",
            "date_of_birth": "1990-01-01",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(mock_author.last_name, "Smith")
