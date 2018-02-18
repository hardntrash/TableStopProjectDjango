# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Bus_Stops, Bus_numbers, TimeForBus

# Register your models here.

admin.site.register(Bus_Stops)
admin.site.register(Bus_numbers)
admin.site.register(TimeForBus)