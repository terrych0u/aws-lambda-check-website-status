#!/usr/bin/env python

import urllib2
import json
from urllib2 import Request, urlopen, URLError, HTTPError

def send2slack(url):
    HOOK_URL = "<slack_url>"
    slack_message = {
      'channel': "<channel_name>",
      'username':'<slack_username>',
      'icon_emoji':':boom:',
      'text': "Alarm: `%s` unreachable\nThreshold Crossed: 1 datapoint was not greater than or equal to the threshold (0.0). " % (url)
    }
    req = Request(HOOK_URL, json.dumps(slack_message))
    response = urlopen(req)
    response.read()

# def lambda_handler(event, context):
    if __name__ == '__main__':
    target = [
        "https://www.exsample.com",
        "https://www.123.com"
    ]

    for url in target:
        request = urllib2.Request(url)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            http_code = e.code
        else:
            http_code = response.code

        if http_code != 200:
            send2slack(url)
    response.close()