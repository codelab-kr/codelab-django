# -*- coding: utf-8 -*-

from django.db.models import QuerySet


class StarterQuerySet(QuerySet):

    def filter_by_keyword(self, keyword):
        return self.filter(title__contains=keyword)
