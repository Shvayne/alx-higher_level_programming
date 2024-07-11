#!/usr/bin/python3
"""prints the last 10 commits of a user"""
import requests
import sys

if __name__ == "__main__":
    owner = sys.argv[1]
    repo = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response  = requests.get(url)
    if response.status_code == 200:
        commits = response.json()[:10]

        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")

        else:
            print(f"Error fetching commits: {response.status_code}")

