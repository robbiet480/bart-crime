# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0011_incident_published_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
