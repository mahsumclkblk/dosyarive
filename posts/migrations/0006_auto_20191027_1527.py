# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-27 13:27
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('posts', '0005_auto_20191020_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='dosya',
            name='doc_tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='dosya',
            name='doc_image_link',
            field=models.CharField(help_text="Görselin yüklübulunduğu esas link. 'örn:resim.jpg | Resmin adresini kopyala'", max_length=1000, verbose_name='Görselin Adresi'),
        ),
    ]