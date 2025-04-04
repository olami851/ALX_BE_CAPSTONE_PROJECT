from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework import generics, mixins, viewsets, filters
from .models import Event, User
from .serializers import EventSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def index(request):
    return render(request, 'event_planner/index.html')

# reverse('index')




class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(organizer=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)
        
        
@api_view(['GET'])
def upcoming_events(request):
    events = Event.objects.filter(date_time__gt=timezone.now())
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

filter_backends = [filters.SearchFilter, filters.OrderingFilter]
search_fields = ['title', 'location']
ordering_fields = ['date_time']



    