from django.urls import path
from . import views
from django.contrib import admin
from main.views import indexdb

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('indexdb/', indexdb, name='indexdb')
]

