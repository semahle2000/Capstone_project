from rest_framework import serializers
from .models import User, Habit, Emotion, MentorshipSession, CommunityPost

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_mentor']

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['id', 'user', 'name', 'date', 'emotion', 'notes']

class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = ['id', 'user', 'date', 'emotion']

class MentorshipSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorshipSession
        fields = ['id', 'mentor', 'student', 'date', 'feedback']

class CommunityPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityPost
        fields = ['id', 'user', 'content', 'created_at']