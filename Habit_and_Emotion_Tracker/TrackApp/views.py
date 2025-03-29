from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import User, Habit, Emotion, MentorshipSession, CommunityPost
from .serializers import UserSerializer, HabitSerializer, EmotionSerializer, MentorshipSessionSerializer, CommunityPostSerializer
from .forms import CustomUserCreationForm, CustomAuthenticationForm

@login_required
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def create_habit(request):
    if request.method == 'POST':
        name = request.POST['name']
        date = request.POST['date']
        emotion = request.POST['emotion']
        notes = request.POST.get('notes', '')
        habit = Habit(user=request.user, name=name, date=date, emotion=emotion, notes=notes)
        habit.save()
        return redirect('habit_tracker')
    return render(request, 'create_habit.html')

@login_required
def habit_tracker(request):
    habits = Habit.objects.filter(user=request.user)
    if request.method == 'POST':
        habit_id = request.POST['habit_id']
        habit = Habit.objects.get(id=habit_id)
        habit.accomplished = not habit.accomplished
        habit.save()
    return render(request, 'habit_tracker.html', {'habits': habits})

@login_required
def log_emotion(request):
    return render(request, 'log_emotion.html')

@login_required
def mentorship(request):
    return render(request, 'mentorship.html')

@login_required
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