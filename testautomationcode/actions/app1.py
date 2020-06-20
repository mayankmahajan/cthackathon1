from testautomationcode.utils.api.api_request import ApiRequest
from testautomationcode.utils.api.api_request_specification import ApiRequestSpecification
import os

from testautomationcode.utils.api.request_type import RequestType
import logging


class App1(object):
    def __init__(self):
        self.api_request = ApiRequest()
        self.base_url = os.environ["BASEURL"]
        self.version = "api/v2"
        self._logger = logging.getLogger(__name__)

    def get_all_users(self):
        endpoint = "users"
        url = "%s/%s/%s" % (self.base_url, self.version, endpoint)
        api_request_specification = ApiRequestSpecification(RequestType.GET, url)
        resp = self.api_request.execute_request(api_request_specification)
        assert resp.ok
        response = resp.json()
        self._logger.info("API Response: %s" % response)
        return response["user"]

    def get_users_param(self, key):
        return [user[key] for user in self.get_all_users()]

    def get_all_user_ids(self):
        ids = self.get_users_param("id")
        self._logger.info(str(ids))
        return ids
