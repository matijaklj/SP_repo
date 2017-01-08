# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 09:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microblog_web', '0005_hashtag_post_hashtag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtag',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]