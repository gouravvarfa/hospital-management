from django import forms
from .models import MedicalRequest, ExternalRequest

# Form for Medical Request (Doctor to Medical Store)
class MedicalRequestForm(forms.ModelForm):
    class Meta:
        model = MedicalRequest
        fields = ['doctor_name', 'medicine_name', 'quantity']

    doctor_name = forms.CharField(max_length=200, label="Doctor Name")
    medicine_name = forms.CharField(max_length=200, label="Medicine Name")
    quantity = forms.IntegerField(label="Quantity")


# Form for External Request (Medical Store to Supplier)
class ExternalRequestForm(forms.ModelForm):
    class Meta:
        model = ExternalRequest
        fields = ['medicine_name', 'quantity']

    medicine_name = forms.CharField(max_length=200, label="Medicine Name")
    quantity = forms.IntegerField(label="Quantity")
