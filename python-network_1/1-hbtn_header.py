#!/usr/bin/python3
"""
    Python script that takes in a URL, sends a request to the URL and displays the value of the variable
"""
import requests
import sys

if __name__ == "__main__":
    # Get the URL from command line arguments
    url = sys.argv[1]
    
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:

        # Get the value of the 'X-Request-Id' h
        request_id = response.headers.get('X-Request-Id')

        # Display the value of 'X-Request-Id'
        if request_id:
            print(request_id)
    else:
        print("Request failed with status code: {}".format(response.status_code))
            
