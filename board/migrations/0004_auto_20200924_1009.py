# Generated by Django 3.0.2 on 2020-09-24 08:09

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20200923_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), blank=True, null=True, size=3),
        ),
    ]
