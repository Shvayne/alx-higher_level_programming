#!/usr/bin/python3
"""prints the last 10 commits of a user"""
import requests
import sys

if __name__ == "__main__":
    res = requests.get("https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1]
        )
    commits = res.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass

