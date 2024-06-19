from django.urls import path
from .views import get_events, get_users


urlpatterns = [
    path('events/', get_events),
    path('users/', get_users),
]
