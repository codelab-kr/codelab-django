from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('common.auth.urls', namespace='account')),
    path('', include('allauth.urls')),  # 소셜 & 로그인 관련 URL
    path('', include('services.blog.apps.post.urls')),
    path('', include('registration.backends.default.urls')),  # django-registrationURL 추가
    # path('api/', include('rest_framework.urls')),  # django-registration URL 추가
    # path('api/auth/', include('dj_rest_auth.urls')),  # 98사용자 인증 관련 API
    # path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  # 사용자 회원가입 관련 API
]

if settings.DEBUG:
    urlpatterns += [path('__reload__/', include('django_browser_reload.urls'))]
