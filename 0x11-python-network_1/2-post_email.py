#!/usr/bin/python3
"""POST request with email as data
    display body of response
"""


import urllib.request
import urllib.parse
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    email = argv[2]

    # create dictionary of data
    data = {'email': email}

    # encode
    encoded_data = urllib.parse.urlencode(data).encode('ascii')

    # Make a POST request
    with urllib.request.urlopen(url, data=encoded_data) as response:
        body = response.read().decode('utf-8')
        print("Your email is: {}".format(body))
