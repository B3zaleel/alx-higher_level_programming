#!/usr/bin/env bash
# Sends a POST request to a given URL, and displays the body of the response
curl -H 'Content-Type: application/json' --data-ascii "$(cat "$2")" "$1"
