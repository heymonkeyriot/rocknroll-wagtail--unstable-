# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-22 15:26
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0012_auto_20160922_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='song_details',
            field=wagtail.wagtailcore.fields.StreamField((('Songs', wagtail.wagtailcore.blocks.StructBlock((), icon='fa-music')),), blank=True, verbose_name='Songs'),
        ),
    ]
