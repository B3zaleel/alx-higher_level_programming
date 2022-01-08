#!/usr/bin/python3
"""Fetches a URL."""
from urllib import request


if __name__ == '__main__':
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        data = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(data)))
        print('\t- content: {}'.format(data))
        print('\t- utf-8 content: {}'.format(data.decode('utf-8')))
