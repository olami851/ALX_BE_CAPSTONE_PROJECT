from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings

# Create your models here.

# Users model

class User(AbstractUser):
    
    email = models.EmailField(unique=True, null=True)
    username = models.CharField(max_length=200, unique=True)
    groups = models.ManyToManyField(Group, related_name='event_planner_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='event_planner_user_permissions')
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
