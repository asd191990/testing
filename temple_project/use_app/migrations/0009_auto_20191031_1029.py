# Generated by Django 2.2.6 on 2019-10-31 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('use_app', '0008_auto_20191031_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people_data',
            name='home_id',
            field=models.CharField(max_length=10),
        ),
    ]
