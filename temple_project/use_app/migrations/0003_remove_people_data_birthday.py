# Generated by Django 2.2.6 on 2019-10-29 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('use_app', '0002_auto_20191029_1954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people_data',
            name='birthday',
        ),
    ]
