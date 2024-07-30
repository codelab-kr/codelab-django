from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.template.loader import render_to_string

from common.models.mixins import CreatedUpdatedMixin

from .fields import OrderField


class Subject(CreatedUpdatedMixin):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Course(CreatedUpdatedMixin):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courses_created')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='courses_joined', blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Module(CreatedUpdatedMixin):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'])  # type: ignore

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order}.{self.title}'


class Content(CreatedUpdatedMixin):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='contents')
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, limit_choices_to={'model__in': ('text', 'video', 'image', 'file')}
    )
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    url = models.URLField(blank=True)
    text = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['module'])  # type: ignore

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.module.title}.{self.content_type}'


class ItemBase(CreatedUpdatedMixin):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)s_related')
    title = models.CharField(max_length=200)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def render(self):
        return render_to_string(f'courses/content/{self._meta.model_name}.html', {'item': self})


class Text(ItemBase):
    content = models.TextField()


class Image(ItemBase):
    file = models.ImageField(upload_to='images')


class File(ItemBase):
    file = models.FileField(upload_to='files')


class Video(ItemBase):
    url = models.URLField()
