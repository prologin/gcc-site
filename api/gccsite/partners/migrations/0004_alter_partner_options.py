# Generated by Django 3.2.7 on 2022-07-05 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0003_auto_20220509_1052'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partner',
            options={'ordering': ('-enabled', '-featured', '-is_on_front_page', 'order'), 'verbose_name': 'partenaire', 'verbose_name_plural': 'partenaires'},
        ),
    ]
