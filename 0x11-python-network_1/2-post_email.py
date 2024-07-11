#!/usr/bin/python3
"""sends a post request to a url"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    email = sys.argv[2]
    url = sys.argv[1]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data) as response:
        body = response.read()
        print(body.decode('utf-8'))

