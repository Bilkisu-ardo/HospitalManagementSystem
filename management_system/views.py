from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Doctor, Patient, Patients
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import PatientLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from .forms import PatientRegistrationForm
from .forms import AppointmentForm
from django.shortcuts import get_object_or_404, render,reverse
from .models import Doctor, Appointment
from .forms import PatientProfileForm
from django.views import View
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Sessions
from django.shortcuts import render, redirect
from .models import Patient



def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def admin(request):
    return render(request, 'admin.html')

def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html')

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

def patient_confirm_delete(request):
    return render(request, 'patient_confirm_delete.html')

class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctor_list.html'

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctor_detail.html'

class DoctorCreateView(CreateView):
    model = Doctor
    template_name = 'doctor_form.html'
    fields = ['name', 'email', 'password']
    success_url = reverse_lazy('doctor_list')

class DoctorUpdateView(UpdateView):
    model = Doctor
    template_name = 'doctor_form.html'
    fields = ['name', 'email', 'password']
    success_url = reverse_lazy('doctor_list')

class DoctorDeleteView(DeleteView):
    model = Doctor
    template_name = 'doctor_confirm.html'
    success_url = reverse_lazy('doctor_list')

#PATIENT views.py

class PatientListView(ListView):
    model = Patient
    template_name = 'patient_list.html'

class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patient_detail.html'
    
class PatientCreateView(CreateView):
    model = Patient
    template_name = 'patient_form.html'
    fields = ['name', 'email', 'birth_date']
    success_url = reverse_lazy('patient_list')

class PatientUpdateView(UpdateView):
    model = Patient
    template_name = 'patient_form.html'
    fields = ['name', 'email', 'birth_date']

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patient_confirm_delete.html'
    success_url = reverse_lazy('patient_list')


def patient_registration(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_login')
    else:
        form = PatientRegistrationForm()
    return render(request, 'patient_registration.html', {'form': form})


def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')

class PatientLoginView(LoginView):
    template_name = 'patient_login.html'
    authentication_form = PatientLoginForm
    next_page = reverse_lazy('patient_login')

class PatientLogoutView(LogoutView):
    next_page = reverse_lazy('patient_logout')


from .forms import PatientRegistrationForm
from .models import PatientProfile

def register(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Create a PatientProfile object for the new patient
            patient_profile = PatientProfile.objects.create(user=user, name=user.first_name, email=user.email)
            patient_profile.save()
            return redirect('patient_dashboard')
    else:
        form = PatientRegistrationForm()
    return render(request, 'patient_registration.html', {'form': form})


from django.shortcuts import render, redirect
from .forms import AppointmentForm
from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect

def appointment(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid(): 
            form.save(commit=True) 
            return redirect('book_appointment') 
        else:
            print(form.errors)
    context_dictionary = {'form': form}
    return render(request, 'book_appointment.html', context_dictionary)



def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    return render(request, 'booking_detail.html', {'booking': booking})

def approve_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    booking.approved = True
    booking.save()
    return redirect('booking_list')
def approve_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.approved = True
    booking.save()
    return render(request, 'approve_booking.html', {'booking': booking})

def viewappointmentlist(request):
    appointment= Appointment.objects.all() 
    context= {'appointment':appointment} 
    return render(request, 'ViewAppoinmentList.html', context)

def booking_list(request):
    appointment = Appointment.objects.all()
    context= {'appointment':appointment} 
    return render(request, 'booking_list.html', context)

def update_appoinment(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id) 
    appointment.save()
    return redirect('viewappoinmentlist')

def delete_appointment(request, appointment_id): 
    appointment = Appointment.objects.get(pk=appointment_id)
    appointment.delete()
    return redirect('viewappoinmentlist')

def assign_doctor(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == 'POST':
        doctor_id = request.POST['doctor']
        doctor = get_object_or_404(Doctor, pk=doctor_id)
        booking.doctor_name = doctor.name
        booking.save()
        return redirect('booking_list')
    else:
        doctors = Doctor.objects.all()
        return render(request, 'assign_doctor.html', {'booking': booking, 'doctors': doctors})
    
def assign_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == 'POST':
        doctor_id = request.POST['doctor_id']
        doctor = get_object_or_404(Doctor, pk=doctor_id)
        booking.doctor = doctor
        booking.save()
        return redirect('booking_list')
    else:
        doctors = Doctor.objects.all()
        return render(request, 'assign_booking.html', {'booking': booking, 'doctors': doctors})

def edit_profile(request):
    patient = request.user
    if request.method == 'POST':
        form = PatientProfileForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('edit_profile.html')
    else:
        form = PatientProfileForm(instance=patient)
    
    return render(request, 'edit_profile.html', {'form': form})

    
def doctor_appointments(request, doctor_email):
    appointments = Appointment.objects.filter(doctor=doctor_email)
    doctor_email = 'bilkeesuardo@gmail.com'  # Replace with the actual email value
    url = reverse('doctor_appointments', kwargs={'doctor_email': doctor_email})
    return render(request, 'doctor_appointments.html', {'appointments': appointments})

from django.shortcuts import render


def doctor_appointments(request):
    doctor_name = request.user.username
    appointments = Appointment.objects.filter(doctor_name=doctor_name, approved=True)
    return render(request, 'doctor_appointments.html', {'appointments': appointments})


def session_documentation(request):
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.Patient = request.user
            session.save()
            return redirect('session_documentation')
    else:
        form = SessionForm()
    return render(request, 'session_documentation.html', {'form': form})


from django.shortcuts import render
from .models import Sessions

def patient_sessions(request):
    sessions = Sessions.objects.filter(patient=request.user)
    return render(request, 'patient_sessions.html', {'sessions': sessions})

def patient_sessionss(request):
    sessions = Sessions.objects.filter(patient=request.user)
    return render(request, 'doctor_session.html', {'sessions': sessions})

def patient_sessionsss(request):
    sessions = Sessions.objects.filter(patient=request.user)
    return render(request, 'admin_patient_sessions.html', { 'sessions': sessions})