# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20150214_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='name',
            field=models.CharField(verbose_name='Название сайта', default='Mimimi Toys', max_length=255, help_text='Например: Mimimi Toys'),
            preserve_default=True,
        ),
    ]
