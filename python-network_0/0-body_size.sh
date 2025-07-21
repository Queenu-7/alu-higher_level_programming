#!/bin/bash
# Sends a request to a URL and displays the size (in bytes) of the body of the response
curl -s "$1" | wc -c
