from django.shortcuts import render

def index(request):
    return render(request, 'cv_jd_scanner/index1.html', {'title': ''})

