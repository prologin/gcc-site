# Generated by Django 4.2.7 on 2023-12-16 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=64, verbose_name='Nom et numéro de voie')),
                ('complement', models.CharField(blank=True, max_length=64, verbose_name="Complément d'adressse (si nécessaire)")),
                ('city', models.CharField(max_length=64, verbose_name='Ville')),
                ('zipcode', models.CharField(max_length=16, verbose_name='Code postal')),
                ('country', models.CharField(max_length=32, verbose_name='Pays')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, verbose_name='Prénom de la participante')),
                ('last_name', models.CharField(max_length=256, verbose_name='Nom de la participante')),
                ('birth_date', models.DateField(verbose_name='Date de naissance de la participante')),
                ('email', models.EmailField(max_length=254, verbose_name='Adresse email de la participante')),
                ('phone', models.CharField(blank=True, max_length=16, verbose_name='Numéro de téléphone de la participante')),
                ('first_name_resp', models.CharField(max_length=256, verbose_name='Prénom du responsable légal')),
                ('last_name_resp', models.CharField(max_length=256, verbose_name='Nom du responsable légal')),
                ('email_resp', models.EmailField(default='', max_length=254, verbose_name='Adresse email du responable légal')),
                ('phone_resp', models.CharField(blank=True, max_length=16, verbose_name='Numéro de téléphone du responsable légal')),
                ('school_name', models.CharField(max_length=64, verbose_name='Etablissement scolaire de la participante')),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='profiles.address', verbose_name='Adresse de la participante')),
                ('address_resp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='profiles.address', verbose_name='Adresse du responsable légal')),
                ('school_address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='profiles.address', verbose_name="Adresse de l'établissement scolaire")),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
        ),
    ]
