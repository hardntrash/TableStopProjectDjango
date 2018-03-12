# -*- coding: utf-8 -*-
from django import forms
from models import Bus_Stops, Bus_numbers, TimeForBus


class BusForm(forms.ModelForm):
    numberBus = forms.ModelChoiceField(queryset=Bus_numbers.objects.all(), empty_label="Выберите автобус",
                                       widget=forms.Select(attrs={'numberBus': 'dropdown'}), label="Автобус")
    nameStop = forms.ModelChoiceField(queryset=Bus_Stops.objects.all(), empty_label="Выберите остановку",
                                      widget=forms.Select(attrs={'nameStop': 'dropdown'}), label="Остановка")

    class Meta:
        model = Bus_numbers
        fields = ('number',)

#class ShowForm(forms.ModelForm):
#    class Meta:
#        model = TimeForBus
#        fields = ('time',)

#    time = forms