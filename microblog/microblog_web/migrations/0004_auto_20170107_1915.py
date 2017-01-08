# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microblog_web', '0003_auto_20170107_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='coverImage',
            field=models.CharField(default='microblog/img/cover-image.jpg', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='profileImage',
            field=models.CharField(default='microblog/img/profile-image.jpg', max_length=100),
        ),
    ]