

# Create your views here.
from django.shortcuts import render,redirect
from .forms import patientform,appointmentform

def Patient(request):
    if request.method=="POST":
        form=patientform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=patientform()
        return render(request,"patient.html",{'form':form})
    
def appointment(request):
    if request.method=="POST":
        form=appointmentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form=appointmentform()
        return render(request,"patient.html",{'form':form})
