# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Например: Mimimi Toys', max_length=255, default='Site Name', verbose_name='Название сайта')),
                ('title', models.CharField(help_text='Заголовок отображается в заголовках страницы браузера', max_length=255, default='Mimimi-toys.ru - Магазин уникальных игрушек', verbose_name='Заголовк страницы')),
                ('slogan', models.CharField(help_text='Слоган который отображется на главной странице под названием сайта.', max_length=255, default='Магазин уникальных игрушек ручной работы', verbose_name='Слоган')),
                ('slider_header', models.CharField(max_length=255, default='<strong>Mimimi Toys -</strong> Игрушки с душой', verbose_name='Заголовк слайдера')),
            ],
            options={
                'verbose_name': 'Конфигурация сайта',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='toys',
            options={'verbose_name': 'Игрушки'},
        ),
    ]
