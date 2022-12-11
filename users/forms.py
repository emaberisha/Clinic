from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import User, Doctor


def get_doctors():
    doctors_json = []
    doctors = Doctor.objects.all()
    for doctor in doctors:
        doctors_json.append((doctor.id, str(doctor)))
    return doctors_json


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    doctors = forms.ChoiceField(choices=get_doctors(), required=True)
    email = forms.EmailField()

    # def __init__(self, *args, **kwargs):
    #     super(UserRegistrationForm, self).__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'doctors']


class UserAuthenticationForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(UserAuthenticationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class UpdateDoctorForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
