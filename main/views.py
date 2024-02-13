from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from main.forms import CustomUserCreationForm
from .forms import CVForm, TechnologyForm
import re
import PyPDF2
from .models import CV


def index(request):
    return render(request, 'cv_jd_scanner/index1.html', {'title': ''})


def indexdb(request):
    cv_data = CV.objects.all()

    # Get the CV instance with the specified cv_id
    selected_cv = None
    cv_id = request.GET.get('cv_id')  # Assuming cv_id is passed as a query parameter

    if cv_id:
        try:
            selected_cv = CV.objects.get(id=cv_id)
        except CV.DoesNotExist:
            selected_cv = None

    return render(request, 'cv_jd_scanner/indexdb.html', {'cv_data': cv_data, 'selected_cv': selected_cv})


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('indexdb')
    else:
        form = CustomUserCreationForm()
    return render(request, 'cv_jd_scanner/register_view.html', {'form': form, 'title': 'Register Page'})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('indexdb')
    else:
        form = AuthenticationForm()
    return render(request, 'cv_jd_scanner/login_user.html', {'form': form, 'title': 'Login Page'})


def add_technology(request):
    if request.method == 'POST':
        form = TechnologyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indexdb')  # Redirect to the main view after successful form submission
    else:
        form = TechnologyForm()

    return render(request, 'cv_jd_scanner/add_technology.html', {'form': form})


def add_cv(request):
    return render(request, 'cv_jd_scanner/add_cv.html')
