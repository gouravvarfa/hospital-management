from django.shortcuts import render,redirect
from .form import doctorform

from patient.models import appointment

def Doctor(request):
    if request.method=="POST":
        form=doctorform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form=doctorform()
        return render(request,"doctor.html",{'form':form})
    
 

def display(request):
    doc=appointment.objects.all()
    return render(request,'doctorlist.html',{'doc':doc}) 