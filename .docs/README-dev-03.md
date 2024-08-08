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

>>> from services.courses.models import Subject
>>> subjects = Subject.objects.all()
>>> cache.set('my_s', subjects)
>>> cache.get('my_s')
<QuerySet [<Subject: Art>, <Subject: Math>, <Subject: Music>, <Subject: Programming>]>
```


```shell
docker run -it --rm --name redis -p 6379:6379 redis
```


```shell
❯ make shell
python -m services.edu.manage shell
>>> from services.courses.api.serializers import SubjectSerializer
>>> subject = Subject.objects.latest('id')
>>> serializer = SubjectSerializer(subject)
>>> serializer.data
{'id': 4, 'title': 'Art', 'slug': 'art'}
```


```shell
❯ curl -i -X POST -u st2:wish0929 http://127.0.0.1:8000/api/course/1/enroll/
HTTP/1.1 200 OK
Date: Tue, 30 Jul 2024 09:13:20 GMT
Server: WSGIServer/0.2 CPython/3.12.3
Content-Type: application/json
Vary: Accept
Allow: POST, OPTIONS
X-Frame-Options: DENY
Content-Length: 17
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin
djdt-store-id: af532da9f749438ea2c5ad247878072f
Server-Timing: TimerPanel_utime;dur=183.71400000000017;desc="User CPU time", TimerPanel_stime;dur=1.7529999999998935;desc="System CPU time", TimerPanel_total;dur=185.46700000000007;desc="Total CPU time", TimerPanel_total_time;dur=189.32916699850466;desc="Elapsed time", SQLPanel_sql_time;dur=1.0979570070048794;desc="SQL 4 queries", CachePanel_total_time;dur=0;desc="Cache 0 Calls"

{"enrolled":true}


❯ curl -X POST http://127.0.0.1:8000/api/auth/ \
     -H "Content-Type: application/json" \
     -d '{"username": "st2", "password": "wish0929"}'
{"token":"98c236c01abfeff249b2af3ebcf1e8be281ae29d"}

curl -X POST http://127.0.0.1:8000/api/course/1/enroll/ \
     -H "Authorization: 98c236c01abfeff249b2af3ebcf1e8be281ae29d";


curl -i -X GET http://127.0.0.1:8000/users/ \
     -H "Authorization: Token 98c236c01abfeff249b2af3ebcf1e8be281ae29d";
HTTP/1.1 200 OK
....

{"count":5,"next":null,"previous":null,"results":[{"id":1,"username":"admin","email":"wishty@gmail.com","phone_number":null},{"id":2,"username":"codelab","email":"master@code-lab.kr","phone_number":null},{"id":18,"username":"wishty","email":"finetips01@gmail.com","phone_number":""},{"id":19,"username":"st1","email":"st1@gmail.com","phone_number":null},{"id":20,"username":"st2","email":"st2@gmail.com","phone_number":null}]}


❯ curl -X POST http://127.0.0.1:8000/api/courses/1/enroll/ \
     -H "Authorization: Token 98c236c01abfeff249b2af3ebcf1e8be281ae29d";
{"enrolled":true}

```