from django.db import models
from django.contrib.auth.models import User


class YourModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.TextField()
    field3 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.field1

