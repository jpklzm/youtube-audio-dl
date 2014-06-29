from base import *


SECRET_KEY = '79&vz)($@07na+25vw4nb0r^p*6w0j+-x!m)y5p#76tp!gvs_5'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

MEDIA_ROOT = '%s/media/' % PROJECT_ROOT

# Celery settings
BROKER_URL = 'amqp://guest:guest@localhost/'
