import uuid

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=500)
    image = models.URLField(max_length=500)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    chapter_verse = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(
        max_length=100,
        default=uuid.uuid4,  # type: ignore
        unique=True,
        primary_key=True,
        editable=False,
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-created']


class Book(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
