# -*- coding: utf-8 -*-

import pytest

from common.auth import forms as f


class TestLogin:

    @pytest.mark.django_db
    def test_login(self):
        form = f.Login({})
        assert not form.is_valid()


class TestSignUp:

    @pytest.mark.django_db
    def test_signup(self):
        form = f.SignUp({})
        assert not form.is_valid()


# class TestDealCreate:
#     @pytest.mark.django_db
#     def test_create_should_fail(self):
#         form = f.DealCreate({})
#         assert not form.is_valid()

#     @pytest.mark.django_db
#     def test_create_should_create_deal(self, user1):
#         form = f.DealCreate({'title': 'My Deal'})
#         assert form.is_valid()
#         form.save(user1.id)
