#!/bin/bash
# Sends a POST request to a given URL, and displays the body of the response
curl -s -X POST -H 'Content-Type: application/json' -d "$([ -f "$2" ] && cat "$2")" "$1"
