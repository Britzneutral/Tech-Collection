import feedparser
import pprint

class SQL_test():
    def search_zenn(keyword):
        url = f"https://zenn.dev/topics/{keyword}/feed"
        f = feedparser.parse(url)
        return f

    def search_qiita(keyword):
        url = f"https://qiita.com/tags/{keyword}/feed.atom"
        f = feedparser.parse(url)
        return f
    
    def __init__(self, url, f):
        self.url = url
        self.f = f
  