#!/usr/bin/env bash
# Retrieves the status code of a request sent to a given URL
curl -s -w "%{response_code}\n" -o /dev/null "$1"
