from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
BASE_DIR = Path(__file__).resolve().parent.parent.parent
print(BASE_DIR)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*!ixa3sx6*+8&v13apjd7*wgcvvo#40xnycs4!k9qm0t_e-$a%'

INTERNAL_IPS = ['127.0.0.1']
ALLOWED_HOSTS = ['']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'common.auth',
    'tailwind',
    'theme',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND':
        'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'services' / 'blog' / 'templates',  # 서비스별 템플릿
            BASE_DIR / 'common' / 'templates'  # 공통 템플릿
        ],
        'APP_DIRS':
        True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
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
    BASE_DIR / 'common/static',  # 공통 정적 파일
    BASE_DIR / 'services' / 'blog' / 'static',  # 서비스별 정적 파일
]
