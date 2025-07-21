#!/bin/bash
# Sends a GET request to the given URL and displays the size of the response body in bytes
curl -s "$1" -o temp_response && wc -c < temp_response && rm -f temp_response
