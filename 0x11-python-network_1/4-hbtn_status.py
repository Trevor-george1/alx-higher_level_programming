#!/usr/bin/python3
"""fetches from url"""


import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'

    # fetch from url
    response = requests.get(url)
    body = response.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
