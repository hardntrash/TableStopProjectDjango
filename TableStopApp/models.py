# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Bus_numbers(models.Model):
    class Meta:
        db_table = 'tableBus'

    number = models.IntegerField(unique=True)
    stop = models.ForeignKey('Bus_Stops')

    def __str__(self):
        return str(self.number)


class Bus_Stops(models.Model):
    class Meta:
        db_table = 'tableStops'

    bus = models.ManyToManyField(Bus_numbers)
    name_stop = models.CharField(max_length=500)

    def __str__(self):
        return self.name_stop

class TimeForBus(models.Model):
    class Meta:
        db_table = 'mergeTime'

    bus = models.ForeignKey(Bus_numbers, related_name='BUS')
    stop = models.ForeignKey(Bus_Stops, related_name='STOP')
    time = models.CharField(max_length=500)

    def __str__(self):
        return str(self.bus) + str(self.stop)