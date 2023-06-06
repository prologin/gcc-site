# Generated by Django 4.2 on 2023-06-06 17:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0004_remove_event_form_application_phone_delete_form"),
    ]

    operations = [
        migrations.AddField(
            model_name="application",
            name="school",
            field=models.JSONField(
                default=dict,
                verbose_name="Etablissement scolaire de la participante",
            ),
        ),
    ]
