import os
from pathlib import Path

from split_settings.tools import include, optional

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRET_KEY = os.getenv('SECRET_KEY', 'None')
ENVIRONMENT = os.getenv('DJANGO_ENVIRONMENT', 'development')

include(
    'base.py',
    optional(f'{ENVIRONMENT}.py'),
    'debug.py',
)
