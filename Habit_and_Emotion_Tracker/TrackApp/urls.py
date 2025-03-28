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
    path('', views.home, name="home"),
    path('Habits', views.create_habit, name="create_habit"),
    path('mentorship', views.mentorship, name="mentorship"),
    path('community', views.community, name="community"),
    path('Emotions', views.log_emotion, name="log_emotion"),
    path('api/', include(router.urls)),
]
