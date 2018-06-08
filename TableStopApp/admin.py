# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import BusStop, BusNumber, TimeForBus

# Register your models here.

admin.site.register(BusStop)
admin.site.register(BusNumber)


@admin.register(TimeForBus)
class TimeForBusAdmin(admin.ModelAdmin):
    list_display = ('stop', 'bus', 'time')
    pass
