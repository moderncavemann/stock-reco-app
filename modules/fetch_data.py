import requests
from bs4 import BeautifulSoup

def fetch_multimodal_data(ticker):
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://finance.yahoo.com/quote/{ticker}?p={ticker}"
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    # 尝试抓取第一个新闻链接
    news_link = None
    for a in soup.find_all("a", href=True):
        if "/news/" in a["href"]:
            news_link = "https://finance.yahoo.com" + a["href"]
            break

    if not news_link:
        return ["No news found."], [], []

    # 抓正文内容
    article_res = requests.get(news_link, headers=headers)
    article_soup = BeautifulSoup(article_res.text, "html.parser")
    paras = article_soup.find_all("p")
    content = " ".join(p.get_text() for p in paras[:5])  # 最多前 5 段

    return [content], [], []
