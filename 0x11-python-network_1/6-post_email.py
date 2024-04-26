#!/usr/bin/python3
"""script that takes URL and email and POSTS
    using requests
"""


import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    email = argv[2]

    # create a dictionary
    data = {'email': email}

    # Make POST request with data
    response = requests.post(url, data=data)
    print(response.text)
