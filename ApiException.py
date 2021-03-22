import json


class APIException(Exception):

    def __init__(self, url, response):
        if not response:
            self.error["message"] = "No response: %s" % url
            return
        msg = json.loads(response.text)
        text = "No message"
        if len(msg) > 0:
            if "message" in msg:
                text = msg["message"]
            else:
                text = json.dumps(msg)
        self.error["message"] = "Call API failed. url: %s,   status code: %s, error: %s" % (
            url, response.status_code, text)
