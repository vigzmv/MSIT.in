# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-19 12:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0034_auto_20170201_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.date(2017, 2, 19)),
        ),
    ]
