from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)



class CV(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    summary = models.TextField()
    skills = models.TextField()
    contacts = models.TextField()
    pdf_file = models.FileField(upload_to='cv_pdfs/')

    def __str__(self):
        return f"{self.name} {self.surname}"


class Technology(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name