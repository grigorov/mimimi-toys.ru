# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_auto_20150214_1347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='toys',
            options={'verbose_name_plural': 'Игрушки', 'verbose_name': 'Игрушки'},
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='fb_url',
            field=models.URLField(verbose_name='Ссылка в Facebook', default='http://facebook.com', help_text='Ссылка на группу или страницу в Facebook'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='instagram_url',
            field=models.URLField(verbose_name='Ссылка в Instagam', default='http://instagram.com', help_text='ссылка на страницу в Instagram'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='vk_url',
            field=models.URLField(verbose_name='Ссылка в Вконтакте', default='http://vk.com', help_text='ССылка на группу или страницу Вконтакте'),
            preserve_default=True,
        ),
    ]
