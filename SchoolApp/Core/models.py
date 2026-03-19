from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    role = models.CharField(max_length=20, choices=[
        ('student','Student'),
        ('teacher','Teacher'),
        ('admin','Admin'),
        ])
    
    def __str__(self):
        return f"{self.username} is of user type {self.role}"


