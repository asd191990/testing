# Generated by Django 2.2.6 on 2020-01-15 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('use_app', '0015_auto_20191206_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='people_data',
            name='time',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]