#!/usr/bin/python3
"""this script fetches a url status"""
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    body = response.text

    print("Body response:")
    print("\t- type:", type(body))
    print(f"\t- content: {body}")

