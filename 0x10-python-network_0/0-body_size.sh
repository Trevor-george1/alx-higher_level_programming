#!/usr/bin/env bash
# script that sends a request to a URL and display
# the size of body of response

curl -s "$1" | wc -c