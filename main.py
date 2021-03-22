import json
import sys
from datetime import datetime
from HAAApiService import HAAApiService
from Logger import AppLogger

CONFIG = "app.json"

# read app settings
with open(CONFIG) as app_config_json:
    app_config = json.load(app_config_json)
log = AppLogger(app_config, "log.txt")

try:
    log.write_line({"start at": datetime.now()})
    if len(sys.argv) < 2:
        print("API name is missing from the command line.")
        print("Please use python.exe main.py <api_name>")
        log.write_line("API name is missing from the command line.")
    else:
        api_name = sys.argv[1]
        job = HAAApiService(app_config, log)
        count = job.request_api_count(api_name)
        print("API %s has been called %d times." % (api_name, count))
except Exception as e:
    log.write_line(e)
