from rest_framework import serializers
from .models import CustomUser, WorkoutSession, Location, LocationDistance, DistanceMatrix, FitnessGroup, JoinRequest, Message, Notification, GroupActivity, PrivacySetting, GroupImage
from rest_framework import serializers, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.urls import path
from .models import CustomUser

# Serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'email', 'branch', 'enrollment_number']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            branch=validated_data.get('branch', ''),
            enrollment_number=validated_data.get('enrollment_number', '')
        )
        return user


# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'username', 'branch', 'enrollment_number', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = CustomUser.objects.create_user(**validated_data)
#         return user


class WorkoutSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSession
        fields = ['id', 'user', 'start_time', 'end_time', 'workout_type', 'duration_minutes', 'calories_burned']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'user', 'latitude', 'longitude', 'timestamp']


class LocationDistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationDistance
        fields = ['id', 'start_location', 'end_location', 'distance_km', 'duration_minutes']


class DistanceMatrixSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistanceMatrix
        fields = ['id', 'user', 'locations', 'matrix']


class FitnessGroupSerializer(serializers.ModelSerializer):
    admin = UserSerializer()
    class Meta:
        model = FitnessGroup
        fields = ['id', 'name', 'description', 'location', 'admin', 'created_at']


class JoinRequestSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    group = FitnessGroupSerializer()
    class Meta:
        model = JoinRequest
        fields = ['id', 'user', 'group', 'status', 'requested_at']


class MessageSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    group = FitnessGroupSerializer()
    class Meta:
        model = Message
        fields = ['id', 'user', 'group', 'content', 'created_at']


class NotificationSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Notification
        fields = ['id', 'user', 'message', 'read', 'created_at']


class GroupActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    group = FitnessGroupSerializer()
    class Meta:
        model = GroupActivity
        fields = ['id', 'user', 'group', 'action', 'timestamp']


class PrivacySettingSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = PrivacySetting
        fields = ['id', 'user', 'share_location', 'share_profile_picture', 'share_workout_data']


class GroupImageSerializer(serializers.ModelSerializer):
    group = FitnessGroupSerializer()
    class Meta:
        model = GroupImage
        fields = ['id', 'group', 'image', 'created_at']
