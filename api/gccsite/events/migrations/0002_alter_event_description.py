# Generated by Django 3.2.7 on 2022-08-19 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(verbose_name="Description de l'évènement"),
        ),
    ]
