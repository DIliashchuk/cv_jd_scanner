from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from main.forms import CustomUserCreationForm



def index(request):
    return render(request, 'cv_jd_scanner/index1.html', {'title': ''})


def indexdb(request):
    print(request.user)
    return render(request, 'cv_jd_scanner/indexdb.html', {'title': 'IndexDB Page'})


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