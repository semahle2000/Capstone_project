from django.shortcuts import render

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