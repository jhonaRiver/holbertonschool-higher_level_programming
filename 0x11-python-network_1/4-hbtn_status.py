#!/usr/bin/python3
'''
script that fetches https://intranet.hbtn.io/status
'''
import requests


if __name__ == "__main__":
    response = requests.get('https://intranet.hbtn.io/status')
    content = response.content.decode('utf8')
    output = "Body response:\n\t- type: {}\n\t- content: {}"
    print(output.format(type(content), content))
