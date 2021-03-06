# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-18 16:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('ansible', '0012_github_gitlab'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Github',
        ),
        migrations.DeleteModel(
            name='Gitlab',
        ),
        migrations.RemoveField(
            model_name='registry',
            name='playbook',
        ),
        migrations.AlterModelOptions(
            name='playbook',
            options={'verbose_name': 'ansible playbook', 'verbose_name_plural': 'ansible playbooks'},
        ),
        migrations.AlterModelManagers(
            name='playbook',
            managers=[
                ('query_set', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='playbook',
            name='name',
        ),
        migrations.AddField(
            model_name='playbook',
            name='repository',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='playbook',
            name='username',
            field=models.CharField(default=b'', max_length=39),
        ),
        migrations.DeleteModel(
            name='Registry',
        ),
    ]
