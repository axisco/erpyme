# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 21:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenedor', '0003_auto_20171028_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacto',
            name='tipo',
        ),
    ]
