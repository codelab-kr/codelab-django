from django.db import models


class CreatedUpdatedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # 추상모델임을 나타냄
