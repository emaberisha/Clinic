from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.timezone import make_naive

from appointments.forms import AppointmentRegistrationForm
from appointments.models import Appointment


# Create your views here.

def is_appointment_free(user, date_time, request):
    if not user.user_doctors.first():
        context = {'message': 'You don\'t have a doctor'}
        return False, context
    doctors_appointments = Appointment.objects.filter(
        user__user_doctors__doctor=user.user_doctors.first().doctor).distinct()
    for appointment_time in doctors_appointments.values_list('datetime', flat=True):
        if date_time + timedelta(minutes=30) > make_naive(appointment_time) or \
                make_naive(appointment_time) + timedelta(minutes=30) < date_time:
            context = {'message': 'This time is busy'}
            return False, context
        return True, {'message': f'Your appointment has been created.'}


def appointment(request):
    if request.method == 'POST':
        form = AppointmentRegistrationForm(request.POST)
        if form.is_valid():
            user = request.user
            date_time = datetime.combine(form.cleaned_data.get('date'), form.cleaned_data.get('time'))

            free_appointment = is_appointment_free(user, date_time, request)
            if free_appointment[0]:
                Appointment.objects.create(user=user, datetime=date_time)

                messages.success(request, f'Your appointment has been created.')
                return redirect('home')
            else:
                form = AppointmentRegistrationForm()
                context = {'form': form, 'error': free_appointment[1]}
                return render(request, 'appointments/appointment.html', context)
    else:
        form = AppointmentRegistrationForm()

    context = {'form': form}
    return render(request, 'appointments/appointment.html', context)


def delete(request, pk):
    appointment_object = Appointment.objects.get(id=pk)
    appointment_object.delete()
    messages.success(request, f'Your appointment has been cancelled.')
    return redirect('home')


def free_appointments(request):
    data = request
    return render(request, 'appointments/free_appointments.html')


def download_excel(request):
    return None