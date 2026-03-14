import requests

def get_news(query):

    url = "https://newsapi.org/v2/everything"

    params = {
        "q": query,
        "sortBy": "publishedAt",
        "language": "en",
        "apiKey": "YOUR_NEWS_API_KEY"
    }

    response = requests.get(url, params=params)

    return response.json()