# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-15 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Erudite', '0004_auto_20160911_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectcs',
            name='link',
            field=models.CharField(max_length=100),
        ),
    ]
