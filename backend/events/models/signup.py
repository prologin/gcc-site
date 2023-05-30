from django.contrib.auth import get_user_model
from django.utils.functional import cached_property
from django.db import models
from django.utils.translation import gettext_lazy as _


class SelectionStatus(models.IntegerChoices):
    ABANDONED = -1, _("Abandonné")
    ENROLLED = 0, _("Inscrit")
    NOT_SELECTED = 1, _("Non sélectionné")
    SELECTED = 2, _("Sélectionné")
    ACCEPTED = 3, _("Accepté")
    CONFIRMED = 4, _("Confirmé")

class ApplicationManager(models.Manager):
    def get_applicants(self, event):
        return self.filter(event=event)

class Application(models.Model):
    user = models.ForeignKey(
        to=get_user_model(),
        verbose_name=_("Utilisateur"),
        on_delete=models.CASCADE,
        related_name="applications",
    )

    first_name = models.CharField(
        max_length=256,
        verbose_name=_("Prénom"),
    )

    last_name = models.CharField(
        max_length=256,
        verbose_name=_("Nom"),
    )

    dob = models.DateField(
        verbose_name=_("Date de naissance"),
    )

    event = models.ForeignKey(
        to="events.Event",
        verbose_name=_("Évènement"),
        on_delete=models.CASCADE,
        related_name="applications",
    )

    status = models.SmallIntegerField(
        choices=SelectionStatus.choices,
        verbose_name=_("Statut de la candidature"),
    )

    labels = models.ManyToManyField(
        to="events.ApplicationLabel",
        blank=True,
        verbose_name=_("Labels"),
    )

    created_at = models.DateTimeField(
        verbose_name=_("Date d'inscription"),
        auto_now_add=True,
    )

    objects = ApplicationManager()

    @cached_property
    def participations_count(self):
        applicants = Application.objects.filter(event=self.event)
        return sum(
            (applicant.status == SelectionStatus.CONFIRMED.value)
            for applicant in applicants if (applicant.last_name == self.last_name and applicant.first_name == self.first_name)
        )

    class Meta:
        verbose_name = _("candidatures")
        verbose_name_plural = _("candidatures")

    def __str__(self):
        return f"{self.first_name} {self.last_name}@{self.event}"


class ApplicationLabel(models.Model):
    title = models.CharField(max_length=120, verbose_name=_("Titre"))

    class Meta:
        verbose_name = _("label participant")
        verbose_name_plural = _("labels participant")
        ordering = ("title",)

    def __str__(self):
        return self.title