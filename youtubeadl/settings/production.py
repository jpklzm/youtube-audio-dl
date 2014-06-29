from base import *


SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['.youtubeadl.com']

MEDIA_ROOT = '/webapps/youtubeadl/media/'

# Celery settings
BROKER_URL = os.environ['BROKER_URL']