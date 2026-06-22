import requests

def get_github_stars(owner, repo):

    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(
        url,
        headers={
            "Accept": "application/vnd.github+json"
        }
    )

    if response.status_code != 200:
        return None

    data = response.json()

    return {
        "name": data["full_name"],
        "stars": data["stargazers_count"],
        "forks": data["forks_count"],
        "url": data["html_url"]
    }