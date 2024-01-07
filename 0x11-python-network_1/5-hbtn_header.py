#!/usr/bin/python3
"""print id"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    print(req.headers["X-Request-Id"])
