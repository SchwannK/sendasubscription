# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions_dir', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
