from django.urls import path
from .import views
urlpatterns = [
    path('External/',views.External,name="external"),
]
