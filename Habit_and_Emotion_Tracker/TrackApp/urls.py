from django.urls import path, include
from . import views
from .views import UserViewSet, HabitViewSet, EmotionViewSet, MentorshipSessionViewSet, CommunityPostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'habits', HabitViewSet)
router.register(r'emotions', EmotionViewSet)
router.register(r'mentorship', MentorshipSessionViewSet)
router.register(r'community', CommunityPostViewSet)

urlpatterns = [
    path('', views.login_view, name='login'),  # Default route to login
    path('home/', views.home, name='home'),    # Home route
    path('Habits', views.create_habit, name='create_habit'),
    path('habit_tracker/', views.habit_tracker, name='habit_tracker'),
    path('mentorship', views.mentorship, name='mentorship'),
    path('start_one_on_one_session/', views.start_one_on_one_session, name='start_one_on_one_session'),
    path('community', views.community, name='community'),
    path('Emotions', views.log_emotion, name='log_emotion'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('api/', include(router.urls)),
]