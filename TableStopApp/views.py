# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from TableStopApp.forms import BusForm, StopForm
from TableStopApp.models import TimeForBus, BusStop, BusNumber

import datetime
import time


numberBus = int()


# Create your views here.

def bus_form_view(request):
    form = BusForm()
    return render(request, 'TableStopApp/select_bus.html', {'form': form})


def stop_form_view(request):
    global numberBus
    numberBus = request.GET['numberBus']
    form = StopForm(TimeForBus.objects.filter(bus_id=request.GET['numberBus']))
    return render(request, 'TableStopApp/select_stop.html', {'form': form})


def show_time_view(request):
    global numberBus

    if actually_time(request, numberBus) != 0:
        message = 'Номер автобуса: %s Название остановки: %s Автобус будет в: %s\n  Время сейчас: %s' % (
            BusNumber.objects.get(id=numberBus).number,
            BusStop.objects.get(id=request.GET['nameStops']).name_stop,
            actually_time(request, numberBus),
            time_now())
    else:
        message = 'Неверные данные'
    return render(request, 'TableStopApp/show_time.html', {'message': message})


def actually_time(req, num):
    if TimeForBus.objects.filter(bus_id=num, stop_id=req.GET['nameStops']).exists():

        allTimes = TimeForBus.objects.get(bus_id=num,
                                          stop_id=req.GET['nameStops']).time.split(', ')
        actTimes = []
        for x in allTimes:
            t = datetime.datetime.strptime(x, '%H:%M').time()
            if time_now() < str(t):
                actTimes.append(str(x))

        if actTimes.__len__() != 0:
            return '%s' % '  '.join(actTimes)
        else:
            return 'Нет автобусов'
    else:
        return 0


def time_now():
    now = time.strftime('%H:%M:%S', time.localtime())
    return now