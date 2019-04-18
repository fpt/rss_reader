import requests
import feedparser
from lxml import html

SITE_URL = "https://nulab.com/ja/blog/"
RSS_URL = "https://nulab.com/ja/feed/"

def inspect(site_uri):
    r = requests.get(site_uri)
    if r.status_code is not 200:
        raise('error')

    tree = html.fromstring(r.content)
    hrefs = tree.xpath('//link[@rel="alternate" and @type="application/rss+xml"]/@href')
    print(hrefs)

def fetch(rss_uri):
    rss_dic = feedparser.parse(rss_uri)

    print(rss_dic.feed.title)

    for entry in rss_dic.entries:
        if 'title' in entry and 'link' in entry:
            title = entry.title
            link  = entry.link
            print(link)
            print(title)

if __name__ == '__main__':
    inspect(SITE_URL)
    # fetch(RSS_URL)
