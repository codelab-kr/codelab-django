from django.db import models
from django.urls import reverse

from services.models.mixins import CreatedUpdatedMixin


class Category(CreatedUpdatedMixin):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)  # unique는 Index의 생성을 의미

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product_list_by_category', args=[self.slug])


class Product(CreatedUpdatedMixin):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product_detail', args=[self.id, self.slug])  # type: ignore
