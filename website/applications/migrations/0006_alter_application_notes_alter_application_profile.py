# Generated by Django 4.2.7 on 2023-12-18 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('applications', '0005_alter_application_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Notes sur la candidatures'),
        ),
        migrations.AlterField(
            model_name='application',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='applications', to='profiles.profile', verbose_name='Profil'),
        ),
    ]
