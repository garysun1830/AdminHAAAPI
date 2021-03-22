import json


class APIException(Exception):
    """customized Exception for API calls"""

    def __init__(self, url, response):
        self.error = None
        if not response:
            self.error["message"] = "No response: %s" % url
            return
        # deserialize response content to objects
        # create this object from response
        self.error = {"url": url, "status_code": response.status_code}
        msg = json.loads(response.text)
        text = "No message"
        if len(msg) > 0:
            if "message" in msg:
                text = msg["message"]
            else:
                text = json.dumps(msg)
        self.error["message"] = "Call API failed. url: %s,   status code: %s, error: %s" % (
            url, response.status_code, text)
