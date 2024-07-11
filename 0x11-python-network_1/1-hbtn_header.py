#!/usr/bin/python3
"""A script that takes a url and sends a request and display
the result of the variable found in the header"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.headers
        x_request = headers.get('X-request-Id')
        print(x_request)

