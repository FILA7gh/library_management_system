from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.books.models import Book
from apps.users.models import CustomUser


class FavoriteBook(models.Model):
    user = models.ForeignKey(
        to=CustomUser,
        blank=False,
        null=False,
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        related_name="user_favorite",
    )
    book = models.ForeignKey(
        to=Book,
        blank=False,
        null=False,
        verbose_name=_("Book"),
        on_delete=models.CASCADE,
        related_name="book_favorite",
    )
    created_at = models.DateTimeField(
        blank=True,
        null=False,
        auto_now_add=True,
        verbose_name=_("Created at"),
        db_index=True,
    )

    def __str__(self):
        return f"{self.user} {self.book}"

    def __repr__(self):
        return f"id: {self.pk}, user: {self.user}, book: {self.book}"

    class Meta:
        db_table = "favorite_books"
        verbose_name = "Favorite book"
        verbose_name_plural = "Favorite books"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "book"], name="unique_favorite_book"
            )
        ]
