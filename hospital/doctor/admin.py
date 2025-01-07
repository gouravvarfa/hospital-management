from django.contrib import admin
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialization']  # Use 'name' instead of 'user'

admin.site.register(Doctor,DoctorAdmin)
