from django.db import models
from django.utils.translation import ugettext_lazy as _


class Partner(models.Model):
    name = models.CharField(
        verbose_name=_("Nom"),
        max_length=256,
    )

    description = models.TextField(
        verbose_name=_("Description"),
        max_length=2_000,
        blank=True,
        null=True,
    )

    website_url = models.URLField(
        verbose_name=_("URL du site"),
        blank=True,
        null=True,
    )

    is_on_front_page = models.BooleanField(
        verbose_name=_("Affiché sur la page d'accueil"),
        default=False,
        editable=True,
    )

    # Indicates if the partner is featured
    # e.g. featured partners are displayed higher on the front page, etc.
    featured = models.BooleanField(
        verbose_name=_("Mis en avant"),
        default=False,
        editable=True,
    )

    logo = models.FileField(
        verbose_name=_("Logo"),
    )

    enabled = models.BooleanField(
        verbose_name=_("Actif"),
        default=True,
    )

    # Order in which partners are supposed to be "ranked", can be use to force
    # partners before or after others.
    # Lower values are more important.
    order = models.PositiveIntegerField(
        verbose_name=_("Ordre"),
        default=0,
    )

    class Meta:
        verbose_name = _("partenaire")
        verbose_name_plural = _("partenaires")

        ordering = (
            "-enabled",
            "-featured",
            "-is_on_front_page",
            "order",
        )

    def __str__(self):
        return self.name
