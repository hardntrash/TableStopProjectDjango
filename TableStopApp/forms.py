# -*- coding: utf-8 -*-
from django import forms
from TableStopApp.models import BusStop, BusNumber


class BusForm(forms.Form):
    numberBus = forms.ModelChoiceField(queryset=BusNumber.objects.all(), empty_label="Выберите автобус",
                                       widget=forms.Select(attrs={'numberBus': 'dropdown'}), label="Автобус")


class StopForm(forms.Form):
    nameStops = forms.ModelChoiceField(queryset=BusStop.objects.all(), initial='class')

    def __init__(self, my_arg1):
        super(StopForm, self).__init__()
        self.fields['nameStops'].queryset = my_arg1
