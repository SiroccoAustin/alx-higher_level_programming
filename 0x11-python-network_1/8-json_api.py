#!/usr/bin/python3
"""post request"""
import sys
import requests

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    value = {"q": letter}
    url = "http://0.0.0.0:5000/search_user")
    req = request.post(url, data=value)
    try:
        resp = req.json()
        if resp == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")

