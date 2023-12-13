# Generated by Django 4.2.7 on 2023-12-13 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_profile_responsable'),
        ('applications', '0004_remove_application_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='responsable',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='responsable', to='users.profile', verbose_name='Profil du responsable légal'),
            preserve_default=False,
        ),
    ]
