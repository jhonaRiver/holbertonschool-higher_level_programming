#!/usr/bin/python3
'''
script that takes in a URL, sends a request to the URL and displays the value
of the variable X-Request-Id in the response header
'''
from sys import argv
import requests


if __name__ == "__main__":
    response = requests.get(argv[1])
    header_dict = response.headers
    print(header_dict.get('X-Request-Id'))
