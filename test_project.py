import json

from HAAApiService import HAAApiService
from Logger import AppLogger
from RequestApiCount import RequestApiCount

CONFIG = "app.json"

# read app settings
with open(CONFIG) as app_config_json:
    app_config = json.load(app_config_json)
log = AppLogger("log.txt")

job = HAAApiService(app_config, log)
count = job.request_api_count("LookupName")
if count > 0:
    print("Passed!")
else:
    print("Failed!")
input()
