# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-28 06:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180228_0637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='tag_name',
            new_name='name',
        ),
    ]
