# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import time

from django.http import HttpResponse
from django.shortcuts import render

from forms import BusForm
from models import TimeForBus, Bus_Stops, Bus_numbers


# Create your views here.

def BusFormView(request):
    form = BusForm()
    return render(request, 'TableStopApp/template.html', {'form': form})


def TestShow(request):
    if ('numberBus' in request.GET) and ('nameStop' in request.GET):
        message = 'Номер автобуса: %s Название остановки: %s Время: %s NOW: %s' % (
        Bus_numbers.objects.get(id=request.GET['numberBus']).number,
        Bus_Stops.objects.get(id=request.GET['nameStop']).name_stop,
        ActualyTime(request),
        TimeNow())
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)


def ActualyTime(req):
    allTimes = TimeForBus.objects.get(bus_id=req.GET['numberBus'],
                                      stop_id=req.GET['nameStop']).time.split(', ')
    actTimes = []
    for x in allTimes:
        t = datetime.datetime.strptime(x, '%H:%M').time()
        if TimeNow() < str(t):
            actTimes.append(str(x))
    return '%s' % '  '.join(actTimes)


def TimeNow():
    now = time.strftime('%H:%M:%S', time.localtime())
    return now