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
        self.last_added_user = None

    def get_all_users(self):
        url = self.get_url(endpoint="users")
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

    def get_url(self, endpoint):
        return "%s/%s/%s" % (self.base_url, self.version, endpoint)

    def add_user(self, user_details):
        url = self.get_url(endpoint="addusers")
        api_req_spec = ApiRequestSpecification(RequestType.POST, url=url, json=user_details)
        resp = self.api_request.execute_request(api_req_spec)
        assert resp.ok
        self.last_added_user = resp.json()
        self._logger.info(
            "User added: %s with id %s." % (str(self.last_added_user['name']), str(self.last_added_user['id'])))
        return resp.json()

    def update_user(self, user_details):
        url = self.get_url(endpoint="updateuser")
        api_req_spec = ApiRequestSpecification(RequestType.PUT, url=url, json=user_details)
        return self.api_request.execute_request(api_req_spec)

    def update_user(self, user_details):
        url = self.get_url(endpoint="updateuser")
        api_req_spec = ApiRequestSpecification(RequestType.PUT, url=url, json=user_details)
        return self.api_request.execute_request(api_req_spec)

    def delete_last_user(self):
        url = self.get_url(endpoint="%s/deleteuser" % (self.last_added_user['id']))
        api_req_spec = ApiRequestSpecification(RequestType.DELETE, url=url)
        return self.api_request.execute_request(api_req_spec)

    def check_user_at_ui(self, driver):
        trs = driver.find_element_by_tag_name("table").find_elements_by_tag_name("tr")
        for i in range(len(trs) - 1, 0, -1):
            element = trs[i]
            self.scroll_into_view(driver, element)
            string_to_search = str(self.last_added_user['id']).lower() + " " + str(self.last_added_user['name']).lower()
            if string_to_search in str(trs[i].text).lower():
                return True

        return False

    def scroll_into_view(self, driver, element, align_to_top=True):
        self._logger.info("Scrolling vertically to element with text: %s" % element.text)
        if align_to_top is True:
            driver.execute_script("arguments[0].scrollIntoView();", element)
        else:
            driver.execute_script("arguments[0].scrollIntoView(false);", element)
