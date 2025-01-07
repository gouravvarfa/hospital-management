from django import forms
from external.models import External
class externalform(forms.ModelForm):
    class Meta:
        model=External
        fields=['name','contact','email','age','address','shop']
