from common.settings.applied import *

INSTALLED_APPS += [  # type: ignore # noqa: F821
    'services.shop.apps.catalog',
    'services.shop.apps.orders',
    'services.shop.apps.cart',
]
ROOT_URLCONF = 'services.shop.shop.urls'
WSGI_APPLICATION = 'services.shop.shop.wsgi.application'
TEMPLATES[0]['DIRS'] += BASE_DIR / 'services' / 'shop' / 'templates',  # type: ignore # noqa: F821
TEMPLATES[0]['OPTIONS']['context_processors'] += ['services.shop.apps.cart.context_processors.cart']  # type: ignore
STATICFILES_DIRS += BASE_DIR / 'services' / 'shop' / 'static',  # type: ignore # noqa: F821
CART_SESSION_ID = 'cart'
