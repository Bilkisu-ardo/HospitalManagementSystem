from django.urls import path
from . import views
from django.urls import include, path
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import patient_registration
from .views import PatientLoginView, PatientLogoutView
from .views import booking_list, booking_detail, approve_booking, assign_booking, session_documentation




urlpatterns = [
    path('admin', views.admin, name='admin'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('base', views.base, name='base'),
    path('', views.index, name='index'),
    path('doctors/', views.DoctorListView.as_view(), name='doctor_list'),
    path('doctors/new/', views.DoctorCreateView.as_view(), name='doctor_create'),
    path('doctors/<int:pk>/', views.DoctorDetailView.as_view(), name='doctor_detail'),
    path('doctors/<int:pk>/update/', views.DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctors/<int:pk>/delete/', views.DoctorDeleteView.as_view(), name='doctor_delete'),
    path('patient_list', views.PatientListView.as_view(), name='patient_list'),
    path('detail/<int:pk>/', views.PatientDetailView.as_view(), name='patient_detail'),
    path('create/', views.PatientCreateView.as_view(), name='patient_create'),
    path('update/<int:pk>/', views.PatientUpdateView.as_view(), name='patient_update'),
    path('delete/<int:pk>/', views.PatientDeleteView.as_view(), name='patient_delete'),
    path('register/', views.patient_registration, name='patient_registration'),
    path('login/', PatientLoginView.as_view(), name='patient_login'),
    path('logout/', PatientLogoutView.as_view(), name='patient_logout'),
    path('dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('dashboardd/', views.doctor_dashboard, name='doctor_dashboard'),
    path('appointment/', views.appointment, name="book_appointment"),
    path('doctor_appointments/', views.doctor_appointments, name='doctor_appointments'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('patient/profile/edit/', views.edit_profile, name='patient_edit_detail'),
    path('bookings/', booking_list, name='booking_list'),
    path('bookings/<int:booking_id>/', booking_detail, name='booking_detail'),
    path('bookings/<int:booking_id>/assign/', assign_booking, name='assign_booking'),  
    path('bookings/<int:booking_id>/approve/', approve_booking, name='approve_booking'),
    path('appointments/<str:doctor_email>/', views.doctor_appointments, name='doctor_appointments'),
    path ('viewappoinmentlist', views.viewappointmentlist, name= 'viewappoinmentlist'),
    path('updateappointment/<appointment_id>', views.update_appoinment, name="updateappointment"),
    path('deleteappointment/<appointment_id>', views.delete_appointment, name="deleteappointment"), 
    path('session/documentation/', session_documentation, name='session_documentation'),
    path('sessions/', views.patient_sessions, name='patient_sessions'),
    path('admin_patient_sessions/', views.patient_sessionsss, name='admin_patient_sessions'),
    path('patient-sessions/', views.patient_sessionss, name='doctor_session'),
     path('patient_confirm_delete/', views.patient_confirm_delete, name='patient_confirm_delete')
]
 



