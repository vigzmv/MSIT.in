# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-21 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20170121_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='profile_pic',
            field=models.ImageField(upload_to=web.models.image_name),
        ),
    ]