from django.urls import path
from .views import index, indexdb, register_view, login_user
from . import views

urlpatterns = [
    path('', index, name='home'),
    path('indexdb/', indexdb, name='indexdb'),
    path('register/', register_view, name='register_view'),
    path('login/', login_user, name='login_user'),
    path('add-cv/', views.add_cv, name='add_cv'),
    path('add-technology/', views.add_technology, name='add_technology'),
]