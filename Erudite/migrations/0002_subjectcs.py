# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-11 07:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Erudite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectCS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subs', models.CharField(max_length=30)),
                ('semeCS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Erudite.SemesterCS')),
            ],
        ),
    ]