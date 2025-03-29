from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    is_mentor = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # Add this line
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Add this line
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits')
    name = models.CharField(max_length=100)
    date = models.DateField()
    emotion = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    accomplished = models.BooleanField(default=False)

class Emotion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emotions')
    date = models.DateField()
    emotion = models.CharField(max_length=100)

class MentorshipSession(models.Model):
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentorship_as_mentor')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentorship_as_student')
    date = models.DateField()
    feedback = models.TextField(blank=True, null=True)

class CommunityPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='community_posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)