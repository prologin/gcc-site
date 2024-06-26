# Generated by Django 4.2.7 on 2023-11-16 23:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0003_remove_application_event_remove_application_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Titre')),
            ],
            options={
                'verbose_name': 'label participant',
                'verbose_name_plural': 'labels participant',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, verbose_name='Prénom de la participante')),
                ('last_name', models.CharField(max_length=256, verbose_name='Nom de la participante')),
                ('dob', models.DateField(verbose_name='Date de naissance de la participante')),
                ('email', models.EmailField(max_length=254, verbose_name='Adresse email de la participante')),
                ('phone', models.CharField(blank=True, max_length=16, verbose_name='Numéro de téléphone de la participante')),
                ('address', models.JSONField(default=dict, verbose_name='Adresse de la participante')),
                ('first_name_resp', models.CharField(max_length=256, verbose_name='Prénom du responsable légal')),
                ('last_name_resp', models.CharField(max_length=256, verbose_name='Nom du responsable légal')),
                ('email_resp', models.EmailField(max_length=254, verbose_name='Adresse email du responable légal')),
                ('phone_resp', models.CharField(blank=True, max_length=16, verbose_name='Numéro de téléphone du responsable légal')),
                ('address_resp', models.JSONField(default=dict, verbose_name='Adresse du responsable légal')),
                ('school', models.JSONField(default=dict, verbose_name='Etablissement scolaire de la participante')),
                ('form_answer', models.JSONField(default=dict, verbose_name='Réponse de formulaire')),
                ('nb_participations', models.CharField(default='', verbose_name='Nombre de participations de la participante')),
                ('notes', models.TextField(verbose_name='Notes sur la candidatures')),
                ('status', models.SmallIntegerField(choices=[(-3, 'Candidature rejetée'), (-2, 'Candidature annulée par la candidate'), (-1, 'Candidature annulée par les organisateurs'), (0, 'Candidature en cours de traitement'), (1, 'Candidature acceptée'), (2, 'Candidature confirmée'), (3, 'Stage terminé')], default=0, verbose_name='Statut de la candidature')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name="Date d'inscription")),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='events.event', verbose_name='Évènement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'candidatures',
                'verbose_name_plural': 'candidatures',
            },
        ),
    ]
