# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-27 08:28
from __future__ import unicode_literals

from django.db import migrations, models
import pages.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0003_auto_20171227_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='share',
            name='slug',
            field=models.SlugField(blank=True, help_text='\u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, "new-share-for_2018"', max_length=150, null=True, validators=[pages.validators.validate_slug_field], verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0441\u044b\u043b\u043a\u0438 \u043a \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435 \u0430\u043a\u0446\u0438\u0438'),
        ),
    ]