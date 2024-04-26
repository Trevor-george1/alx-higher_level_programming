#!/usr/bin/python3
"""Using githu api to check my user id"""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # get username and password
    username = sys.argv[1]
    password = sys.argv[2]

    # Github API URL
    url = 'https://api.github.com/user'

    # authentication
    auth = HTTPBasicAuth(username, password)

    # send GET request to Github API
    response = requests.get(url, auth=auth)
    print(response.json().get('id'))
