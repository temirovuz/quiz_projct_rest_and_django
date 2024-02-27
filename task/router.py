from django.urls import path

from .status_check import StatusCheckConsumer

ws_urlpatterns = [
    path('ws/tasks', StatusCheckConsumer.as_asgi())
]