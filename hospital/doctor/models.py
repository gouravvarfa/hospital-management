from django.db import models

class Doctor(models.Model):
        name=models.CharField(max_length=300)
        specialization=models.CharField(max_length=400)
        def __str__(self):
           return self.name