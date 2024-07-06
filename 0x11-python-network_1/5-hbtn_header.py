#!/usr/bin/python3
import requests
import sys
"""displays the result of the X-Request-Id in the header"""

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    x_request = response.headers.get('X-request-Id')
    print(x_request)

