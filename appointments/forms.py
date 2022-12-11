from datetime import datetime

from django import forms

from appointments.models import Appointment


class AppointmentRegistrationForm(forms.ModelForm):
    widgets = {
        'date': forms.DateInput(
            format='%d-%m-%Y',
            attrs={'type': 'date', 'class': "form-control",
                   'min': datetime.now().date()}),
        'time': forms.TimeInput(
            attrs={'type': 'time', 'min': '08:00:00', 'max': '16:00:00', 'class': 'form-control'}
        )
    }
    date = forms.DateField(required=True, widget=widgets['date'])
    time = forms.TimeField(required=True, widget=widgets['time'])

    class Meta:
        model = Appointment
        fields = ['date', 'time']


class FreeAppointmentForm(forms.ModelForm):
    widgets = {
        'date': forms.DateInput(
            format='%d-%m-%Y',
            attrs={'type': 'date', 'class': "form-control",
                   'min': datetime.now().date()}),
    }
    date = forms.DateField(required=True, widget=widgets['date'])

    class Meta:
        model = Appointment
        fields = ['date']