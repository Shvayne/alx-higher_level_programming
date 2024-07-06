#!/usr/bin/python3
import urllib.request
import urllib.error
import sys
"""takes a url, send a request to the url and display the body of the response while handling any errors"""
if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try: 
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

