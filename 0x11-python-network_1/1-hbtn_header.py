#!/usr/bin/python3
"""send the request to the server"""
import urllib.request
import sys

if __name__ == "__main__":
    user_input = sys.argv[1]
    req = urllib.request.Request(user_input)
    with urllib.request.urlopen(req) as response:
        content = response.info()
        obj = dict(content)
        print(obj["X-Request-Id"])
