#!/bin/bash
#script that sends a request
curl -s "$1" | wc -c
