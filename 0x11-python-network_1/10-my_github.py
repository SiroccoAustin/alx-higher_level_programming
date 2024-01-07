#!/usr/bin/python3
"""display my github id"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    auth = HTTPBasicAuth(username, password)
    url = "https://api.github.com/user"
    response = requests.get(url, auth=auth)
    print(r.json().get("id"))
