# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-11-19 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_readmail'),
    ]

    operations = [
        migrations.AddField(
            model_name='readmail',
            name='code',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]