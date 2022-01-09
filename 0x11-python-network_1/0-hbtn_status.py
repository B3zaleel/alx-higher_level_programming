#!/usr/bin/python3
"""Fetches a URL."""
import urllib.request as request


if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'
    with request.urlopen(url) as response:
        if response.readable():
            data = response.read()
            print('Body response:')
            print('\ttype: {}'.format(type(data)))
            print('\tcontent: {}'.format(data))
            print('\tutf-8 content: {}'.format(data.decode('utf-8')))
