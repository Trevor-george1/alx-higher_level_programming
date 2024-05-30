#!/bin/bash
#script that sends json data to url
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
