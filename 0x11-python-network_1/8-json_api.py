#!/usr/bin/python3
"""send post request to url using requests"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user'

    # create a dictionary for the data
    data = {'q': letter}

    # make a POST request with the data
    response = requests.post(url, data=data)

    # check if json valid
    try:
        body = response.json()

        if body == {}:
            print("No result")
        else:
            print("[{}] {}".format(body.get('id'), body.get('name')))
    except ValueError:
        print("Not a valid JSON")
