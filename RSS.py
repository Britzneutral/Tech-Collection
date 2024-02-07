import requests
from bs4 import BeautifulSoup
import re

class SQL():
    url = "https://www.yahoo.co.jp/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    elems = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))

    def __init__(self, url, res, soup, elems):
        self.url = url
        self.res = res
        self.soup = soup
        self.elems = elems

