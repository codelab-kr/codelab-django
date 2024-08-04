## clone from git
```shell
git clone https://github.com/codelab-kr/django-starter
git checkout dev
# copy extra files(.env & db.sqlite3)
```

## start & down with docker
```shell
make up
make down
```

## python settings
```shell
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
make install
```

## apply code changes
```shell
make lint
make collect
ad
cm "커밋 메시지"
ps
```
