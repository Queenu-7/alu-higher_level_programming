#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status and displays response details.

The script uses urllib to perform a GET request to the specified URL.
It then prints:
    - the type of the response body
    - the byte content
    - the UTF-8 decoded content
"""

import urllib.request

url = 'https://intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read()
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode('utf-8'))
