# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-02 17:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtaildocs', '0007_merge'),
        ('wagtailcore', '0028_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_external', models.URLField(blank=True, help_text='Set an external link if you want the link to point somewhere outside the CMS.', null=True, verbose_name='External link')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Navigation menu',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('linkfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.LinkFields')),
            ],
            options={
                'verbose_name': 'Menu item',
            },
            bases=('core.linkfields',),
        ),
        migrations.AddField(
            model_name='linkfields',
            name='link_document',
            field=models.ForeignKey(blank=True, help_text='Choose an existing document if you want the link to open a document.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document'),
        ),
        migrations.AddField(
            model_name='linkfields',
            name='link_page',
            field=models.ForeignKey(blank=True, help_text='Choose an existing page if you want the link to point somewhere inside the CMS.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.CreateModel(
            name='MenuMenuItem',
            fields=[
                ('menuitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.MenuItem')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('parent', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='core.Menu')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=('core.menuitem', models.Model),
        ),
    ]
