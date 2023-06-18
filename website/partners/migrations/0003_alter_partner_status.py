# Generated by Django 4.2.2 on 2023-06-18 18:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("partners", "0002_partneradmin"),
    ]

    operations = [
        migrations.AlterField(
            model_name="partner",
            name="status",
            field=models.CharField(
                choices=[
                    ("Promoted", "Partenaires qui nous soutiennent"),
                    ("Funding", "Partenaires qui nous financent"),
                    ("Welcoming", "Partenaires qui nous accueillent"),
                ],
                default="Promoted",
                max_length=20,
                verbose_name="Statut",
            ),
        ),
    ]
