import os
import requests
import json

from ApiException import APIException


class HAAApi:
    CONFIG = "api.json"

    def __init__(self):
        with open(HAAApi.CONFIG) as api_config_json:
            self.api_config = json.load(api_config_json)

    def populate_url(self, method, url_params):
        root = self.api_config["admin_api_root"]
        url = self.api_config[method]
        if url_params:
            url = url % tuple(url_params)
        url = os.path.join(root, url)
        return url

    @staticmethod
    def api_call_return(response):
        result = {"response": response}
        if response.text:
            text = response.text.strip()
            if text and (text.startswith("{") or text.startswith("[")):
                result["text"] = json.loads(text)
        return result

    def call_api(self, method, url_params=None):
        url = self.populate_url(method, url_params)
        response = requests.get(url=url)
        if response.ok:
            return self.api_call_return(response)
        raise APIException(url, response)

    def request_api_count(self, method):
        haa_api_root = self.api_config["haa_api_root"]
        haa_api_root = haa_api_root.replace("://", "_").replace("/", "_").replace(".", "_")
        result = self.call_api("admin_api_get_request_count", [haa_api_root, method])
        return result["text"]["RequestCount"]
