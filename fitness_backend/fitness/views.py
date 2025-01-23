from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.permissions import AllowAny
from .models import CustomUser, WorkoutSession, Location, LocationDistance, DistanceMatrix, FitnessGroup, JoinRequest, Message, Notification, GroupActivity, PrivacySetting, GroupImage
from .serializers import UserSerializer, WorkoutSessionSerializer, LocationSerializer, LocationDistanceSerializer, DistanceMatrixSerializer, FitnessGroupSerializer, JoinRequestSerializer, MessageSerializer, NotificationSerializer, GroupActivitySerializer, PrivacySettingSerializer, GroupImageSerializer
from django.views.decorators.csrf import csrf_exempt
# CustomUser ViewSet
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
import logging


class CustomUserViewSet(viewsets.ViewSet):
 @action(detail=False, permission_classes=[AllowAny], methods=['post'], url_path='signup')
 def signup(self, request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()  # Save the user with the serializer's `create` method
        
        return Response({
            "success": True,
            "message": "User created successfully",
            "user": UserSerializer(user).data
        }, status=status.HTTP_201_CREATED)
    return Response({
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, permission_classes=[AllowAny], methods=['post'], url_path='login')
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate user
        user = authenticate(username=username, password=password)
        if user:
            # Login the user (creates a session for them)
            login(request, user)
            return Response({
                "success": True,
                "message": "Login successful",
                "user": UserSerializer(user).data
            }, status=status.HTTP_200_OK)

        # Invalid credentials
        return Response({
            "success": False,
            "error": "Invalid credentials"
        }, status=status.HTTP_401_UNAUTHORIZED)


# WorkoutSession ViewSet
class WorkoutSessionViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer


# Location ViewSet
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


# LocationDistance ViewSet
class LocationDistanceViewSet(viewsets.ModelViewSet):
    queryset = LocationDistance.objects.all()
    serializer_class = LocationDistanceSerializer


# DistanceMatrix ViewSet
class DistanceMatrixViewSet(viewsets.ModelViewSet):
    queryset = DistanceMatrix.objects.all()
    serializer_class = DistanceMatrixSerializer


# FitnessGroup ViewSet
class FitnessGroupViewSet(viewsets.ModelViewSet):
    queryset = FitnessGroup.objects.all()
    serializer_class = FitnessGroupSerializer


# JoinRequest ViewSet
class JoinRequestViewSet(viewsets.ModelViewSet):
    queryset = JoinRequest.objects.all()
    serializer_class = JoinRequestSerializer


# Message ViewSet
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


# Notification ViewSet
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


# GroupActivity ViewSet
class GroupActivityViewSet(viewsets.ModelViewSet):
    queryset = GroupActivity.objects.all()
    serializer_class = GroupActivitySerializer


# PrivacySetting ViewSet
class PrivacySettingViewSet(viewsets.ModelViewSet):
    queryset = PrivacySetting.objects.all()
    serializer_class = PrivacySettingSerializer


# GroupImage ViewSet
class GroupImageViewSet(viewsets.ModelViewSet):
    queryset = GroupImage.objects.all()
    serializer_class = GroupImageSerializer
