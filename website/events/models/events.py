from django.conf import settings
from django.utils.module_loading import import_string
from django.core.validators import FileExtensionValidator, ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from events.validators import validate_is_pdf
from events.tasks import expense_report_generate_document
class Address(models.Model):
    street = models.CharField(
        verbose_name=_("Numéro et nom de voie"),
        max_length=250,
    )
    complement = models.CharField(
        verbose_name=_("Complément d'adresse"),
        max_length=200,
        blank=True,
        null=True,
    )
    city = models.CharField(verbose_name=_("Ville"), max_length=50)
    zip_code = models.IntegerField(verbose_name=_("Code postal"))
    country = models.CharField(
        verbose_name=_("Pays"), max_length=30, default="France"
    )
    center = models.OneToOneField(
        to="events.Center",
        on_delete=models.CASCADE,
        verbose_name=_("Centre"),
    )

    lat = models.DecimalField(
        verbose_name=_("Latitude"),
        max_digits=14,
        decimal_places=10,
        null=True,
        blank=True,
    )
    lng = models.DecimalField(
        verbose_name=_("Longitude"),
        max_digits=14,
        decimal_places=10,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.city}, {self.street}"

    class Meta:
        verbose_name = _("Adresse")
        verbose_name_plural = _("Adresses")


class Center(models.Model):
    name = models.CharField(verbose_name=_("Nom"), max_length=120)

    private_notes = models.TextField(
        verbose_name=_("Notes privées"), max_length=2000, blank=True, null=True
    )

    class Meta:
        verbose_name = _("centre")
        verbose_name_plural = _("centres")

    def __str__(self):
        return self.name


class EventManager(models.Manager):
    def get_open_events(self):
        return self.filter(
            signup_start_date__lte=timezone.now(),
            signup_end_date__gt=timezone.now(),
        )

    def get_visible_events(self):
        return self.filter(signup_start_date__lte=timezone.now())


class Event(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name=_("Nom de l'évènement"),
    )

    center = models.ForeignKey(
        to="events.Center",
        verbose_name=_("Centre"),
        on_delete=models.CASCADE,
    )

    year = models.PositiveIntegerField(verbose_name=_("Année de l'événement"))

    signup_start_date = models.DateTimeField(
        verbose_name=_("Date de début d'inscription")
    )
    signup_end_date = models.DateTimeField(
        verbose_name=_("Date de fin d'inscription")
    )

    start_date = models.DateTimeField(verbose_name=_("Date de début"))
    end_date = models.DateTimeField(verbose_name=_("Date de fin"))


    document = models.FileField(
        upload_to="events_gcc/",
        validators=(
            FileExtensionValidator(allowed_extensions=("pdf",)),
            validate_is_pdf,
        ),
        null=True,
        blank=True,
    )


    notes = models.TextField(
        verbose_name=_("Notes"),
        help_text=_(
            "Ce texte, si défini, est affiché lors de l'inscription à"
            " l'évènement (il peut éventuellement contenir des liens)"
        ),
        blank=True,
        null=True,
    )

    description = models.TextField(
        verbose_name=_("Description de l'évènement"),
    )

    objects = EventManager()

    @property
    def is_open(self):
        return (
            self.signup_start_date <= timezone.now()
            and self.signup_end_date > timezone.now()
        )

    class Meta:
        verbose_name = _("évènement")
        verbose_name_plural = _("évènements")

    def __str__(self):
        return self.name

    def clean(self):
        errors = {}

        if self.signup_start_date > self.signup_end_date:
            errors["signup_start_date"] = _(
                "La date début d'inscription doit être avant la date de "
                "fin d'inscription."
            )

        if self.signup_end_date > self.start_date:
            errors["signup_end_date"] = _(
                "La date de fin d'inscription doit être avant "
                "la date de début d'évènement."
            )

        if self.start_date > self.end_date:
            errors["end_date"] = _(
                "La date de fin d'évènement doit être après "
                "la date de début d'évènement."
            )

        if errors:
            raise ValidationError(errors)

    def generate_document(self):
        print("cc")
        expense_report_generate_document.delay(self.pk)
        self.save()

    def get_application_questions(self, mandatory_only=False):
        if mandatory_only:
            return self.form.questions.filter(mandatory=True)
        else:
            return self.form.questions.all()
