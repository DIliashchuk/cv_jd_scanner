from django.shortcuts import render

def index(request):
    return render(request, 'cv_jd_scanner/index1.html', {'title': ''})

def indexdb(request):
    return render(request, 'cv_jd_scanner/indexdb.html', {'title': 'IndexDB Page'})