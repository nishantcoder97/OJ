# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-12 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coder',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]