from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

def index(request):
    return render(request, 'cv_jd_scanner/index1.html', {'title': ''})

def indexdb(request):
    return render(request, 'cv_jd_scanner/indexdb.html', {'title': 'IndexDB Page'})

def register_user(request):
    return render(request, 'cv_jd_scanner/register.html', {'title': 'Register Page'})