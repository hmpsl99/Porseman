"""
ASGI config for Porsesh project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Porsesh.settings')

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())