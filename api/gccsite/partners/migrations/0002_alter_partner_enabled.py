# Generated by Django 3.2.7 on 2022-05-07 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='enabled',
            field=models.BooleanField(default=True, verbose_name='Actif'),
        ),
    ]
