from backend.types import UniqueViewsDocument
from typing import List
import requests
from dotenv import load_dotenv
import os
load_dotenv()

def fetch_github_unique_views() -> List[UniqueViewsDocument]:
    """
    Fetch GitHub data.
    """
    pass
    # Add your code here to fetch GitHub data
    url="https://api.github.com/repos"
    GITHUB_TOKEN=os.getenv("GITHUB_USER_TOKEN")
    GITHUB_USERNAME=os.getenv("GITHUB_USERNAME")
    GITHUB_REPO=os.getenv("GITHUB_REPO")
    url+=f"/{GITHUB_USERNAME}/{GITHUB_REPO}/traffic/views"
    print(url)
    r = requests.get(url = url, headers={'Authorization': f'Bearer {GITHUB_TOKEN}'})
    data = r.json()
    print(data)
    if(data.get('message')=='Not Found'):
        print("Not able to get data")
        return None
    views=data["views"]
    return_list=[]
    for day_stats in views:
        return_list.append(
            UniqueViewsDocument(
                date=day_stats["timestamp"], 
                site=GITHUB_REPO, 
                unique_views=day_stats["uniques"]))
    return return_list
