from django.urls import path, include
from .views import index, indexdb, register_view, login_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='home'),
    path('indexdb/', indexdb, name='indexdb'),
    path('register/', register_view, name='register_view'),
    path('login/', login_user, name='login_user'),
    path('logout/', LogoutView.as_view(), name='logout'),
]