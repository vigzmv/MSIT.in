# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-15 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marquee',
            name='title',
            field=models.CharField(help_text='Text to show in the Marquee', max_length=200, verbose_name='Link Title'),
        ),
    ]
