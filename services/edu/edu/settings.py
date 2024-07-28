from common.settings.applied import *

INSTALLED_APPS += ['services.edu.apps.courses']  # type: ignore # noqa: F821
ROOT_URLCONF = 'services.edu.edu.urls'
WSGI_APPLICATION = 'services.edu.edu.wsgi.application'
TEMPLATES[0]['DIRS'] += BASE_DIR / 'services' / 'edu' / 'templates',  # type: ignore # noqa: F821
STATICFILES_DIRS += BASE_DIR / 'services' / 'edu' / 'static',  # type: ignore # noqa: F821
