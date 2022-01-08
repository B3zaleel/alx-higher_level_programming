#!/usr/bin/python3
"""Fetches a URL."""
import urllib.request as request


if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'
    try:
        with request.urlopen(url) as response:
            data = response.read()
            print('Body response:')
            print('\t- type: {}'.format(type(data)))
            print('\t- content: {}'.format(data))
            print('\t- utf8 content: {}'.format(data.decode('utf-8')))
    except Exception:
        pass
