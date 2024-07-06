import os

# 환경 변수 또는 기본값을 사용하여 환경 설정 파일을 동적으로 로드
ENVIRONMENT = os.getenv('DJANGO_ENVIRONMENT', 'development')

if ENVIRONMENT == 'production':
    from common.settings.production import *
else:
    from common.settings.development import *

INSTALLED_APPS += [  # type: ignore
    'services.blog.apps.post',
]

ROOT_URLCONF = 'services.blog.blog.urls'

WSGI_APPLICATION = 'services.blog.blog.wsgi.application'
