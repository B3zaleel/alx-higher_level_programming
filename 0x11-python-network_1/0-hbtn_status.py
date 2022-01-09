#!/usr/bin/python3
"""Fetches a URL."""
import urllib.request as request


if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        if response.readable():
            data = response.read()
            print("Body response:\r")
            print("\t- type: {}\r".format(type(data)))
            print("\t- content: {}\r".format(data))
            print("\t- utf8 content: {}\r".format(data.decode("utf-8")))
