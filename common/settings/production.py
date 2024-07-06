from .base import *

DEBUG = False

ALLOWED_HOSTS += ['your-production-domain.com']

# 프로덕션 환경에서의 추가 설정 (예: 보안, 실제 데이터베이스 등)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'your_db_host',
        'PORT': 'your_db_port',
    }
}
