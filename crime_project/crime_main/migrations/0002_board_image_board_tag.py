# Generated by Django 4.2.7 on 2023-12-05 07:21

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='board',
            name='tag',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, size=None),
        ),
    ]