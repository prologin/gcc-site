# Generated by Django 4.2.2 on 2023-06-19 20:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("partners", "0003_alter_partner_status"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="partner",
            options={
                "verbose_name": "Partenaire",
                "verbose_name_plural": "Partenaires",
            },
        ),
        migrations.DeleteModel(
            name="PartnerAdmin",
        ),
    ]
