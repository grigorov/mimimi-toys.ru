# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_auto_20150214_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='gallery')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='gallery',
            name='pictures',
            field=models.ManyToManyField(to='landing.Picture'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='toys',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, to='landing.Gallery'),
            preserve_default=True,
        ),
    ]
