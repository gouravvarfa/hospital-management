from django import forms
from .models import Medical
class medicalform(forms.ModelForm):
    class Meta:
        model=Medical
        fields=['name','contact','email','age','address','shop']
