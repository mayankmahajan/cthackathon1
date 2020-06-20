import pytest
from testautomationcode.actions.app1 import App1
from time import time
import json


class TestChallenge0(object):
    @pytest.fixture(scope="module")
    def app1_utils(self):
        return App1()

    # def test_get_all_users(self, app1_utils, ):
    #     assert app1_utils.get_all_user_ids()

    def test_user_operations(self, app1_utils):
        user_details = {
            "name": "Mayank",
            "surname": "Mahajan",
            "adress": "Guavus"
        }
        resp = app1_utils.add_user(user_details)
        user_details['id'] = resp['id']
        user_details['name'] = "M"
        assert app1_utils.update_user(user_details).ok
        assert app1_utils.delete_last_user().ok
