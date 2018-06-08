# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-07 05:11
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('TableStopApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='busnumber',
            options={'verbose_name_plural': '\u041d\u043e\u043c\u0435\u0440\u0430 \u0430\u0432\u0442\u043e\u0431\u0443\u0441\u043e\u0432'},
        ),
        migrations.AlterModelOptions(
            name='busstop',
            options={'verbose_name_plural': '\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043e\u043a'},
        ),
        migrations.AlterModelOptions(
            name='timeforbus',
            options={'verbose_name_plural': '\u0412\u0440\u0435\u043c\u044f \u043f\u0440\u0438\u0431\u0438\u0442\u0438\u044f'},
        ),
        migrations.AddField(
            model_name='timeforbus',
            name='stops',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='bus', chained_model_field='bus', default=0, on_delete=django.db.models.deletion.CASCADE, to='TableStopApp.BusStop'),
            preserve_default=False,
        ),
    ]