from django import forms
from .models import Patient,appointment

class patientform(forms.ModelForm):
    class Meta:
        model=Patient
        fields=['name','age','contact','doctor']
class appointmentform(forms.ModelForm):
    class Meta:
        model=appointment
        fields=['patient', 'doctor', 'date', 'symptoms', 'status']
                
