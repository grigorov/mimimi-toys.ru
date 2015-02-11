# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Toys',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(help_text='Необходимо указать имя игрушки, максимальная длина имени 256 символов.', max_length=256, verbose_name='Имя игрушки:')),
                ('avatar', models.ImageField(help_text='Большая картинка игрушки', upload_to='avatars', verbose_name='Основное фото')),
                ('desc_mini', models.TextField(help_text='Краткое описание игрушки, выводиться в ленте игрушек', verbose_name='Описание игрушки кратко')),
                ('desc_full', models.TextField(help_text='Полное описание игрушки, выводиться в подробном описании каждой игрушки', verbose_name='История игрушки')),
                ('price', models.IntegerField(help_text='Необходимо указать стоимость игрушки в рублях', default=1000, verbose_name='Стоимость игрушки')),
                ('avalable', models.BooleanField(help_text='Указать, имеется ли в наличии', default=1, verbose_name='В наличии')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
