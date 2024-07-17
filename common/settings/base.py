# Application definition
INSTALLED_APPS = [
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
    'rest_framework',
    'crispy_forms',
    'crispy_tailwind',
    'tailwind',
    'theme',

    # Apps
    'common.auth',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # django-allauth
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
)

# crispy_tailwind 설정
CRISPY_ALLOWED_TEMPLATE_PACKS = 'tailwind'
CRISPY_TEMPLATE_PACK = 'tailwind'

ROOT_URLCONF = 'services.blog.site.urls'

TEMPLATES = [
    {
        'BACKEND':
        'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'services' / 'blog' / 'templates',  # type: ignore # noqa: F821
            BASE_DIR / 'common' / 'templates'  # type: ignore # noqa: F821
        ],
        'APP_DIRS':
        True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'services.blog.site.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # type: ignore # noqa: F821
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 언어 코드와 시간대 설정
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'

# 국제화 설정
USE_I18N = True  # 번역 시스템 활성화
USE_L10N = True  # 현지화 형식 사용
USE_TZ = True  # 시간대 인식(datetime-aware) 객체 사용

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'common_auth.CustomUser'
TAILWIND_APP_NAME = 'theme'

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'common/static',  # type: ignore # noqa: F821
    BASE_DIR / 'services' / 'blog' / 'static',  # type: ignore # noqa: F821
]

# 이메일 설정
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # 콘솔에 이메일 출력 (개발용)
# 실제 이메일 설정 예시 (Gmail)
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your_email@gmail.com'
# EMAIL_HOST_PASSWORD = 'your_password'

# django-allauth 설정
ACCOUNT_ACTIVATION_DAYS = 7  # 며칠 동안 계정 활성화 링크가 유효한지 설정
REGISTRATION_AUTO_LOGIN = True  # 회원가입 후 자동으로 로그인
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_CONFIRMATION_HMAC = True  # (옵션) 보안을 강화하기 위한 설정
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
SOCIALACCOUNT_ENABLED = True
ACCOUNT_UNIQUE_EMAIL = True  # 이메일 고유성을 유지
ACCOUNT_EMAIL_REQUIRED = True  # 이메일 필수

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '622422964261-5fpj5mi4fbl1gmoj16j5cnrqfcpk81ok.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    }
}
