import requests

API_KEY = '172b2b28664a482e92dd3ca48068ede1'
ENDPOINT = 'https://newsapi.org/v2/top-headlines'

params = {
    'apiKey': API_KEY,
    'country': 'us',  # You can change this to fetch news from different countries
    'pageSize': 100  # Number of articles to fetch
}

response = requests.get(ENDPOINT, params=params)
data = response.json()

headlines = [article['title'] for article in data['articles']]
