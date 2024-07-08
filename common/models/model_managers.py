# -*- coding: utf-8 -*-

from django.db import models

from .model_querysets import StarterQuerySet


class StarterManager(models.Manager):

    def get_queryset(self):
        return StarterQuerySet(self.model, using=self._db)
