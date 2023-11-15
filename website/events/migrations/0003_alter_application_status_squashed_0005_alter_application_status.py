# Generated by Django 4.2.7 on 2023-11-15 15:50

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    replaces = [('events', '0003_alter_application_status'), ('events', '0004_alter_application_options'), ('events', '0005_alter_application_status')]

    dependencies = [
        ('events', '0002_alter_event_options_application_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=django_fsm.FSMField(choices=[(-3, 'Candidature rejetée'), (-2, 'Candidature annulée de la part de la candidate'), (-1, 'Candidature annulée de la part des organisateurs'), (0, 'Candidature en cours de traitement'), (1, 'Candidature acceptée'), (2, 'Candidature confirmée'), (3, 'Stage terminé')], default=0, max_length=50, protected=True, verbose_name='Statut de la candidature'),
        ),
        migrations.AlterModelOptions(
            name='application',
            options={'permissions': [('manage_applications', 'Can manage the status of applications'), ('override_applications', 'Can override the application status flow')], 'verbose_name': 'candidatures', 'verbose_name_plural': 'candidatures'},
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=django_fsm.FSMIntegerField(choices=[(-3, 'Candidature rejetée'), (-2, 'Candidature annulée de la part de la candidate'), (-1, 'Candidature annulée de la part des organisateurs'), (0, 'Candidature en cours de traitement'), (1, 'Candidature acceptée'), (2, 'Candidature confirmée'), (3, 'Stage terminé')], default=0, protected=True, verbose_name='Statut de la candidature'),
        ),
    ]
