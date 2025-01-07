from django.shortcuts import render,redirect
from .forms import medicalform


# View to handle the doctor form (creating new medical records)
def worker(request):
    if request.method == "POST":
        form = medicalform(request.POST)
        if form.is_valid():
            form.save()  # Save the new medical record
            return redirect("home")
    else:
        form = medicalform()  # Create an empty form for GET requests
    
    return render(request, "medical.html", {'form': form})  # Pass the form to the template

# View to handle displaying all medical requests

