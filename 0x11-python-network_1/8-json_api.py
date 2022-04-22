#!/usr/bin/python3
'''
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
'''
import requests
import sys


if __name__ == "__main__":
    try:
        query = {"q": sys.argv[1]}
    except:
        query = {"q": ""}
    url = 'http://0.0.0.0:5000/search_user'
    try:
        r = requests.post(url, query)
        if (r.json().get('id') is not None):
            print("[{}] {}".format(r.json().get('id'), r.json().get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
