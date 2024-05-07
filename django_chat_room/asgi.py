"""
ASGI config for django_chat_room project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
# 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_chat_room.settings')
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

import chat.routing

application = ProtocolTypeRouter({
    #所有HTTP请求由标准的ASGI应用处理
    "http": django_asgi_app,
    #WebSocket请求首先通过AllowedHostsOriginValidator验证请求来源是否在允许的主机列表中，然后通过AuthMiddlewareStack进行用户认证，并通过URLRouter路由到相应的视图。
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                chat.routing.websocket_urlpatterns
            )
        )
    ),
})
