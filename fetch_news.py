import requests
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Access environment variables
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

NEWS_URL = "https://newsapi.org/v2/everything"

def fetch_news(query="Web3 OR blockchain OR AI"):
    params = {
        "q": query,
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 5
    }
    response = requests.get(NEWS_URL, params=params)
    articles = response.json().get("articles", [])
    return [
        {"title": article["title"], "url": article["url"]}
        for article in articles
    ]