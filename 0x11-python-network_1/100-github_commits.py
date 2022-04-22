#!/usr/bin/python3
'''
list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”
'''
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    commits = requests.get(url).json()
    for i in range(0, 10):
        if i < len(commits):
            print(commits[i].get("sha"), end=": ")
            print(commits[i].get("commit").get("author").get("name"))
