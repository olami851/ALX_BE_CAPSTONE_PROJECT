from rest_framework import serializers
from .models import Event
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.utils import timezone
User = get_user_model()
token = Token.objects.create

# user serializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            username = validated_data['username']
        )
        
        user.set_password(validated_data['password'])
        user.save()
        return user
    
# event serializer

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'descrition', 'date_time', 'location', 'organizer', 'capacity', 'created_date']
        
    def validate_date_time(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Events can not be created with past date.")
        return value
    
    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title must be of five character and above.")
        return value
    def validate_location(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("The location should be of five or more character long.")
        return value
        