import pytest
from testautomationcode.actions.app1 import App1


class TestChallenge0(object):
    @pytest.fixture(scope="session")
    def app1_utils(self):
        return App1()

    def test_get_all_users(self, app1_utils, ):
        assert app1_utils.get_all_user_ids()
