from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def index(request):
    return render(request, 'cv_jd_scanner/index1.html', {'title': ''})


def indexdb(request):
    return render(request, 'cv_jd_scanner/indexdb.html', {'title': 'IndexDB Page'})


def register_view(request):
    return render(request, 'cv_jd_scanner/register_view.html', {'title': 'Register Page'})


def register_user(request):
    # Your existing register_user logic here
    return render(request, 'cv_jd_scanner/register_user.html', {'title': 'Register Page'})
