# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-28 16:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0006_auto_20160913_1434'),
        ('feature_content_page', '0006_auto_20160915_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenreFeaturePageRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genre_feature_page_relationship', to='genre.GenreClass')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature_page_genre_relationship', to='feature_content_page.FeatureContentPage')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='SubGenreFeaturePageRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature_page_subgenre_relationship', to='feature_content_page.FeatureContentPage')),
                ('subgenre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subgenre_feature_page_relationship', to='genre.SubgenreClass')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
    ]
