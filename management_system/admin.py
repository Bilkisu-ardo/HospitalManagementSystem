from django.contrib import admin
from .models import Doctor, Patient, Patients, Appointment, PatientProfile,Sessions

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(PatientProfile)
admin.site.register(Patients)
admin.site.register(Appointment)
admin.site.register(Sessions)
