from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .froms import MedicalRequestForm, ExternalRequestForm
from .models import MedicalRequest, ExternalRequest

# View for doctors to request medicine from the medical store
def request_medicine(request):
    if request.method == 'POST':
        form = MedicalRequestForm(request.POST)
        if form.is_valid():
            form.save()  # Save the request to the database
            return HttpResponse("Medicine request submitted successfully!")
    else:
        form = MedicalRequestForm()

    return render(request, 'doctorrequest.html', {'form': form})

# View for medical store to request from the supplier
def store_request_to_supplier(request):
    if request.method == 'POST':
        # Get the selected medical request from the form (no need for request_id in URL)
        medical_request_id = request.POST.get('medical_request')
        medical_request = MedicalRequest.objects.get(id=medical_request_id)

        # Handle the external request creation
        form = ExternalRequestForm(request.POST)
        if form.is_valid():
            # Create an external request to the supplier
            external_request = form.save(commit=False)
            external_request.medicine_name = medical_request.medicine_name
            external_request.quantity = medical_request.quantity
            external_request.status = 'Pending'  # Set the initial status as 'Pending'
            external_request.save()

            # Update the status of the medical request
            medical_request.status = 'Forwarded to Supplier'
            medical_request.save()

            return HttpResponse(f"External request for {external_request.quantity} {external_request.medicine_name} has been created and forwarded to the supplier.")
    else:
        # For GET requests, display the available medical requests
        medical_requests = MedicalRequest.objects.filter(status="Pending")  # Filter based on your logic
        form = ExternalRequestForm()

    return render(request, 'supplier.html', {'form': form, 'medical_requests': medical_requests})