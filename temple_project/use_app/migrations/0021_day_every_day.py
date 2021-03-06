# Generated by Django 2.2.6 on 2020-03-17 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('use_app', '0020_auto_20200128_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_name', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='every_day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_lights', models.TextField()),
                ('two_lights', models.TextField()),
                ('three_lights', models.TextField()),
                ('four_lights', models.TextField()),
                ('five_lights', models.TextField()),
                ('date', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='firm', to='use_app.Day')),
            ],
            options={
                'verbose_name_plural': '燈的紀錄',
            },
        ),
    ]
