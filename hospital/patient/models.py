from django.db import models
from doctor.models import Doctor

class Patient(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    contact = models.CharField(max_length=10) 
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name  
class appointment(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date=models.DateTimeField()
    symptoms=models.CharField(max_length=500)
    status=models.CharField(max_length=400,default='pending')

def __str__(self):
    return f"Appointment of {self.patient.name} with {self.doctor.name} on {self.date}"
