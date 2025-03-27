"""
ASGI config for yatube_api project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
>>>>>>> 5596f616f928223a336f7372d31359f311bf4a2c
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yatube_api.settings')

application = get_asgi_application()
<<<<<<< HEAD
=======

>>>>>>> 5596f616f928223a336f7372d31359f311bf4a2c
