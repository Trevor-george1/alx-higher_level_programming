#!/usr/bin/python3
"""script that takes URL and displays value of X-Request-ID
    using requests
"""


import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]

    # fetch data from the URL
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    print("{}".format(request_id))
