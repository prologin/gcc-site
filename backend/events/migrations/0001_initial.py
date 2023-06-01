# Generated by Django 4.2 on 2023-06-01 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pathlib


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ApplicationLabel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=120, verbose_name="Titre"),
                ),
            ],
            options={
                "verbose_name": "label participant",
                "verbose_name_plural": "labels participant",
                "ordering": ("title",),
            },
        ),
        migrations.CreateModel(
            name="Center",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120, verbose_name="Nom")),
                (
                    "private_notes",
                    models.TextField(
                        blank=True,
                        max_length=2000,
                        null=True,
                        verbose_name="Notes privées",
                    ),
                ),
            ],
            options={
                "verbose_name": "centre",
                "verbose_name_plural": "centres",
            },
        ),
        migrations.CreateModel(
            name="Document",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "admin_name",
                    models.CharField(
                        help_text="Ce nom est uniquement utilisé pour l'admin django",
                        max_length=260,
                        unique=True,
                        verbose_name="Nom du document",
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        upload_to=pathlib.PurePosixPath("events/documents"),
                        verbose_name="Fichier",
                    ),
                ),
            ],
            options={
                "verbose_name": "document",
                "verbose_name_plural": "documents",
            },
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=256, verbose_name="Nom de l'évènement"
                    ),
                ),
                (
                    "year",
                    models.PositiveIntegerField(
                        verbose_name="Année de l'événement"
                    ),
                ),
                (
                    "signup_start_date",
                    models.DateTimeField(
                        verbose_name="Date de début d'inscription"
                    ),
                ),
                (
                    "signup_end_date",
                    models.DateTimeField(
                        verbose_name="Date de fin d'inscription"
                    ),
                ),
                (
                    "start_date",
                    models.DateTimeField(verbose_name="Date de début"),
                ),
                ("end_date", models.DateTimeField(verbose_name="Date de fin")),
                (
                    "notes",
                    models.TextField(
                        blank=True,
                        help_text="Ce texte, si défini, est affiché lors de l'inscription à l'évènement (il peut éventuellement contenir des liens)",
                        null=True,
                        verbose_name="Notes",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        verbose_name="Description de l'évènement"
                    ),
                ),
                (
                    "center",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="events.center",
                        verbose_name="Centre",
                    ),
                ),
            ],
            options={
                "verbose_name": "évènement",
                "verbose_name_plural": "évènements",
            },
        ),
        migrations.CreateModel(
            name="Form",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120, verbose_name="Nom")),
                (
                    "json_schema",
                    models.JSONField(
                        default=dict,
                        help_text='The JSON schema of the Form.\nYou can use <a href="https://jsonforms-editor.netlify.app/">this website</a> to generate your form',
                        verbose_name="JSON Schema",
                    ),
                ),
                (
                    "ui_schema",
                    models.JSONField(
                        default=dict,
                        help_text='The UI schema of the Form.\nYou can use <a href="https://jsonforms-editor.netlify.app/">this website</a> to generate your form',
                        verbose_name="UI Schema",
                    ),
                ),
            ],
            options={
                "verbose_name": "formulaire",
                "verbose_name_plural": "formulaires",
            },
        ),
        migrations.CreateModel(
            name="EventDocument",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "display_name",
                    models.CharField(
                        help_text="Le nom public du document qui sera affiché aux participants",
                        max_length=260,
                        verbose_name="Nom public du document",
                    ),
                ),
                (
                    "visibility",
                    models.IntegerField(
                        choices=[
                            (1, "Public"),
                            (2, "Accepté ou confirmé"),
                            (3, "Confirmé seulement"),
                        ],
                        verbose_name="Visibilité",
                    ),
                ),
                (
                    "document",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="events.document",
                        verbose_name="Document",
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="events.event",
                        verbose_name="Évènement",
                    ),
                ),
            ],
            options={
                "verbose_name": "document lié à l'évènement",
                "verbose_name_plural": "documents liés à l'évènement",
            },
        ),
        migrations.AddField(
            model_name="event",
            name="documents",
            field=models.ManyToManyField(
                blank=True,
                related_name="events",
                through="events.EventDocument",
                to="events.document",
                verbose_name="Documents",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="form",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="events.form",
                verbose_name="Formulaire",
            ),
        ),
        migrations.CreateModel(
            name="Application",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=256, verbose_name="Prénom"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=256, verbose_name="Nom"),
                ),
                ("dob", models.DateField(verbose_name="Date de naissance")),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[
                            (-1, "Abandonné"),
                            (0, "Inscrit"),
                            (1, "Non sélectionné"),
                            (2, "Sélectionné"),
                            (3, "Accepté"),
                            (4, "Confirmé"),
                        ],
                        verbose_name="Statut de la candidature",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Date d'inscription"
                    ),
                ),
                (
                    "form_answer",
                    models.JSONField(
                        default=dict, verbose_name="Réponse de formulaire"
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to="events.event",
                        verbose_name="Évènement",
                    ),
                ),
                (
                    "labels",
                    models.ManyToManyField(
                        blank=True,
                        to="events.applicationlabel",
                        verbose_name="Labels",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Utilisateur",
                    ),
                ),
            ],
            options={
                "verbose_name": "candidatures",
                "verbose_name_plural": "candidatures",
            },
        ),
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "street",
                    models.CharField(
                        max_length=250, verbose_name="Numéro et nom de voie"
                    ),
                ),
                (
                    "complement",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Complément d'adresse",
                    ),
                ),
                (
                    "city",
                    models.CharField(max_length=50, verbose_name="Ville"),
                ),
                ("zip_code", models.IntegerField(verbose_name="Code postal")),
                (
                    "country",
                    models.CharField(
                        default="France", max_length=30, verbose_name="Pays"
                    ),
                ),
                (
                    "lat",
                    models.DecimalField(
                        blank=True,
                        decimal_places=10,
                        max_digits=14,
                        null=True,
                        verbose_name="Latitude",
                    ),
                ),
                (
                    "lng",
                    models.DecimalField(
                        blank=True,
                        decimal_places=10,
                        max_digits=14,
                        null=True,
                        verbose_name="Longitude",
                    ),
                ),
                (
                    "center",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="events.center",
                        verbose_name="Centre",
                    ),
                ),
            ],
            options={
                "verbose_name": "Adresse",
                "verbose_name_plural": "Adresses",
            },
        ),
    ]
