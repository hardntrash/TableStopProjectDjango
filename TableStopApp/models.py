# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class BusNumber(models.Model):
    class Meta:
        db_table = u'Номера автобусов'
        verbose_name = u'Номер автобуса'
        verbose_name_plural = u'Номера автобусов'

    number = models.IntegerField("Номер автобуса", unique=True)

    def __str__(self):
        return str(self.number)


class BusStop(models.Model):
    class Meta:
        db_table = u'Названия остановок'
        verbose_name = u'Название остановки'
        verbose_name_plural = u'Названия остановок'

    name_stop = models.CharField("Название остановки", max_length=500, unique=True)

    def __str__(self):
        return (self.name_stop).encode('utf8')


class TimeForBus(models.Model):
    class Meta:
        db_table = u'Время прибытия'
        verbose_name = u'Время прибытия'
        verbose_name_plural = u'Время прибытия'

    bus = models.ForeignKey(BusNumber, related_name='BUS', verbose_name='Номер автобуса')
    stop = models.ForeignKey(BusStop, related_name='STOP', verbose_name='Название остановки')
    time = models.CharField("Время", max_length=500)

    def __str__(self):
        return str(self.stop)
