import os

ADMINS = [
    ('admin', 'master@code-lab.kr'),
]
ALLOWED_HOSTS += ['code-lab.kr']  # type: ignore # noqa: F821
CSRF_TRUSTED_ORIGINS += ['http://code-lab.kr', 'https://code-lab.kr']  # type: ignore # noqa: F821
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.getenv('DB_HOST'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'PORT': 5432,
        'ATOMIC_REQUESTS': True,
        'CONN_MAX_AGE': 600,  # 10 minutes
    }
}

# email 설정 - Gmail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

# cache 설정 - Redis
REDIS_HOST = os.getenv('REDIS_HOST', '127.0.0.1')
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': f'redis://{REDIS_HOST}:6379',
    }
}

# chatting 설정 - Redis
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [(REDIS_HOST, 6379)],
        },
    },
}
