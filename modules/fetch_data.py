import requests

def fetch_multimodal_data(ticker):
    api_key = "d20tfn9r01qvvf1k2ao0d20tfn9r01qvvf1k2aog"  
    url = f"https://finnhub.io/api/v1/company-news?symbol={ticker}&from=2024-07-01&to=2024-07-24&token={api_key}"
    res = requests.get(url)
    
    if res.status_code != 200:
        return ["Failed to fetch news."], [], []

    data = res.json()
    if not data:
        return ["No news found."], [], []

    texts = [article['headline'] + ". " + article.get('summary', '') for article in data[:2]]
    images = [article['image'] for article in data[:2] if article.get('image')]
   

    return texts, images

