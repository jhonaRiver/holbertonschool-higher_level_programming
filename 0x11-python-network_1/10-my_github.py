#!/usr/bin/python3
'''
script that takes your GitHub credentials (username and password) and uses
the GitHub API to display your id
'''
from sys import argv
import requests


if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(user, passwd))
    print(response.json().get('id'))
