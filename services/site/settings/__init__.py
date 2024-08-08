import os
from pathlib import Path

from django.urls import reverse_lazy
from split_settings.tools import include, optional

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
SECRET_KEY = os.getenv('SECRET_KEY', 'None')
ENVIRONMENT = os.getenv('DJANGO_ENVIRONMENT', 'development')

include(
    'base.py',
    optional(f'{ENVIRONMENT}.py'),
    'debug.py',
)

INSTALLED_APPS += [   # type: ignore # noqa: F821
    'services.courses',
    'services.students',
    'services.chat',
    'services.cart',
    'services.orders',
    'services.catalog',
    'services.payment',
    'services.post',
]
ROOT_URLCONF = 'services.site.urls'
WSGI_APPLICATION = 'services.site.wsgi.application'
TEMPLATES[0]['DIRS'] += BASE_DIR / 'services' / 'templates',  # type: ignore # noqa: F821
TEMPLATES[0]['OPTIONS']['context_processors'] += ['services.cart.context_processors.cart']  # type: ignore # noqa: F821
STATICFILES_DIRS += BASE_DIR / 'services' / 'static',  # type: ignore # noqa: F821
LOGIN_REDIRECT_URL = reverse_lazy('student_course_list')  # type: ignore # noqa: F821\\\
CART_SESSION_ID = 'cart'
STRIPE_WEBHOOK_SECRET = os.getenv('STRIPE_WEBHOOK_SECRET')
STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
STRIPE_API_VERSION = os.getenv('STRIPE_API_VERSION')
