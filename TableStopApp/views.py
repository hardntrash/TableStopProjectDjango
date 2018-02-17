# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render
from forms import BusForm


# Create your views here.

def BusFormView(request):
    form = BusForm()
    return render(request, 'TableStopApp/template.html', {'form': form})


def TestShow(request):
    if ('numberBus' in request.GET) and ('nameStop' in request.GET):
        message = 'You searched for: %s %s' % (request.GET['numberBus'], request.GET['nameStop'])
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
