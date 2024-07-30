# 이러닝 시스템
```shell
python scripts/add_service_app.py edu courses

python -m services.edu.manage dumpdata courses --indent=2 --output=services/edu/apps/courses/fixtures/subjects.json
python -m services.edu.manage loaddata services/edu/apps/courses/fixtures/subjects.json
```


```shell
python scripts/add_service_app.py edu students
```

```shell
docker pull memcached
docker run -it --rm --name memcached -p 11211:11211 memcached -m 64

❯ make shell
python -m services.edu.manage shell
Python 3.12.3 (main, Jul  8 2024, 16:28:24) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.core.cache import cache
>>> cache.set('musician', 'DDFWFE', 20)
>>> cache.get('musician')
'DDFWFE'

>>> from services.edu.apps.courses.models import Subject
>>> subjects = Subject.objects.all()
>>> cache.set('my_s', subjects)
>>> cache.get('my_s')
<QuerySet [<Subject: Art>, <Subject: Math>, <Subject: Music>, <Subject: Programming>]>
```


```shell
docker run -it --rm --name redis -p 6379:6379 redis
```