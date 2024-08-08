from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('', include('services.auth.urls')),
    path('', include('services.courses.urls')),
    path('students/', include('services.students.urls')),
    path('chat/', include('services.chat.urls', namespace='chat')),
    path('cart/', include('services.cart.urls', namespace='cart')),
    path('orders/', include('services.orders.urls', namespace='orders')),
    path('catalog/', include('services.catalog.urls', namespace='catalog')),
    path('payment/', include('services.payment.urls', namespace='payment')),
    path('post/', include('services.post.urls', namespace='post')),
    path('api/', include('services.courses.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
