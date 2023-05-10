# Generated by Django 4.2 on 2023-05-31 12:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0005_delete_form_remove_application_form_answer"),
    ]

    operations = [
        migrations.AddField(
            model_name="application",
            name="about",
            field=models.TextField(
                default="rien", verbose_name="Association et stages"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="allergies",
            field=models.TextField(default="rien", verbose_name="Allergies"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="diet",
            field=models.TextField(
                default="rien", verbose_name="Régime Alimentaire"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="learning",
            field=models.TextField(
                default="rien", verbose_name="Apprentisage"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="programming",
            field=models.TextField(
                default="rien", verbose_name="Programmation"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="studies",
            field=models.TextField(default="rien", verbose_name="Etudes"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="tshirt",
            field=models.SmallIntegerField(
                choices=[
                    (1, "XS"),
                    (2, "S"),
                    (3, "M"),
                    (4, "L"),
                    (5, "XL"),
                    (6, "XXL"),
                ],
                default=1,
                verbose_name="Taille du t-shirt",
            ),
            preserve_default=False,
        ),
    ]