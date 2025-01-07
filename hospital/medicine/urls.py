from django.urls import path
from . import views

urlpatterns = [
    path('request_medicine/', views.request_medicine, name='d'),  # Doctor submits a request
    path('store_request_to_supplier/', views.store_request_to_supplier, name='supplier'),  # Medical store forwards request
]
