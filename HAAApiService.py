import ApiException
from HAAApi import HAAApi


class HAAApiService:

    def __init__(self, app_config, log):
        self.app_config = app_config
        self.log = log
        self.HAAApiCall = HAAApi()

    def request_api_count(self, api_name):
        try:
            return self.HAAApiCall.request_api_count(api_name)
        except ApiException as e:
            self.log.write_line(e)
