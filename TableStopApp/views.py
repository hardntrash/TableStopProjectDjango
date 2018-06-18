# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

from TableStopApp.forms import BusForm, StopForm
from TableStopApp.models import TimeForBus, BusStop, BusNumber

import datetime
import time


numberBus = int()


# Create your views here.

def bus_form_view(request):
    form = BusForm()
    return render(request, 'TableStopApp/select_bus.html', {'form': form, 'time_now': time_now()})


def stop_form_view(request):
    global numberBus
    try:
        numberBus = request.GET['numberBus']
    except MultiValueDictKeyError:
        numberBus = numberBus
    form = StopForm(TimeForBus.objects.filter(bus_id=request.GET['numberBus']))
    return render(request, 'TableStopApp/select_stop.html', {'form': form, 'time_now': time_now()})


def show_time_view(request):
    global numberBus

    if actually_time(request, numberBus) != 0:
        # message = 'Номер автобуса: %s Название остановки: %s Автобус будет в: %s\n  Время сейчас: %s' % (
        #     BusNumber.objects.get(id=numberBus).number,
        #     BusStop.objects.get(id=request.GET['nameStops']).name_stop,
        #     actually_time(request, numberBus),
        #     time_now())
        res_num_bus = BusNumber.objects.get(id=numberBus).number
        res_name_stop =  BusStop.objects.get(id = TimeForBus.objects.get(bus_id=numberBus, id=request.GET['nameStops']).stop_id).name_stop
        res_actually_time = actually_time(request, numberBus)
        res_time_now = time_now()
    else:
        res_num_bus = ''
        res_name_stop = ''
        res_actually_time = 'Неверные данные'
        res_time_now = time_now()
    return render(request, 'TableStopApp/show_time.html', {'res_num_bus': res_num_bus,
                                                           'res_name_stop':res_name_stop,
                                                           'res_actually_time': res_actually_time,
                                                           'res_time_now': res_time_now})


def actually_time(req, num):
    if TimeForBus.objects.filter(bus_id=num, id=req.GET['nameStops']).exists():

        allTimes = TimeForBus.objects.get(bus_id=num,
                                          id=req.GET['nameStops']).time.split(', ')
        actTimes = []
        for x in allTimes:
            t = datetime.datetime.strptime(x, '%H:%M').time()
            if time_now() < str(t):
                actTimes.append(str(x))

        if actTimes.__len__() != 0:
            return '%s' % '  '.join(actTimes)
        else:
            return 'сегодня атобусов больше нет'
    else:
        return 0


def time_now():
    now = time.strftime('%H:%M:%S', time.localtime())
    return now