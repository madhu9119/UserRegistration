from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'users/base.html') 

def useraction(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request,"You have been successfully Registered")
            form = UserForm()
            return render(request,'users/register.html',{'form':form}) 
        else:
            print("Invalid form")
    else:

        form=UserForm()
    return render(request,"users/register.html",{'form':form})

def userlogincheck(request):
    return render(request,"users/signin.html")

