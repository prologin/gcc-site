# Generated by Django 4.2.2 on 2023-08-23 17:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0002_application_notes_address_resp"),
    ]

    operations = [
        migrations.AddField(
            model_name="application",
            name="email_resp",
            field=models.EmailField(
                default="example@prologin.org",
                max_length=254,
                verbose_name="Adresse email du responable légal",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="first_name_resp",
            field=models.CharField(
                default="Prologin",
                max_length=256,
                verbose_name="Prénom du responsable légal",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="last_name_resp",
            field=models.CharField(
                default="Prologin",
                max_length=256,
                verbose_name="Nom du responsable légal",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="application",
            name="address",
            field=models.JSONField(
                default=dict, verbose_name="Adresse de la participante"
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="address_resp",
            field=models.JSONField(
                default=dict, verbose_name="Adresse du responsable légal"
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="dob",
            field=models.DateField(
                verbose_name="Date de naissance de la participante"
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="first_name",
            field=models.CharField(
                max_length=256, verbose_name="Prénom de la participante"
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="last_name",
            field=models.CharField(
                max_length=256, verbose_name="Nom de la participante"
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="phone",
            field=models.CharField(
                blank=True,
                max_length=16,
                verbose_name="Numéro de téléphone du responsable légal",
            ),
        ),
    ]