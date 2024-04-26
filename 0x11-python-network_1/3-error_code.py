#!/usr/bin/python3
"""Send request to url and display response decoded in utf-8"""


import urllib.request
import sys


url = sys.argv[1]
if __name__ == '__main__':
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {e.code}")