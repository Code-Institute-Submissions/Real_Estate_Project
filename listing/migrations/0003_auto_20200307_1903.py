# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-07 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_auto_20200301_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='photo1',
            field=models.ImageField(default='img1', upload_to='img'),
        ),
        migrations.AddField(
            model_name='listing',
            name='photo2',
            field=models.ImageField(default='img2', upload_to='img'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photos',
            field=models.ImageField(default='img0', upload_to='img'),
        ),
    ]