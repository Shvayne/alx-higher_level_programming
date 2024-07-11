#!/usr/bin/python3
"""displays athe result of the X-request_id in the header"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    x_request = response.headers.get('X-request-Id')
    print(x_request)

