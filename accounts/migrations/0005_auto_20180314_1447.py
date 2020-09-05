# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-14 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_relatedconsultant_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refferalconsultant',
            name='num_apartment',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=999, null=True, verbose_name='\u041a\u0432\u0430\u0440\u0442\u0438\u0440\u0430'),
        ),
        migrations.AlterField(
            model_name='refferalconsultant',
            name='num_home',
            field=models.CharField(blank=True, default=b'', max_length=5, null=True, verbose_name='\u0414\u043e\u043c'),
        ),
        migrations.AlterField(
            model_name='refferalconsultant',
            name='passport_data',
            field=models.CharField(blank=True, default=b'', max_length=26, null=True, verbose_name='\u0421\u0435\u0440\u0438\u044f \u0438 \u043d\u043e\u043c\u0435\u0440 \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='refferalconsultant',
            name='region',
            field=models.CharField(blank=True, default=b'', max_length=50, null=True, verbose_name='\u041f\u043e\u0447\u0442\u043e\u0432\u044b\u0439 \u0418\u043d\u0434\u0435\u043a\u0441'),
        ),
        migrations.AlterField(
            model_name='refferalconsultant',
            name='street',
            field=models.CharField(blank=True, default=b'', max_length=50, null=True, verbose_name='\u0423\u043b\u0438\u0446\u0430'),
        ),
        migrations.AlterField(
            model_name='refferalconsultanttablerelations',
            name='num_apartment',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=999, null=True, verbose_name='\u041a\u0432\u0430\u0440\u0442\u0438\u0440\u0430'),
        ),
        migrations.AlterField(
            model_name='refferalconsultanttablerelations',
            name='num_home',
            field=models.CharField(blank=True, default=b'', max_length=5, null=True, verbose_name='\u0414\u043e\u043c'),
        ),
        migrations.AlterField(
            model_name='refferalconsultanttablerelations',
            name='passport_data',
            field=models.CharField(blank=True, default=b'', max_length=26, null=True, verbose_name='\u0421\u0435\u0440\u0438\u044f \u0438 \u043d\u043e\u043c\u0435\u0440 \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='refferalconsultanttablerelations',
            name='region',
            field=models.CharField(blank=True, default=b'', max_length=50, null=True, verbose_name='\u041f\u043e\u0447\u0442\u043e\u0432\u044b\u0439 \u0418\u043d\u0434\u0435\u043a\u0441'),
        ),
        migrations.AlterField(
            model_name='refferalconsultanttablerelations',
            name='street',
            field=models.CharField(blank=True, default=b'', max_length=50, null=True, verbose_name='\u0423\u043b\u0438\u0446\u0430'),
        ),
        migrations.AlterField(
            model_name='user',
            name='num_apartment',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=999, null=True, verbose_name='\u041a\u0432\u0430\u0440\u0442\u0438\u0440\u0430'),
        ),
        migrations.AlterField(
            model_name='user',
            name='num_home',
            field=models.CharField(blank=True, default=b'', max_length=5, null=True, verbose_name='\u0414\u043e\u043c'),
        ),
        migrations.AlterField(
            model_name='user',
            name='passport_data',
            field=models.CharField(blank=True, default=b'', max_length=26, null=True, verbose_name='\u0421\u0435\u0440\u0438\u044f \u0438 \u043d\u043e\u043c\u0435\u0440 \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='user',
            name='region',
            field=models.CharField(blank=True, default=b'', max_length=50, null=True, verbose_name='\u041f\u043e\u0447\u0442\u043e\u0432\u044b\u0439 \u0418\u043d\u0434\u0435\u043a\u0441'),
        ),
        migrations.AlterField(
            model_name='user',
            name='street',
            field=models.CharField(blank=True, default=b'', max_length=50, null=True, verbose_name='\u0423\u043b\u0438\u0446\u0430'),
        ),
    ]
