# Generated by Django 3.2.7 on 2022-04-15 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Nom')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Description')),
                ('website_url', models.URLField(blank=True, null=True, verbose_name='URL du site')),
                ('featured', models.BooleanField(default=False, verbose_name='Mis en avant')),
                ('logo', models.FileField(upload_to='', verbose_name='Logo')),
                ('enabled', models.BooleanField(verbose_name='Activé')),
                ('order', models.PositiveIntegerField(default=1, verbose_name='Ordre')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
    ]
