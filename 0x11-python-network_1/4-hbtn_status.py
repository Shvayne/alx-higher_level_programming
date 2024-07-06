#!/usr/bin/python3
import requests
"""this script fetches a url status"""
if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    body = response.text

    print("Body response:")
    print("\t- type:", type(body))
    print(f"\t- content: {body}")

