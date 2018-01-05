# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Bus_Stops
from django.views import generic

# Create your views here.

class Table_Stops(generic.ListView):
    template_name = 'TableStopApp/stops.html'
    context_object_name = "test_bus_stops_list"
    def get_queryset(self):
        return Bus_Stops.objects.all()