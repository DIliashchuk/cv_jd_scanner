from django.urls import path
from . import views
from django.contrib import admin
from main.views import indexdb
from .views import index, indexdb, register_user
from .views import register_view

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('indexdb/', indexdb, name='indexdb'),
    path('register/user/', register_user, name='register_user'),
    path('register/view/', register_view, name='register_view'),
]

