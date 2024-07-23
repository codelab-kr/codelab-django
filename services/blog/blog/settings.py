from common.settings.applied import *

INSTALLED_APPS += ['services.blog.apps.post']  # type: ignore # noqa: F821
ROOT_URLCONF = 'services.blog.blog.urls'
WSGI_APPLICATION = 'services.blog.blog.wsgi.application'
TEMPLATES[0]['DIRS'] += BASE_DIR / 'services' / 'blog' / 'templates',  # type: ignore # noqa: F821
STATICFILES_DIRS += BASE_DIR / 'services' / 'blog' / 'static',  # type: ignore # noqa: F821
