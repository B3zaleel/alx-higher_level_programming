#!/usr/bin/python3
"""Fetches a URL."""
from urllib import request


if __name__ == '__main__':
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        data = response.read()
        print('Body response:')
        # tabs = '\t'
        tabs = '    '
        print('{}- type: {}'.format(tabs, type(data)))
        print('{}- content: {}'.format(tabs, data))
        print('{}- utf8 content: {}'.format(tabs, data.decode('utf-8')))
