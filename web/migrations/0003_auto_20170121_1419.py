# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-21 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20170121_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='profile_pic',
            field=models.ImageField(upload_to=b''),
        ),
    ]