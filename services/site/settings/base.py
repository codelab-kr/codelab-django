DEBUG = False
INTERNAL_IPS = ['127.0.0.1', 'localhost']  # django-debug-toolbar가 나타나는 IP들
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'app']
CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1', 'http://localhost']

# Application definition
INSTALLED_APPS = [
    'daphne',
    # Django 기본 앱
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # django-allauth 앱
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # Third-party
    'debug_toolbar',
    'rest_framework',
    'rest_framework.authtoken',
    'crispy_forms',
    'crispy_tailwind',
    'tailwind',
    'theme',
    'embed_video',
    'redisboard',

    # Apps
    'services.auth',  # account 폼이 정의된 앱
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # django-debug-toolbar
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',  # 사이트 단위 캐시 (응답 시 캐시)
    'django.middleware.common.CommonMiddleware',  # 설정한 요청 데이터에 접근
    # 'django.middleware.cache.FetchFromCacheMiddleware',  # 사이트 단위 캐시 (요청 시 캐시))
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # django-allauth
]

SITE_ID = 1

ROOT_URLCONF = 'services.auth.urls'
ASGI_APPLICATION = 'services.site.asgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # type: ignore # noqa: F821
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [  # 모든 템플릿에서 전역적으로 사용할 수 있는 함수를 만들어야 할 때 유용
                'django.template.context_processors.debug',  # 요청에서 실행된 SQL 쿼리 목록을 출력하는 콘텍스트의 debug와 sql_queries 변수를 설정함
                'django.template.context_processors.request',  # 콘텍스트의 request 변수를 설정함 # `allauth` needs this from django
                'django.contrib.auth.context_processors.auth',  # 요청의 user 변수를 설정
                'django.contrib.messages.context_processors.messages',  # 콘텍스트에서 메시지 프레임워크를 사용해서 생성된 모든 메시지를 담는 message 변수를 설정
            ],
        },
    },
]

# auth 설정
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'
    },
]

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
)

AUTH_USER_MODEL = 'common_auth.CustomUser'

ACCOUNT_FORMS = {
    'signup': 'services.auth.forms.CustomSignupForm',
}

# django-allauth
REGISTRATION_AUTO_LOGIN = True  # 회원가입 후 자동으로 로그인
ACCOUNT_ACTIVATION_DAYS = 7  # 며칠 동안 계정 활성화 링크가 유효한지 설정
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_CONFIRMATION_HMAC = True  # (옵션) 보안을 강화하기 위한 설정
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_UNIQUE_EMAIL = True  # 이메일 고유성을 유지
ACCOUNT_EMAIL_REQUIRED = True  # 이메일 필수
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
SOCIALACCOUNT_ENABLED = True

# Provider 설정
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '622422964261-5fpj5mi4fbl1gmoj16j5cnrqfcpk81ok.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    }
}

# rest framework 설정
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        # 'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# 언어 코드와 시간대 설정
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 국제화 설정
USE_I18N = True  # 번역 시스템 활성화
USE_L10N = True  # 현지화 형식 사용
USE_TZ = True  # 시간대 인식(datetime-aware) 객체 사용

# static 파일 설정
STATIC_URL = 'static/'
STATICFILES_DIRS = ['']
STATIC_ROOT = BASE_DIR / 'static'  # type: ignore # noqa: F821

# media 파일 설정
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'  # type: ignore # noqa: F821

# crispy_tailwind 설정
TAILWIND_APP_NAME = 'theme'
CRISPY_ALLOWED_TEMPLATE_PACKS = 'tailwind'
CRISPY_TEMPLATE_PACK = 'tailwind'

# database 설정
# DATABASES = {}

# cache 설정
# CACHES = {}
CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 60 * 15  # 15 분
CACHE_MIDDLEWARE_KEY_PREFIXㅌ = 'edu'

# chatting 설정
# CHANNEL_LAYERS = {}

# email 설정
# EMAIL_BACKEND = NotImplemented

# Celery 설정
CELERY_BROKER_URL = 'amqp://guest:guest@rabbitmq:5672//'
CELERY_RESULT_BACKEND = 'rpc://'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
