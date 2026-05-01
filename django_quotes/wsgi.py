"""
WSGI config for django_quotes project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_quotes.settings')

application = get_wsgi_application()

app = application
