"""
ASGI config for QuizProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from decouple import config

from django.core.asgi import get_asgi_application

from task import router

os.environ.setdefault('DJANGO_SETTINGS_MODULE', config('DJANGO_SETTINGS_MODULE'))


application = ProtocolTypeRouter({
  'http': get_asgi_application(),
  'websocket': URLRouter(
      router.ws_urlpatterns
    ),
})
