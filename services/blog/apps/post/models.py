import uuid

from django.db import models

from common.models.managers import SearchManager
from common.models.mixins import CreatedUpdatedMixin


class Post(CreatedUpdatedMixin):
    title = models.CharField(max_length=500)
    image = models.URLField(max_length=500, null=True, blank=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    chapter_verse = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField()
    id = models.CharField(
        max_length=100,
        default=uuid.uuid4,  # type: ignore
        unique=True,
        primary_key=True,
        editable=False,
    )

    objects = SearchManager()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.title)


class Book(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
