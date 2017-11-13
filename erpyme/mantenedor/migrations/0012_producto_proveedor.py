# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 18:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mantenedor', '0011_remove_producto_proveedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mantenedor.Proveedor'),
            preserve_default=False,
        ),
    ]
