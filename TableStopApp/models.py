# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import _sqlite3
from django.db import models


# Create your models here.
class Bus_numbers(models.Model):
    class Meta:
        db_table = 'tableBus'
    number = models.IntegerField(unique=True)
    def __str__(self):
        return str(self.number)

class Bus_Stops(models.Model):
    class Meta:
        db_table = 'tableStops'
    bus = models.ForeignKey(Bus_numbers)
    name_stop = models.CharField(max_length=500)
    time = models.CharField(max_length=500)
    def __str__(self):
        return self.name_stop