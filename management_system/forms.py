from django import forms
from .models import Patients
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Appointment
from .models import Patient
from .models import Sessions


class PatientRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Patients
        fields = ['email', 'password', 'first_name', 'last_name', 'date_of_birth', 'phone_number', 'address', 'city', 'state', 'country', 'postal_code']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Patients.objects.filter(email=email).exists():
            raise forms.ValidationError('Email is already in use.')
        return email

    def save(self, commit=True):
        patient = super(PatientRegistrationForm, self).save(commit=False)
        patient.set_password(self.cleaned_data['password'])
        if commit:
            patient.save()
        return patient


class PatientLoginForm(AuthenticationForm):
    username = forms.CharField(label='Email', widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label='Password', strip=False, widget=forms.PasswordInput)



class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'email', 'birth_date']


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'time', 'date', 'doctor', 'notes']
       


