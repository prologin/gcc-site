# Generated by Django 4.2 on 2023-05-31 12:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0004_remove_event_form"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Form",
        ),
        migrations.RemoveField(
            model_name="application",
            name="form_answer",
        ),
    ]