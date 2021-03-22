import json

from HAAApiService import HAAApiService
from Logger import AppLogger

CONFIG = "app.json"

# read app settings
with open(CONFIG) as app_config_json:
    app_config = json.load(app_config_json)
log = AppLogger(app_config, "log.txt")

job = HAAApiService(app_config, log)
# test for "LookupName" API method
# the return count should be greater than 0
try:
    count = job.request_api_count("LookupName")
    if count > 0:
        print("Passed!")
    else:
        print("Failed!")
except:
    print("Failed!")
