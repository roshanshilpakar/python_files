import feedparser
from plyer import notification
import time

def parseFeed():
    f = feedparser.parse("http://feeds.bci.co.np/news/rss.xml")
    for newsitem in f['items']:
        notification.notify(title=newsitem['title'], message = str(newsitem['summary']), timeout = 150)
        time.sleep(1200)


if __name__ == '_main_':
    parseFeed()
