import os.path
from pathlib import Path

from split_settings.tools import include, optional

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENVIRONMENT = os.getenv('DJANGO_ENVIRONMENT', 'development')
SECRET_KEY = os.environ.get('SECRET_KEY', 'None')
DEBUG = False
INTERNAL_IPS = ['127.0.0.1']
ALLOWED_HOSTS = ['']

include(
    'base.py',
    optional(f'{ENVIRONMENT}.py'),
    'debug.py',
)
