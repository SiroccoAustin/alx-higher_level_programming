#!/usr/bin/python3
"""Send a post request to the server"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    encode_data = urllib.parse.urlencode(email).encode("ascii")
    data = urllib.request.Request(url, encode_data)

    with urllib.request.urlopen(data) as response:
        print(response.read().decode("utf-8"))
