import os

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # type: ignore # noqa: F821
    }
}

# email 설정 - console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

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
