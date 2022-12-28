# Generated by Django 3.2.7 on 2022-08-20 16:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0002_alter_event_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="question",
            name="form",
        ),
        migrations.AddField(
            model_name="application",
            name="form_answer",
            field=models.JSONField(
                default=dict, verbose_name="Réponse de formulaire"
            ),
        ),
        migrations.AddField(
            model_name="form",
            name="json_schema",
            field=models.JSONField(
                default=dict,
                help_text=(
                    "The JSON schema of the Form.\nYou can use <a"
                    ' href="https://jsonforms-editor.netlify.app/">this'
                    " website</a> to generate your form"
                ),
                verbose_name="JSON Schema",
            ),
        ),
        migrations.AddField(
            model_name="form",
            name="ui_schema",
            field=models.JSONField(
                default=dict,
                help_text=(
                    "The UI schema of the Form.\nYou can use <a"
                    ' href="https://jsonforms-editor.netlify.app/">this'
                    " website</a> to generate your form"
                ),
                verbose_name="UI Schema",
            ),
        ),
        migrations.DeleteModel(
            name="FormAnswer",
        ),
        migrations.DeleteModel(
            name="Question",
        ),
    ]
