import pytest
from testautomationcode.actions.app1 import App1, APPUI
from time import time
import json
import logging
import os


class TestChallenge0(object):
    @pytest.fixture(scope="module")
    def app1_utils(self):
        return App1()

    def test_get_all_users(self, app1_utils, ):
        assert app1_utils.get_all_user_ids()

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

    # @pytest.fixture()
    # def launch_driver(self, driver):
    #     driver.get(os.environ['CHALLENGE0URL'])
    #     driver.maximize_window()
    #
    #     self.app_ui = APPUI(driver)
    #
    #     self._logger = logging.getLogger(__name__)
    #     yield
    #     self._logger.info("****** Dumping complete dom after each exp : %s " % driver.page_source)

    def test_add_user(self, app1_utils, driver):
        driver.get(os.environ['CHALLENGE0URL'])
        driver.maximize_window()

        self.app_ui = APPUI(driver)

        self._logger = logging.getLogger(__name__)

        user_details = {
            "name": "Mayank1",
            "surname": "Mahajan1",
            "adress": "Guavus1"
        }
        app1_utils.add_user(user_details)
        assert self.app_ui.check_user_at_ui(driver)
        assert app1_utils.delete_last_user().ok
        assert not self.app_ui.check_user_at_ui(driver)
