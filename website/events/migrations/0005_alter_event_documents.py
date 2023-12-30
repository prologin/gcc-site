# Generated by Django 4.2.7 on 2023-12-30 23:28

import django.core.validators
from django.db import migrations, models
import events.validators


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_remove_eventdocument_document_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='documents',
            field=models.FileField(blank=True, null=True, upload_to='events_gcc/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('pdf',)), events.validators.validate_is_pdf, events.validators.validate_file_max_size], verbose_name='Documents'),
        ),
    ]
