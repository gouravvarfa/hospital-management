from django.contrib import admin
from .models import MedicalRequest, ExternalRequest

# Custom admin class for MedicalRequest
class MedicalRequestAdmin(admin.ModelAdmin):
    list_display = ('doctor_name', 'medicine_name', 'quantity', 'status', 'date_requested')  # Display these fields in the admin list view
    list_filter = ('status',)  # Add a filter sidebar for the 'status' field
    search_fields = ('doctor_name', 'medicine_name')  # Allow searching by doctor name or medicine name
    ordering = ('-date_requested',)  # Order the list by the date requested (newest first)

# Register the MedicalRequest model with the custom admin class
admin.site.register(MedicalRequest, MedicalRequestAdmin)


# Custom admin class for ExternalRequest
class ExternalRequestAdmin(admin.ModelAdmin):
    list_display = ('medicine_name', 'quantity', 'status', 'date_requested')  # Display these fields in the admin list view
    list_filter = ('status',)  # Add a filter sidebar for the 'status' field
    search_fields = ('medicine_name',)  # Allow searching by medicine name
    ordering = ('-date_requested',)  # Order the list by the date requested (newest first)

# Register the ExternalRequest model with the custom admin class
admin.site.register(ExternalRequest, ExternalRequestAdmin)
