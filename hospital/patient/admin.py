from django.contrib import admin
from .models import Patient, appointment  # Import the Appointment model

# Patient Admin Configuration
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'contact', 'doctor']  # Removed 'prescription' since it's not defined in Patient

admin.site.register(Patient, PatientAdmin)

# Appointment Admin Configuration
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'date', 'symptoms', 'status']

admin.site.register(appointment, AppointmentAdmin)
