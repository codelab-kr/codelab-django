from common.settings.applied import *

INSTALLED_APPS += ['services.blog.apps.post']  # type: ignore # noqa: F821
ROOT_URLCONF = 'services.blog.site.urls'
WSGI_APPLICATION = 'services.blog.site.wsgi.application'
