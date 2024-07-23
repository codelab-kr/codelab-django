from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('cart/', include('services.shop.apps.cart.urls', namespace='cart')),
    path('orders/', include('services.shop.apps.orders.urls', namespace='orders')),
    path('', include('common.auth.urls')),
    path('', include('services.shop.apps.catalog.urls', namespace='shop')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
