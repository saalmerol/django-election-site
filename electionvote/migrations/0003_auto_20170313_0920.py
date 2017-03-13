# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electionvote', '0002_auto_20170312_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='num_vote_down',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='num_vote_up',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='vote_score',
        ),
        migrations.AddField(
            model_name='candidate',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
