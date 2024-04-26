#!/usr/bin/python3
"""script that takes URL and displays value of X-Request-ID"""


import urllib.request
from sys import argv

if __name__ == '__main__':
    url = argv[1]

    # fetch data from the URL
    with urllib.request.urlopen(url) as response:
        request_id = response.getheader('X-Request-Id')
        print("{}".format(request_id))
