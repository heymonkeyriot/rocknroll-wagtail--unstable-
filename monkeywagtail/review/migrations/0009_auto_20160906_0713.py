# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-06 06:13
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0008_auto_20160905_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewpage',
            name='song_details',
            field=wagtail.wagtailcore.fields.StreamField((('SongBlock', wagtail.wagtailcore.blocks.StructBlock((('album_song', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='e.g. Waiting Room', required=False)), ('album_song_length', wagtail.wagtailcore.blocks.TimeBlock(blank=True, required=False))), icon='fa-music', template='blocks/songstreamblock.html', title='Song')),), blank=True, verbose_name='Songs'),
        ),
    ]