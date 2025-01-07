from django.urls import path
from . import views

urlpatterns = [
    path('doctor/', views.Doctor, name="doctor"),  # URL pattern for Doctor view
 
        path('display/', views.display, name="display")# URL pattern for RequestDoctor view
]
