from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

# Users model

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=200, unique=True)

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='organizers')
    capacity = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
