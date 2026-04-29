import requests
from bs4 import BeautifulSoup

def get_trending_repos():
    url = "https://github.com/trending"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return "Failed to fetch data"

    soup = BeautifulSoup(response.text, "html.parser")
    repos = soup.find_all("article", class_="Box-row", limit=5)
    
    trending_data = []
    for repo in repos:
        title = repo.h2.text.strip().replace("\n", "").replace(" ", "")
        desc = repo.p.text.strip() if repo.p else "No description"
        trending_data.append(f"Repo: {title}\nDescription: {desc}\n")
    
    return "\n".join(trending_data)

if __name__ == "__main__":
    print(get_trending_repos())