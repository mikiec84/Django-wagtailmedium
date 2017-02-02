# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 17:19
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20161124_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='hallo',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='medium',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph_hallo', wagtail.wagtailcore.blocks.RichTextBlock()), ('paragraph_medium', wagtail.wagtailcore.blocks.RichTextBlock(editor='medium'))], blank=True),
        ),
    ]