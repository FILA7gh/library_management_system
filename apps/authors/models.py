from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    first_name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        db_index=True,
        verbose_name=_("First name"),
    )
    last_name = models.CharField(
        max_length=255, blank=False, null=False, verbose_name=_("Last name")
    )
    biography = models.TextField(blank=False, null=False, verbose_name=_("Biography"))
    date_of_birth = models.DateField(
        blank=False, null=False, db_index=True, verbose_name=_("Date of birth")
    )
    date_of_death = models.DateField(
        blank=True, null=False, db_index=True, verbose_name=_("Date of death")
    )

    def __str__(self):
        return self.first_name

    def __repr__(self):
        return f"id: {self.pk}, title: {self.first_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = "authors"
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")
        constraints = [
            models.UniqueConstraint(
                fields=["first_name", "last_name", "date_of_birth", "date_of_death"],
                name="unique_author",
            )
        ]
