"""
WSGI config for django_chat_room project.

It exposes the WSGI callable as a module-level variable named ``application``.
这个WSGI配置文件是部署Django应用到生产环境的关键步骤，它定义了Web服务器如何与您的Django应用进行交互

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_chat_room.settings')

application = get_wsgi_application()
