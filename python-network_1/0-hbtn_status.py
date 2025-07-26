#!/usr/bin/python3
"""
This script fetches the status of the URL https://intranet.hbtn.io/status
using the urllib package. It prints:
    - the type of the response body
    - the raw byte content
    - the decoded UTF-8 content
"""

import urllib.request

url = 'https://intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read()
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode('utf-8'))
