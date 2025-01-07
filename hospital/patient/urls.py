from django.urls import path
from .import views
urlpatterns = [
    path('Patient/',views.Patient,name="patient"),
    path('appointment/',views.appointment,name="appointment")
]
