import os
import requests

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}


def get_issues(repo, since=None):

    url = f"https://api.github.com/repos/{repo}/issues"

    params = {}

    if since:
        params["since"] = since

    response = requests.get(
        url,
        headers=HEADERS,
        params=params
    )

    response.raise_for_status()

    return response.json()


def get_commits(repo, since=None):

    url = f"https://api.github.com/repos/{repo}/commits"

    params = {}

    if since:
        params["since"] = since

    response = requests.get(
        url,
        headers=HEADERS,
        params=params
    )

    response.raise_for_status()

    return response.json()