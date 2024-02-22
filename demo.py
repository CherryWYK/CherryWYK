import requests
import os

org = 'COMP5241-2324-Project'
token = os.getenv('YOUR_GITHUB_TOKEN')
if token is None:
    raise ValueError("Missing GitHub token. Please set the 'YOUR_GITHUB_TOKEN' environment variable.")
headers = {'Authorization': f'token {token}'}

# Get all repositories of the organization
response = requests.get(f'https://api.github.com/orgs/{org}/repos', headers=headers)
repos = response.json()

# For each repository, get the issues and commits
for repo in repos:
    # Get issues
    response = requests.get(f'https://api.github.com/repos/{org}/{repo["name"]}/issues', headers=headers)
    issues = response.json()
    for issue in issues:
        print(f"Issue: {issue['title']}")

    # Get commits
    response = requests.get(f'https://api.github.com/repos/{org}/{repo["name"]}/commits', headers=headers)
    commits = response.json()
    for commit in commits:
        print(f"Commit: {commit['commit']['message']}")
