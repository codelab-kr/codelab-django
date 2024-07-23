import os
import subprocess
import sys

# 프로젝트 이름과 디렉토리 설정
service_name = sys.argv[1]
app_name = sys.argv[2]
base_dir = os.path.abspath('./services')
service_directory = os.path.join(base_dir, service_name)
core_directory = os.path.join(service_directory, service_name)
app_directory = os.path.join(service_directory, 'apps', app_name)

# 프로젝트 생성
if not os.path.exists(service_directory):
    os.makedirs(service_directory)
    subprocess.run(['django-admin', 'startproject', service_name, service_directory])

    # 필요한 디렉토리 생성
    os.makedirs(os.path.join(service_directory, 'templates'), exist_ok=True)
    os.makedirs(os.path.join(service_directory, 'static'), exist_ok=True)
    os.makedirs(os.path.join(service_directory, 'apps', app_name), exist_ok=True)
    os.makedirs(os.path.join(service_directory, 'tests'), exist_ok=True)

    # settings.py 파일 경로 설정
    settings_path = os.path.join(service_directory, service_name, 'settings.py')
    asgi_path = os.path.join(service_directory, service_name, 'asgi.py')
    wsgi_path = os.path.join(service_directory, service_name, 'wsgi.py')
    urls_path = os.path.join(service_directory, service_name, 'urls.py')

    # settings.py 파일 수정
    with open(settings_path, 'w') as file:
        lines = f"""from common.settings.applied import *

INSTALLED_APPS += ['services.{service_name}.apps.{app_name}']  # type: ignore # noqa: F821
ROOT_URLCONF = 'services.{service_name}.{service_name}.urls'
WSGI_APPLICATION = 'services.{service_name}.{service_name}.wsgi.application'
"""
        file.write(lines)

    # asgi.py 파일 수정
    with open(asgi_path, 'r') as file:
        asgi = file.read()

    asgi = asgi.replace(
        f"os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{service_name}.settings')",
        f"os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'services.{service_name}.{service_name}.settings')"
    )

    with open(asgi_path, 'w') as file:
        file.write(asgi)

    # wsgi.py 파일 수정
    with open(wsgi_path, 'r') as file:
        wsgi = file.read()

    wsgi = wsgi.replace(
        f"os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{service_name}.settings')",
        f"os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'services.{service_name}.{service_name}.settings')"
    )

    with open(wsgi_path, 'w') as file:
        file.write(wsgi)

    # urls.py 파일 추가
    with open(urls_path, 'w') as file:
        urls = f"""from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('common.auth.urls')),
     path('', include('services.{service_name}.apps.{app_name}.urls', namespace='{service_name}')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
        file.write(urls)

    # manage.py 파일 수정
    manage_path = os.path.join(service_directory, 'manage.py')
    with open(manage_path, 'r') as file:
        manage = file.read()

    manage = manage.replace(
        f"os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{service_name}.settings')",
        f"""BASE_DIR = Path(__file__).resolve().parent.parent.parent
        sys.path.insert(0, str(BASE_DIR / 'services' / '{service_name}'))
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'services.{service_name}.{service_name}.settings')"""
    )

    with open(manage_path, 'w') as file:
        file.write(manage)

# 서비스 디렉토리로 이동
os.chdir(service_directory)

# app 디렉토리가 없으면 생성
if not os.path.exists(app_directory):
    os.makedirs(app_directory)

    # 애플리케이션 생성
    subprocess.run(['python', 'manage.py', 'startapp', app_name, f'apps/{app_name}'])
    apps_path = os.path.join(service_directory, 'apps', app_name, 'apps.py')
    urls_path = os.path.join(service_directory, 'apps', app_name, 'urls.py')

    # apps.py 파일 수정
    with open(apps_path, 'r') as file:
        apps = file.read()

    apps = apps.replace(f"name = '{app_name}'", f"name = 'services.{service_name}.apps.{app_name}'")

    with open(apps_path, 'w') as file:
        file.write(apps)

    # urls.py 파일 수정
    with open(urls_path, 'w') as file:
        urls = f"""from django.urls import path
from . import views

app_name = '{app_name}'

urlpatterns = [
]
"""
        file.write(urls)

    settings_path = os.path.join(service_directory, service_name, 'settings.py')

    # settings.py 파일 수정
    with open(settings_path, 'a') as file:
        lines = f"INSTALLED_APPS += ['services.{service_name}.apps.{app_name}']"
        file.write(lines)

print(f'프로젝트 {service_name} 생성 및 구성 완료: {service_directory, app_directory}')
