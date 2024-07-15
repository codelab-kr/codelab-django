# -*- coding: utf-8 -*-

from django.db.models import Q, QuerySet


class SearchQuerySet(QuerySet):

    def search(self, query):
        # return self.filter(Q(title__icontains=query) | Q(content__icontains=query))
        return self.filter(Q(title__icontains=query))
