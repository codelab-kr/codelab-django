# -*- coding: utf-8 -*-

import pytest
from django.test import Client


class TestDealListView:

    @pytest.mark.django_db
    def test_list(self, client: Client):
        response = client.get('/')
        assert response.status_code == 200
