import os
import requests
import json

from ApiException import APIException


class HAAApi:
    """ API caller that requests for REST API from the server"""
    """ the API url and parameters are in api.json """

    CONFIG = "api.json"

    def __init__(self):
        with open(HAAApi.CONFIG) as api_config_json:
            self.api_config = json.load(api_config_json)
        self.api_url_root = self.api_config["admin_api_root"]

    def populate_url(self, method, url_params):
        """ populate API URL with the API method and parameters """
        url = self.api_config[method]
        if url_params:
            url = url % tuple(url_params)
        url = os.path.join(self.api_url_root, url)
        return url

    @staticmethod
    def api_call_return(response):
        """ populate object from response to return to the caller """
        result = {"response": response}
        if response.text:
            text = response.text.strip()
            if text and (text.startswith("{") or text.startswith("[")):
                result["text"] = json.loads(text)
        return result

    def call_api(self, method, url_params=None):
        url = self.populate_url(method, url_params)
        # call REST API with requests
        response = requests.get(url=url)
        if response.ok:
            return self.api_call_return(response)
        # not response.ok, failed to call API
        raise APIException(url, response)

    def request_api_count(self, method):
        """ to retrieve the count of a specific API method called  """
        # populate the parameters for the API call
        haa_api_root = self.api_config["haa_api_root"]
        haa_api_root = haa_api_root.replace("://", "_").replace("/", "_").replace(".", "_")
        # call API
        result = self.call_api("admin_api_get_request_count", [haa_api_root, method])
        # when successful, get the count
        return result["text"]["RequestCount"]
