from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Habit, Emotion, MentorshipSession, CommunityPost
from .serializers import UserSerializer, HabitSerializer, EmotionSerializer, MentorshipSessionSerializer, CommunityPostSerializer

def home(request):
    return render(request, 'home.html')

def create_habit(request):
    return render(request,'create_habit.html')

def log_emotion(request):
    return render(request, 'log_emotion.html')

def mentorship(request):
    return render(request, 'mentorship.html')

def community(request):
    return render(request, 'community.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

class EmotionViewSet(viewsets.ModelViewSet):
    queryset = Emotion.objects.all()
    serializer_class = EmotionSerializer

class MentorshipSessionViewSet(viewsets.ModelViewSet):
    queryset = MentorshipSession.objects.all()
    serializer_class = MentorshipSessionSerializer

class CommunityPostViewSet(viewsets.ModelViewSet):
    queryset = CommunityPost.objects.all()
    serializer_class = CommunityPostSerializer