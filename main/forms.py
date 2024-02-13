from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import CV, Technology


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'password1', 'password2']


class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['name', 'surname', 'summary', 'skills', 'contacts', 'pdf_file']


class TechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = ['name', 'description']
