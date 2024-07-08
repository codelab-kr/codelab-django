## 특징
모노레포와 MSA를 결합

## 기본 환경구성
### Install Python
```shell
❯ brew install pyenv
❯ pyenv global 3.12.3
❯ pyenv local 3.12.3
```

## 프로젝트 생성
### Create Django Project
```shell
❯ mkdir django_starter && cd django_starter
❯ git init
# vs-code 상단 > make gitignore # python
❯ mkdir -p common/auth && mkdir -p services/blog
❯ pip install django djangorestframework
```

### Setting dev tools
```shell
❯ mkdir .vscode .docs
❯ touch .vscode/{extensions.json,settings.json} # 작성
❯ touch {.editorconfig,.flake8} # 작성
❯ vi .pre-commit-config.yaml  # 작성
❯ vi pyproject.toml  # 설정 추가
❯ pip install pre-commit flake8
❯ pre-commit install
```

### common > auth
```shell
❯ touch common/auth/{__init__.py,authentication.py,models.py,serializers.py,urls.py,views.py,tests.py,apps.py,admin.py} # 작성
```

### services > blog
```shell
❯ cd services/blog
❯ django-admin startproject blog .
❯ vi manage.py
from pathlib import Path  # add
def main():
  BASE_DIR = Path(__file__).resolve().parent.parent.parent  # add
  sys.path.insert(0, os.path.join(BASE_DIR, 'services/blog'))  # add
❯ vi blog/settings.py
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
INSTALLED_APPS = [
    'rest_framework',  # add
    'common.auth',  # add
]
# Custom user model 설정
AUTH_USER_MODEL = 'common_auth.CustomUser'  # add
❯ vi blog/urls.py
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

### services > blog > apps > post
```shell
❯ mkdir -pv apps/post
❯ python manage.py startapp post apps/post
❯ vi apps/post/apps.py
# name = 'post'
name = 'services.blog.apps.post'
❯ vi blog/settings.py
INSTALLED_APPS = [...'services.blog.apps.post']
❯ python -m services.blog.manage makemigrations post
Migrations for 'post':
  services/blog/apps/post/migrations/0001_initial.py
    - Create model Post
❯ python -m services.blog.manage migrate
Operations to perform:
  Apply all migrations: admin, auth, post, common_auth, contenttypes, sessions
Running migrations:
  Applying post.0001_initial... OK
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
❯ pip install 'django-tailwind[reload]'
❯ vi services/blog/blog/settings.py
INSTALLED_APPS = [...'tailwind']
❯ python -m services.blog.manage tailwind init
❯ vi services/blog/blog/settings.py
ALLOWED_HOSTS = ['127.0.0.1']
INTERNAL_IPS = ['127.0.0.1']
INSTALLED_APPS = [...'theme']
TAILWIND_APP_NAME = 'theme'
if DEBUG:  # type: ignore # noqa: F821
    INSTALLED_APPS.extend(['django_browser_reload'])  # type: ignore # noqa: F821
    MIDDLEWARE.insert(-1, 'django_browser_reload.middleware.BrowserReloadMiddleware')  # type: ignore # noqa: F821
❯ python -m services.blog.manage tailwind install
❯ vi services/blog/blog/urls.py
 path("__reload__/", include("django_browser_reload.urls")),
```


### Add templates
```shell
└── services
    └── blog
        ├── blog
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
vi services/blog/blog/settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'services/blog/templates')],  # add
        ...
        },
    },
]
```




----
## TODO
- [x] post app 간단 버전으로 추가
- [x] tailwind & 오토 리로드 확인
- [x] 설정 파일 분리


테스트 긴 버전
```shell
❯ python -m services.blog.manage test services.blog.apps.post.tests
/Users/codelab/Documents/works/django_starter
Found 2 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
Destroying test database for alias 'default'...
```



## cf. setup.cfg, setup.py 이용 시
```shell
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# pip install -r requirements.txt

pip install .
❯ python -m services.blog.manage runserver

pre-commit install
pre-commit run --all-files
```



```shell
### services > blog > apps > post
❯ python -m services.blog.manage startapp

```shell
❯ mkdir -pv services/blog/apps/post
❯ python manage.py startapp post apps/post
❯ vi apps/post/apps.py
# name = 'post'
name = 'services.blog.apps.post'
❯ vi blog/settings.py
INSTALLED_APPS = [...'services.blog.apps.post']
❯ python -m services.blog.manage makemigrations post
Migrations for 'post':
  services/blog/apps/post/migrations/0001_initial.py
    - Create model Post
❯ python -m services.blog.manage migrate
Operations to perform:
  Apply all migrations: admin, auth, post, common_auth, contenttypes, sessions
Running migrations:
  Applying post.0001_initial... OK


python -m services.blog.manage shell < scripts/load_data.py
make shell < scripts/load_data.py


make test

pip install dist/django_starter-0.1.0-py2.py3-none-any.whl

pip install ".[dev]"
```



```



## TODO
- [X] poetry 제거 - readme 포함
- https://youtu.be/t-uAgI-AUxc?si=X-kzJXmh2EAmF-YX