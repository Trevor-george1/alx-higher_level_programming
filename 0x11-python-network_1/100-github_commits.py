#!/usr/bin/python3
"""Fetch commits from repo in github using API"""


import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        owner, repo_name
    )

    params = {'per_page': 10, 'page': 1}
    response = requests.get(url, params=params)

    commits = response.json()

    for commit in commits:
        sha = commit['sha']
        author = commit['commit']['author']['name']
        print("{}: {}".format(sha, author))
