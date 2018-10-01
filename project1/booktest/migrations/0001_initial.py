# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('btitle', models.CharField(max_length=20)),
                ('bpub_date', models.DateField()),
                ('bread', models.IntegerField(default=0)),
                ('bcomment', models.IntegerField(default=0)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('hanme', models.CharField(max_length=20)),
                ('hgender', models.BooleanField(default=False)),
                ('hcomment', models.CharField(max_length=200)),
                ('isDelete', models.BooleanField(default=False)),
                ('hbook', models.ForeignKey(to='booktest.BookInfo')),
            ],
        ),
    ]
