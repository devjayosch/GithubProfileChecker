import requests
from collections import Counter

username = input("Github username: ").strip()

user = requests.get(f"https://api.github.com/users/{username}").json()
repos = requests.get(f"https://api.github.com/users/{username}/repos?per_page=100").json()

languages = Counter(repo["language"] for repo in repos if repo["language"])

print(f"\nGithub Profile from {user['login']}")
print(f"Name: {user.get('name')}")
print(f"Bio: {user.get('bio')}")
print(f"Repos Count: {user.get('public_repos')}")
print(f"Followers: {user.get('followers')}")
print(f"Following: {user.get('following')}")
print(f"Most used language: {languages.most_common(1)[0][0]}")

print(f"Profile: {user['html_url']}")
