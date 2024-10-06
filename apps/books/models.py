from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.authors.models import Author
from apps.books.constants import GENRE_CHOICES


class Book(models.Model):
    title = models.CharField(
        max_length=255, blank=False, null=False, db_index=True, verbose_name=_("Title")
    )
    summary = models.TextField(blank=False, null=False, verbose_name=_("Summary"))
    isbn = models.CharField(
        max_length=13, unique=True, db_index=True, verbose_name=_("ISBN")
    )
    authors = models.ManyToManyField(
        to=Author, blank=False, verbose_name=_("Authors"), related_name="author_books"
    )
    genre = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        db_index=True,
        choices=GENRE_CHOICES,
        verbose_name=_("Genre"),
    )
    publication_date = models.DateField(
        blank=False,
        null=False,
        db_index=True,
        auto_now_add=True,
        verbose_name=_("Publication date"),
    )

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"id: {self.pk}, title: {self.title}"

    class Meta:
        db_table = "books"
        verbose_name = _("Book")
        verbose_name_plural = _("Books")
