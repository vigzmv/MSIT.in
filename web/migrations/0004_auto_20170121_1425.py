# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-21 14:25
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20170121_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]