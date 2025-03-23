from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('/Habits', views.create_habit, name="create_habit"),
    path('/mentorship', views.mentorship, name="mentorship"),
    path('/community', views.community, name="community"),
    path('/Emotions', views.log_emotion, name="log_emotion")
]
