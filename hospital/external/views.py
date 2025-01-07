from django.shortcuts import render,redirect

from .forms import externalform

def External(request):
    if request.method=="POST":
        form=externalform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form=externalform()
        return render(request,"external.html",{'form':form})