## clone from git
```shell
git clone https://github.com/codelab-kr/django-starter
git checkout dev
# copy extra files(.env & db.sqlite3)
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
ad
cm "커밋 메시지"
ps
```

## start & down with docker
```shell
docker-compose up --build
docker compose -f docker-compose.yaml down  -v --rmi all --remove-orphans
```