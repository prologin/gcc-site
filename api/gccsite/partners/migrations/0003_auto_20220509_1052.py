# Generated by Django 3.2.7 on 2022-05-09 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0002_alter_partner_enabled'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partner',
            options={'ordering': ('-enabled', '-featured', '-is_on_front_page', 'order')},
        ),
        migrations.AddField(
            model_name='partner',
            name='is_on_front_page',
            field=models.BooleanField(default=False, verbose_name="Affiché sur la page d'accueil"),
        ),
        migrations.AlterField(
            model_name='partner',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Ordre'),
        ),
    ]
