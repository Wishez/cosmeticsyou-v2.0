# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=36, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f')),
                ('first_name', models.CharField(max_length=32, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f')),
                ('middle_name', models.CharField(blank=True, max_length=32, null=True, verbose_name=b'\xd0\x9e\xd1\x82\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe')),
                ('empty_middle_name', models.BooleanField(default=False, verbose_name=b'\xd0\x9d\xd0\xb5\xd1\x82 \xd0\xbe\xd1\x82\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xb0.')),
                ('birthday', models.DateTimeField(verbose_name=b'\xd0\x94\xd0\xb5\xd0\xbd\xd1\x8c \xd1\x80\xd0\xbe\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('citizenship', models.BooleanField(default=False, verbose_name=b'\xd0\x9d\xd0\xb5 \xd0\xb3\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xbd \xd0\xa0\xd0\xa4.')),
                ('passport_data', models.CharField(max_length=26, verbose_name=b'\xd0\xa1\xd0\xb5\xd1\x80\xd0\xb8\xd1\x8f \xd0\xb8 \xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xbf\xd0\xb0\xd1\x81\xd0\xbf\xd0\xbe\xd1\x80\xd1\x82\xd0\xb0')),
                ('phone_number', models.CharField(max_length=26, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd\xd0\xb0')),
                ('city', models.CharField(max_length=50, verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4')),
                ('region', models.CharField(blank=True, max_length=50, null=True, verbose_name=b'\xd0\x9e\xd0\xb1\xd0\xbb\xd0\xb0\xd1\x81\xd1\x82\xd1\x8c')),
                ('street', models.CharField(max_length=50, verbose_name=b'\xd0\xa3\xd0\xbb\xd0\xb8\xd1\x86\xd0\xb0')),
                ('num_home', models.CharField(max_length=5, verbose_name=b'\xd0\x94\xd0\xbe\xd0\xbc')),
                ('num_apartment', models.DecimalField(decimal_places=1, max_digits=999, verbose_name=b'\xd0\x9a\xd0\xb2\xd0\xb0\xd1\x80\xd1\x82\xd0\xb8\xd1\x80\xd0\xb0')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name=b'E-mail')),
                ('consultant_num', models.CharField(blank=True, max_length=40, null=True, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xba\xd0\xbe\xd0\xbd\xd1\x81\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb0\xd0\xbd\xd1\x82\xd0\xb0')),
                ('status', models.CharField(choices=[('\u041d\u043e\u0432\u044b\u0439', b'\xd0\x9d\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb9'), ('\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439', b'\xd0\x97\xd0\xb0\xd1\x80\xd0\xb5\xd0\xb3\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb9'), ('\u041f\u0443\u0441\u0442\u043e\u0439', b'\xd0\x9f\xd1\x83\xd1\x81\xd1\x82\xd0\xbe\xd0\xb9')], default=b'\xd0\x9d\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb9', max_length=18, verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb0\xd1\x82\xd1\x83\xd1\x81 \xd1\x80\xd0\xb5\xd0\xb3\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8')),
                ('registered_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-registered_date'],
                'verbose_name': '\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442',
                'verbose_name_plural': '\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442\u044b',
            },
        ),
    ]
