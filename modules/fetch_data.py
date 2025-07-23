import requests
from newspaper import Article

# 临时抓取逻辑：从 Yahoo Finance 新闻页提取第一个文章内容
def fetch_multimodal_data(ticker):
    # 获取新闻搜索页
    search_url = f"https://finance.yahoo.com/quote/{ticker}?p={ticker}"
    r = requests.get(search_url, headers={"User-Agent": "Mozilla/5.0"})

    if "https://finance.yahoo.com/news/" not in r.text:
        return ["No news found."], [], []

    # 提取第一个新闻链接
    start = r.text.find("https://finance.yahoo.com/news/")
    end = r.text.find('"', start)
    article_url = r.text[start:end]

    try:
        article = Article(article_url)
        article.download()
        article.parse()
        article.nlp()  # 可选：提取摘要
        summary = article.summary or article.text[:500]
    except Exception:
        summary = "Failed to load article."

    return [summary], [], []
