import feedparser, requests, os, time

BOT_TOKEN = os.environ['BOT_TOKEN']
CHANNEL_ID = "@IndiaJobAlertTamil"

FEEDS = [
    "https://ssc.nic.in/rss",
    "https://www.rrbcdg.gov.in/rss",
    "https://ibps.in/feed/",
    "https://www.nabard.org/rss",
    "https://tnpsc.gov.in/english/rss.xml"
]

def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHANNEL_ID, "text": msg, "parse_mode": "HTML"})

def check():
    for feed_url in FEEDS:
        try:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries[:2]:
                text = f"🚨 <b>{entry.title}</b>\n\n🔗 {entry.link}\n\n#CentralGovtJobs #TNJobs @IndiaJobAlertTamil"
                send(text)
                time.sleep(5)
        except:
            pass

if __name__ == "__main__":
    check()
