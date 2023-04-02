from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

# Create your views here.

def index(request):
    return render(request,'users/base.html') 

def registerform(request):
    form = UserForm()
    # print(form)
    return render(request,'users/register.html',{'form':form})

