#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL 
and displays the value of the variable
"""

import requests
import sys 

if __name__ == "__main__":
    # Get the URL from command line arguments
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code == 200:
        request_id = response.headers.get('X-Request-Id') 
        
        "Displays the value of X-Request-Id"
        if request_id:
            print(request_id)
            
        else:
            print("Request failed with status code: {}".format(response.status_code))
            
