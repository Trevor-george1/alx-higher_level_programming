#!/bin/bash
#script that sends a request to a URL
curl -s "$1" | wc -c