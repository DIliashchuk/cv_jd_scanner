from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        pass

    def create_superuser(self, email, name, password=None, **extra_fields):
        pass