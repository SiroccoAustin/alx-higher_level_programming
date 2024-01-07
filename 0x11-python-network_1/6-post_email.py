#!/usr/bin/python3
"""request post to the server"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email", sys.argv[2]}
    req = requests.post(url, json=email)
    print(req.text)
