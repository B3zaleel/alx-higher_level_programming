#!/usr/bin/env bash
# Follows a URL and its redirects for a non-redirect response
curl -L --max-redirs '-1' "$1"
