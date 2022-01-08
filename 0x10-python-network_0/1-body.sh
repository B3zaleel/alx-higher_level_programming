#!/usr/bin/env bash
# Gets the body of a response from a URL if the status code is 200
[ "$(curl -sI "$1" | head -n1 | cut -d ' ' -f2)" == '200' ] && curl "$1"
