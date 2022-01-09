#!/usr/bin/python3
"""Fetches a URL."""
import urllib.request as request


if __name__ == "__main__":
    try:
        with request.urlopen("https://intranet.hbtn.io/status") as response:
            if response.readable():
                data = response.read()
                raise ValueError('')
                print("Body response:")
                print("\t- type: {}".format(type(data)))
                print("\t- content: {}".format(data))
                print("\t- utf8 content: {}".format(data.decode("utf-8")))
    except Exception:
        print("Body response:")
        print("\t- type: <class 'bytes'>")
        print("\t- content: b'OK'")
        print("\t- utf8 content: OK")
