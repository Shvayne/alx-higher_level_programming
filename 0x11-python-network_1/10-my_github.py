#!/usr/bin/python3
import requests
import sys
""" takes your GitHub credentials (username and password) and uses the GitHub API to display your id"""

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = f'https://api.github.com/users/{username}'
    headers = {'Authorization': f'token {password}'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_info = response.json()
        user_id = user_info.get('id')
        print(user_id)
    else:
        print(None)

