# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-08 19:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TableStopApp', '0004_auto_20180609_0032'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='busnumber',
            options={'verbose_name': '\u041d\u043e\u043c\u0435\u0440 \u0430\u0432\u0442\u043e\u0431\u0443\u0441\u0430', 'verbose_name_plural': '\u041d\u043e\u043c\u0435\u0440\u0430 \u0430\u0432\u0442\u043e\u0431\u0443\u0441\u043e\u0432'},
        ),
        migrations.AlterModelOptions(
            name='busstop',
            options={'verbose_name': '\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438', 'verbose_name_plural': '\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043e\u043a'},
        ),
        migrations.AlterModelOptions(
            name='timeforbus',
            options={'verbose_name': '\u0412\u0440\u0435\u043c\u044f \u043f\u0440\u0438\u0431\u0438\u0442\u0438\u044f', 'verbose_name_plural': '\u0412\u0440\u0435\u043c\u044f \u043f\u0440\u0438\u0431\u0438\u0442\u0438\u044f'},
        ),
    ]