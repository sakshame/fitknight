from django.urls import path
from .views import (
    CustomUserViewSet, WorkoutSessionViewSet, LocationViewSet,
    LocationDistanceViewSet, DistanceMatrixViewSet, FitnessGroupViewSet,
    JoinRequestViewSet, MessageViewSet, NotificationViewSet,
    GroupActivityViewSet, PrivacySettingViewSet, GroupImageViewSet
)

urlpatterns = [
    # Authentication endpoints
    path('api/users/signup/', CustomUserViewSet.as_view({'post': 'signup'}), name='user-signup'),
    path('api/users/login/', CustomUserViewSet.as_view({'post': 'login'}), name='user-login'),

    # User-related endpoints
    path('api/users/', CustomUserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('api/users/<int:pk>/', CustomUserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-detail'),

    # General endpoints (CRUD pattern)
    path('api/workouts/', WorkoutSessionViewSet.as_view({'get': 'list', 'post': 'create'}), name='workout-list'),
    path('api/workouts/<int:pk>/', WorkoutSessionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='workout-detail'),

    path('api/locations/', LocationViewSet.as_view({'get': 'list', 'post': 'create'}), name='location-list'),
    path('api/locations/<int:pk>/', LocationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='location-detail'),

    path('api/location-distances/', LocationDistanceViewSet.as_view({'get': 'list', 'post': 'create'}), name='location-distance-list'),
    path('api/location-distances/<int:pk>/', LocationDistanceViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='location-distance-detail'),

    path('api/distance-matrices/', DistanceMatrixViewSet.as_view({'get': 'list', 'post': 'create'}), name='distance-matrix-list'),
    path('api/distance-matrices/<int:pk>/', DistanceMatrixViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='distance-matrix-detail'),

    path('api/fitness-groups/', FitnessGroupViewSet.as_view({'get': 'list', 'post': 'create'}), name='fitness-group-list'),
    path('api/fitness-groups/<int:pk>/', FitnessGroupViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='fitness-group-detail'),

    path('api/join-requests/', JoinRequestViewSet.as_view({'get': 'list', 'post': 'create'}), name='join-request-list'),
    path('api/join-requests/<int:pk>/', JoinRequestViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='join-request-detail'),

    path('api/messages/', MessageViewSet.as_view({'get': 'list', 'post': 'create'}), name='message-list'),
    path('api/messages/<int:pk>/', MessageViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='message-detail'),

    path('api/notifications/', NotificationViewSet.as_view({'get': 'list', 'post': 'create'}), name='notification-list'),
    path('api/notifications/<int:pk>/', NotificationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='notification-detail'),

    path('api/group-activities/', GroupActivityViewSet.as_view({'get': 'list', 'post': 'create'}), name='group-activity-list'),
    path('api/group-activities/<int:pk>/', GroupActivityViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='group-activity-detail'),

    path('api/privacy-settings/', PrivacySettingViewSet.as_view({'get': 'list', 'post': 'create'}), name='privacy-setting-list'),
    path('api/privacy-settings/<int:pk>/', PrivacySettingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='privacy-setting-detail'),

    path('api/group-images/', GroupImageViewSet.as_view({'get': 'list', 'post': 'create'}), name='group-image-list'),
    path('api/group-images/<int:pk>/', GroupImageViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='group-image-detail'),
]
