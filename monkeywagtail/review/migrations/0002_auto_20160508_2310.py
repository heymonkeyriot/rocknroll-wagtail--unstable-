# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-08 22:10
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewpage',
            name='rating',
            field=models.IntegerField(help_text='Your rating needs to be between 0 - 5', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Album rating'),
        ),
    ]
