## 특징
모노레포와 MSA를 결합

## 기본 환경구성
### Install Python
```shell
❯ brew install pyenv
❯ pyenv global 3.12.3
❯ pyenv local 3.12.3
```

### Install Poetry
```shell
❯ curl -sSL https://install.python-poetry.org | python3 - --uninstall # delete
❯ curl -sSL https://install.python-poetry.org | python3 -
❯ poetry --version
```

## 프로젝트 생성
### Create Django Project
```shell
❯ mkdir django_starter && cd django_starter
❯ git init
# > make gitignore # python
❯ mkdir -p common/auth && mkdir -p services/base
❯ poetry init --no-interaction
❯ poetry shell
❯ poetry add django djangorestframework
```

### Setting dev tools
```shell
❯ mkdir .vscode .docs
❯ touch .vscode/{extensions.json,settings.json} # 작성
❯ touch {.editorconfig,.flake8} # 작성
❯ vi .pre-commit-config.yaml  # 작성
❯ vi pyproject.toml  # 설정 추가
❯ poetry add --group dev pre-commit flake8
❯ poetry run pre-commit install
```

### common > auth
```shell
❯ touch common/auth/{__init__.py,authentication.py,models.py,serializers.py,urls.py,views.py,tests.py,apps.py,admin.py} # 작성
```

### services > base
```shell
❯ cd services/base
❯ django-admin startproject base .
❯ vi manage.py
from pathlib import Path  # add
def main():
  BASE_DIR = Path(__file__).resolve().parent.parent.parent  # add
  sys.path.insert(0, os.path.join(BASE_DIR, 'services/base'))  # add
❯ vi base/settings.py
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
INSTALLED_APPS = [
    'rest_framework',  # add
    'common.auth',  # add
]
# Custom user model 설정
AUTH_USER_MODEL = 'common_auth.CustomUser'  # add
❯ vi base/urls.py
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('common.auth.urls')),
]
```

### Makefile
```shell
❯ cd ../..
❯ vi Makefile  # 작성
❯ make init
❯ make makemigrations-auth
❯ make makemigrations
❯ make migrate
❯ make superuser # admin
```

### services > base > apps > blog
```shell
❯ mkdir -pv apps/blog
❯ python manage.py startapp blog apps/blog
❯ vi apps/blog/apps.py
# name = 'blog'
name = 'services.base.apps.blog'
❯ vi base/settings.py
INSTALLED_APPS = [...'services.base.apps.blog']
❯ poetry run python -m services.base.manage makemigrations blog
Migrations for 'blog':
  services/base/apps/blog/migrations/0001_initial.py
    - Create model Post
❯ poetry run python -m services.base.manage migrate
Operations to perform:
  Apply all migrations: admin, auth, blog, common_auth, contenttypes, sessions
Running migrations:
  Applying blog.0001_initial... OK
```

### Run server
```shell
❯ make runserver
```
http://127.0.0.1:8000/api/auth/users/ 접속


### Add tailwind

https://django-tailwind.readthedocs.io/en/latest/installation.html

Install
```shell
❯ poetry add 'django-tailwind[reload]'
❯ vi services/base/base/settings.py
INSTALLED_APPS = [...'tailwind']
❯ poetry run python -m services.base.manage tailwind init
❯ vi services/base/base/settings.py
ALLOWED_HOSTS = ['127.0.0.1']
INTERNAL_IPS = ['127.0.0.1']
INSTALLED_APPS = [...'theme']
TAILWIND_APP_NAME = 'theme'
if DEBUG:  # type: ignore # noqa: F821
    INSTALLED_APPS.extend(['django_browser_reload'])  # type: ignore # noqa: F821
    MIDDLEWARE.insert(-1, 'django_browser_reload.middleware.BrowserReloadMiddleware')  # type: ignore # noqa: F821
❯ poetry run python -m services.base.manage tailwind install
❯ vi services/base/base/urls.py
 path("__reload__/", include("django_browser_reload.urls")),
```

Use
```html


```

### Add templates
```shell
└── services
    └── base
        ├── base
        │   ├── __init__.py
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── templates
        │   │   ├── base.html
        │   │   ├── home.html
        │   │   └── includes
        │   │       ├── header.html
        │   │       ├── hero.html
        │   │       └── sidebar.html
        │   ├── urls.py
        │   └── wsgi.py
        └── manage.py
vi services/base/base/settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'services/base/templates')],  # add
        ...
        },
    },
]
```




----
## TODO
- [x] blog app 간단 버전으로 추가
- [x] tailwind & 오토 리로드 확인
- [ ] 설정 파일 분리
