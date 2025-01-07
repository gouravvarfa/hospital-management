from django import forms
from.models import Doctor
class doctorform(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=['name','specialization']