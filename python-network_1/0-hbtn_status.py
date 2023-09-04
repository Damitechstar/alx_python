#!/usr/bin/python3
"""
Script that fetches URL
"""

import requests

url = "https://alu-intranet.hbtn.io/status"

response = requests.get(url)

if response.status_code == 200:
    print("Body response:")
    print("\t- type: {}".format(type(response.text))) 
    print("\t- content: {}".format(response.text))

else:
    print("Error: {}".format(response.status_code))