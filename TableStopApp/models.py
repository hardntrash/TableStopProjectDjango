# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Bus_Stops(models.Model):
    number_bus = models.IntegerField()
    stop_1 = models.CharField(max_length=500, blank=True)
    stop_2 = models.CharField(max_length=500, blank=True)
    stop_3 = models.CharField(max_length=500, blank=True)
    stop_4 = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return str(self.number_bus)
