from django.db import models


class Partner(models.Model):
    name = models.CharField(
        verbose_name="Nom",
        max_length=256,
    )

    description = models.TextField(
        verbose_name="Description",
        max_length=2_000,
        blank=True,
        null=True,
    )

    website_url = models.URLField(
        verbose_name="URL du site",
        blank=True,
        null=True,
    )

    is_on_front_page = models.BooleanField(
        verbose_name="Affiché sur la page d'accueil",
        default=False,
        editable=True,
    )

    # Indicates if the partner is featured
    # e.g. featured partners are displayed higher on the front page, etc.
    featured = models.BooleanField(
        verbose_name="Mis en avant",
        default=False,
        editable=True,
    )

    logo = models.FileField(
        verbose_name="Logo",
    )

    enabled = models.BooleanField(
        verbose_name="Actif",
        default=True,
    )

    # Order in which partners are supposed to be "ranked", can be use to force
    # partners before or after others.
    # Lower values are more important.
    order = models.PositiveIntegerField(
        verbose_name="Ordre",
        default=0,
    )

    class Meta:
        verbose_name = "partenaire"
        verbose_name_plural = "partenaires"

        ordering = (
            "-enabled",
            "-featured",
            "-is_on_front_page",
            "order",
        )

    def __str__(self):
        return self.name
