from base import *


SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['.youtubeadl.com']

MEDIA_ROOT = '/webapps/youtubeadl/media/'

# Celery settings
BROKER_URL = os.environ['BROKER_URL']

# 3rd-party apps tracking IDs.
GOOGLE_ANALYTICS_TRACKING_ID = 'UA-52335746-1'
ADDTHIS_PUBLISHER_ID = 'ra-52fffdf9456ec7d2'