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
    print(f"Sending: {msg[:50]}...")
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        r = requests.post(url, data={"chat_id": CHANNEL_ID, "text": msg, "parse_mode": "HTML"}, timeout=10)
        print(f"Result: {r.text[:200]}")
    except Exception as e:
        print(f"Send failed: {e}")

def check():
    print("Bot started checking feeds...")
    count = 0
    for feed_url in FEEDS:
        try:
            print(f"Checking {feed_url}")
            feed = feedparser.parse(feed_url)
            for entry in feed.entries[:2]:
                text = f"🔥 <b>{entry.title}</b>\n\n🔗 {entry.link}\n\n#CentralJobs #TNJobs @IndiaJobAlertTamil"
                send(text)
                count += 1
                time.sleep(2)
        except Exception as e:
            print(f"Feed error {feed_url}: {e}")
    print(f"Done! Sent {count} jobs")
    if count == 0:
        send("✅ India Job Alert Bot is Live! Daily govt jobs will be posted here. #Test")

if __name__ == "__main__":
    check()
