# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('class_name', models.CharField(max_length=20)),
                ('stu_num', models.IntegerField()),
                ('class_num', models.IntegerField()),
            ],
            options={
                'db_table': 'classinfo',
            },
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=20)),
                ('stu_gender', models.BooleanField(default=False)),
                ('stu_age', models.IntegerField()),
                ('stu_class', models.ForeignKey(to='stu_manageapp.ClassInfo')),
            ],
            options={
                'db_table': 'studentinfo',
            },
        ),
    ]
