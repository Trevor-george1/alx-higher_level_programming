#!/usr/bin/python3
"""using urlib to fetch from url"""

from urllib import request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    # fetch url
    with request.urlopen(url) as response:
        response_body = response.read()

        # Display the response body with tabs
        print("Body response:")
        print("\t- type: {}".format(type(response_body)))
        print("\t- content: {}".format(response_body))
        print("\t- utf8 content: {}".format(response_body.decode('utf-8')))
