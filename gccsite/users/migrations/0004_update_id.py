# Generated by Django 2.2.3 on 2019-07-11 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('users', '0003_auto_20190319_1901')]

    operations = [
        migrations.AlterField(
            model_name='gccuser',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        )
    ]
