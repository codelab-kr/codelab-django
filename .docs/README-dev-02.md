# Shop
[ ] add_service.py 작성하고 shop 만들기 테스트 아래는 참고


### services > shop
```shell
❯ mkdir -pv services/shop
❯ cd services/shop
❯ django-admin startproject shop .

❯ vi manage.py
from pathlib import Path  # add
def main():
  BASE_DIR = Path(__file__).resolve().parent.parent.parent  # add
  sys.path.insert(0, os.path.join(BASE_DIR, 'services/shop'))  # add
❯ vi shop/settings.py
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
INSTALLED_APPS = [
    'rest_framework',  # add
    'common.auth',  # add
]
# Custom user model 설정
AUTH_USER_MODEL = 'common_auth.CustomUser'  # add
❯ vi shop/urls.py
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('common.auth.urls')),
]
```


]