# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-19 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180118_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callback',
            name='callback_message',
            field=models.TextField(blank=True, max_length=250, null=True, verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439'),
        ),
    ]
