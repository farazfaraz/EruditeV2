# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-11 08:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Erudite', '0002_subjectcs'),
    ]

    operations = [
        migrations.CreateModel(
            name='SemesterECE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.CharField(max_length=30)),
                ('str', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Erudite.Stream')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectECE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subs', models.CharField(max_length=30)),
                ('semeECE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Erudite.SemesterECE')),
            ],
        ),
    ]
