from django.db import models

class External(models.Model):
    name=models.CharField(max_length=200)
    contact=models.CharField(max_length=10)
    age=models.PositiveIntegerField()
    email=models.CharField(max_length=30)
    shop=models.CharField(max_length=10)
    address=models.CharField(max_length=60)

def __str__(self):
    return self.name