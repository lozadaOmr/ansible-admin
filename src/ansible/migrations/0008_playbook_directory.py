# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-16 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ansible', '0007_auto_20170516_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='playbook',
            name='directory',
            field=models.CharField(default=b'dir', editable=False, max_length=200),
        ),
    ]