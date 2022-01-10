"""
WSGI config for frank django shop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys
import site
from whitenoise import WhiteNoise

from django.core.wsgi import get_wsgi_application
sys.path.append('C:/Users/USER/frank django shop')
sys.path.append('C:/Users/USER/frank django shop/store')

os.environ['DJANGO_SETTINGS_MODULE'] = 'f-django.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'f-django.settings')

application = get_wsgi_application()




   

