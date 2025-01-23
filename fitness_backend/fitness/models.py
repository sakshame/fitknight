from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class CustomUser(AbstractUser):
    branch = models.CharField(max_length=100)
    enrollment_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.username


class WorkoutSession(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="workout_sessions")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    workout_type = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    calories_burned = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.workout_type} - {self.start_time.strftime('%Y-%m-%d %H:%M')}"


class Location(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="locations")
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.latitude}, {self.longitude} - {self.timestamp}"


class LocationDistance(models.Model):
    start_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="start_location_distances")
    end_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="end_location_distances")
    distance_km = models.FloatField()
    duration_minutes = models.IntegerField()

    def __str__(self):
        return f"Distance from {self.start_location} to {self.end_location}: {self.distance_km} km"


class DistanceMatrix(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="distance_matrices")
    locations = models.ManyToManyField(Location, related_name="distance_matrices")
    matrix = models.JSONField()  # Storing the distance matrix in a JSON format

    def __str__(self):
        return f"Distance Matrix for {self.user.username} - {len(self.locations.all())} locations"


class FitnessGroup(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    admin = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="admin_groups")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Group: {self.name}, Admin: {self.admin.username}"


class JoinRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="join_requests")
    group = models.ForeignKey(FitnessGroup, on_delete=models.CASCADE, related_name="join_requests")
    status_choices = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='PENDING')
    requested_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Join Request: {self.user.username} to {self.group.name} - {self.status}"


class Message(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="messages")
    group = models.ForeignKey(FitnessGroup, on_delete=models.CASCADE, related_name="messages")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message by {self.user.username} in {self.group.name}: {self.content[:30]}"


class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="notifications")
    message = models.CharField(max_length=255)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message[:30]}"


class GroupActivity(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="group_activities")
    group = models.ForeignKey(FitnessGroup, on_delete=models.CASCADE, related_name="group_activities")
    action_choices = [
        ('JOIN', 'Join'),
        ('MESSAGE', 'Send Message'),
        ('LEAVE', 'Leave'),
        ('UPDATE', 'Update Info'),
    ]
    action = models.CharField(max_length=10, choices=action_choices)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Activity: {self.user.username} performed {self.action} in {self.group.name}"


class PrivacySetting(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="privacy_settings")
    share_location = models.BooleanField(default=True)
    share_profile_picture = models.BooleanField(default=True)
    share_workout_data = models.BooleanField(default=True)

    def __str__(self):
        return f"Privacy settings for {self.user.username}"


class GroupImage(models.Model):
    group = models.ForeignKey(FitnessGroup, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='group_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.group.name}"
