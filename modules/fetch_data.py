import requests
from datetime import datetime, timedelta

def fetch_multimodal_data(ticker):
    api_key = "d20tfn9r01qvvf1k2ao0d20tfn9r01qvvf1k2aog"  
    
    # 当前 UTC 时间 和 24 小时前时间（用于调用 API）
    now = datetime.utcnow()
    from_date = (now - timedelta(days=1)).strftime('%Y-%m-%d')
    to_date = now.strftime('%Y-%m-%d')

    url = f"https://finnhub.io/api/v1/company-news?symbol={ticker}&from={from_date}&to={to_date}&token={api_key}"
    res = requests.get(url)

    if res.status_code != 200:
        return ["Failed to fetch news."], []

    data = res.json()
    if not data:
        return ["No news found."], []

    # ✅ 只保留最近 6 小时的新闻
    cutoff_time = now - timedelta(hours=6)
    recent_articles = []
    for article in data:
        try:
            published_time = datetime.fromtimestamp(article['datetime'])
            if published_time >= cutoff_time:
                recent_articles.append(article)
        except:
            continue

    if not recent_articles:
        return ["No recent news in the last 6 hours."], []

    texts = [a['headline'] + ". " + a.get('summary', '') for a in recent_articles[:2]]
    images = [a['image'] for a in recent_articles[:2] if a.get('image')]

    return texts, images

