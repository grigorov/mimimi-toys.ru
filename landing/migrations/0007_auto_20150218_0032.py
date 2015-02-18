# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0006_auto_20150215_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите имя', max_length=255, verbose_name='Имя')),
                ('email', models.EmailField(help_text='Укажите Email', max_length=75, verbose_name='Ваш Email')),
                ('mob', phonenumber_field.modelfields.PhoneNumberField(help_text='укажите номер телефона для связи', max_length=128, verbose_name='Ваш номе телефона')),
                ('text', models.CharField(help_text='Укажите комментарий к заказу', max_length=255, verbose_name='Комментарий к заказу')),
            ],
            options={
                'verbose_name_plural': 'Заказы',
                'verbose_name': 'Заказ',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name_plural': 'Галлереи', 'verbose_name': 'Галлерея'},
        ),
        migrations.AlterModelOptions(
            name='picture',
            options={'verbose_name_plural': 'Изображения для галлереи', 'verbose_name': 'Изображение для галлереи'},
        ),
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(help_text='укажите изображение', upload_to='gallery', verbose_name='Изображение'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='picture',
            name='title',
            field=models.CharField(help_text='укажите имя картинки', max_length=50, verbose_name='Имя картинки'),
            preserve_default=True,
        ),
    ]
