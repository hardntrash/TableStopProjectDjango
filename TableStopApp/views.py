# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from forms import BusForm


# Create your views here.
def BusForm(request):
    if request.method == 'GET':

        form = BusForm(request.GET)

        if form.is_valid():
            return HttpResponseRedirect('/about/')

    else:
        form = BusForm(request.GET)

    return render(request, 'TableStopApp/template.html', {'form': form})
