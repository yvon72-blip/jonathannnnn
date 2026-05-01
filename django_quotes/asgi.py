"""
ASGI config for django_quotes project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_quotes.settings')

application = get_asgi_application()
