# 이러닝 시스템
```shell
python scripts/add_service_app.py edu courses

python -m services.edu.manage dumpdata courses --indent=2 --output=services/edu/apps/courses/fixtures/subjects.json
python -m services.edu.manage loaddata services/edu/apps/courses/fixtures/subjects.json
```