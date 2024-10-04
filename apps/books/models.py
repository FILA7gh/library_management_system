from django.db import models
from django.utils.translation import gettext_lazy as _

class Book(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False, db_index=True, verbose_name=_('title'))
    summary = models.TextField(blank=False, null=False, verbose_name=_('summary'))
    isbn = models.CharField(max_length=13, unique=True, db_index=True, verbose_name=_('ISBN'))
    #authors =
    publication_date = models.DateField(
        blank=False,
        null=False,
        db_index=True,
        auto_now_add=True,
        verbose_name=_('publication_date')
    )
    # genre = models.CharField(choices=)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'id: {self.pk}, title: {self.title}'

    class Meta:
        db_table = 'books'
        verbose_name = _('Book')
        verbose_name_plural = _('Books')
