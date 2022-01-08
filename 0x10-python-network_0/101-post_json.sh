#!/bin/bash
# Sends a POST request to a given URL, and displays the body of the response
curl -X POST -H 'Content-Type: application/json' --d "$(cat "$2")" "$1"
