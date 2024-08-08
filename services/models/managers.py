from django.db import models

from services.models.querysets import SearchQuerySet


class SearchManager(models.Manager):

    def get_queryset(self):
        return SearchQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)
