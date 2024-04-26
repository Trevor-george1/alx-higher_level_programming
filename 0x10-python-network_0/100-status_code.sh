#!/bin/bash
# script that sends a request to url and display status code
curl -sI -o dev/null -w "%{http_code}" "$1"
