from django.shortcuts import render, redirect
from django.contrib import messages

from appointments.forms import FreeAppointmentForm
from users.forms import UserRegistrationForm, UpdateDoctorForm
from users.models import UserDoctor


def home(request):
    free_appointment_form = FreeAppointmentForm()
    return render(request, 'users/home.html', {'freeAppointmentForm': free_appointment_form})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            UserDoctor.objects.create(
                user_id=user.id,
                doctor_id=form.cleaned_data['doctors']
            )

            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)


def doctor_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            doctor_form = UpdateDoctorForm(request.POST, instance=request.user)
            if doctor_form.is_valid():
                doctor_form.save()
                messages.success(request, 'Your profile is updated successfully')
                return redirect(to='users/doctorData.html')
        else:
            doctor_form = UpdateDoctorForm(instance=request.user)
        return render(request, 'users/doctorData.html', {'doctorForm': doctor_form})
    return render(request, 'users/doctorData.html')

