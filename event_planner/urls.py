
from django.urls import path
from . import views

app_name = 'event_planner'

urlpatterns = [
    path('', views.index, name='index'),
]

