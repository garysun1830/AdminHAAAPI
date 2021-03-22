import json
import sys
from datetime import datetime
from HAAApiService import HAAApiService
from Logger import AppLogger
""" this application calls the REST API from the server """
""" the server URL is configured in api.json """
""" this is entry of the whole application """
""" run this application to retrieve the count of a given API method called"""
""" run command: """
""" python.exe main.py <api_name>"""
""" use test_project.py to test this application """

CONFIG = "app.json"

# read app settings
with open(CONFIG) as app_config_json:
    app_config = json.load(app_config_json)
# create a logger
log = AppLogger(app_config, "log.txt")

try:
    log.write_line({"start at": datetime.now()})
    # bring in the API method name from the command line
    if len(sys.argv) < 2:
        # the API method name not brought in
        print("API name is missing from the command line.")
        print("Please use python.exe main.py <api_name>")
        log.write_line("API name is missing from the command line.")
    else:
        # get API method name from the command line
        api_name = sys.argv[1]
        # use the service object to execute the API call
        job = HAAApiService(app_config, log)
        count = job.request_api_count(api_name)
        print("API %s has been called %d times." % (api_name, count))
except Exception as e:
    log.write_line(e)
