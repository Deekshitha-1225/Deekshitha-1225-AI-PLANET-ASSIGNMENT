import requests
import os
from bs4 import BeautifulSoup

def search_datasets_on_kaggle(query):
    kaggle_url = f"https://www.kaggle.com/search?q={query}&sortBy=mostVotes"
    
    response = requests.get(kaggle_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    datasets = []
    links = soup.find_all('a', class_='dataset-link')
    
    for link in links[:5]:  # Fetch top 5 datasets
        datasets.append({
            "title": link.text,
            "link": "https://www.kaggle.com" + link.get('href')
        })

    return datasets

# Example
if __name__ == "__main__":
    query = "healthcare"
    datasets = search_datasets_on_kaggle(query)
    print(datasets)
