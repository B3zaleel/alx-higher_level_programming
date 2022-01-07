#!/usr/bin/python3
"""Retrieves the last 10 commits of a repository.
Usage: ./100-github_commits.py repository_name repository_owner_name
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 2:
        repository_name = sys.argv[1]
        owner_name = sys.argv[2]
        req_queries = 'per_page=10'
        req_url = 'https://api.github.com/repos/{}/{}/commits?{}'.format(
            owner_name,
            repository_name,
            req_queries
        )
        response = requests.get(
            req_url,
            headers={'Accept': 'application/vnd.github.v3+json'}
        )
        if response.status_code == 200:
            for commit in map(lambda x: x['commit'], response.json()):
                commit_sha = commit['tree']['sha']
                commit_author = commit['committer']['name']
                print('{}: {}'.format(commit_sha, commit_author))
