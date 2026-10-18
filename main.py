import os, asyncio, datetime, random
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@IndiaJobAlertTamil"

# 22 CATEGORY - HOURLY ROTATE
CATEGORIES = [
    {"cat": "TNPSC", "emoji": "📚", "link": "https://www.tnpsc.gov.in/"},
    {"cat": "UPSC", "emoji": "🏛️", "link": "https://www.upsc.gov.in/"},
    {"cat": "SSC", "emoji": "📝", "link": "https://ssc.nic.in/"},
    {"cat": "Railway Jobs", "emoji": "🚂", "link": "https://indianrailways.gov.in/"},
    {"cat": "Bank Jobs", "emoji": "🏦", "link": "https://www.ibps.in/"},
    {"cat": "Defence / Army", "emoji": "🪖", "link": "https://joinindianarmy.nic.in/"},
    {"cat": "Police Jobs", "emoji": "👮", "link": "https://tnusrb.tn.gov.in/"},
    {"cat": "Teaching Jobs", "emoji": "👩‍🏫", "link": "https://www.tn.gov.in/"},
    {"cat": "Engineering", "emoji": "⚙️", "link": "https://www.tnpsc.gov.in/"},
    {"cat": "IT / Software", "emoji": "💻", "link": "https://www.tcs.com/careers"},
    {"cat": "TN Govt Jobs", "emoji": "🏢", "link": "https://www.tn.gov.in/"},
    {"cat": "Central Govt", "emoji": "🇮🇳", "link": "https://www.india.gov.in/"},
    {"cat": "10th Pass Jobs", "emoji": "✅", "link": "https://www.tnpsc.gov.in/"},
    {"cat": "12th Pass Jobs", "emoji": "✅", "link": "https://ssc.nic.in/"},
    {"cat": "Degree Jobs", "emoji": "🎓", "link": "https://www.tnpsc.gov.in/"},
    {"cat": "Work From Home", "emoji": "🏠", "link": "https://www.naukri.com/wfh-jobs"},
    {"cat": "Private Jobs", "emoji": "💼", "link": "https://www.naukri.com/"},
    {"cat": "Fresher Jobs", "emoji": "🆕", "link": "https://www.freshersworld.com/"},
    {"cat": "Medical / Nurse", "emoji": "🏥", "link": "https://www.tn.gov.in/"},
    {"cat": "Office Jobs", "emoji": "🖥️", "link": "https://www.naukri.com/"},
    {"cat": "Part Time Jobs", "emoji": "⏰", "link": "https://www.indeed.co.in/"},
    {"cat": "Abroad Jobs", "emoji": "✈️", "link": "https://www.naukri.com/abroad-jobs"},
]

async def main():
    bot = Bot(token=TOKEN)
    now = datetime.datetime.now()
    hour = now.hour
    # Hour vachu category pick pannum
    job = CATEGORIES[hour % 22]
    
    msg = f"""{job['emoji']} **{job['cat']} Latest Vacancy 2026** {job['emoji']}

📌 வேலை இடம்: தமிழ்நாடு / இந்தியா முழுவதும்
📌 கல்வித் தகுதி: {job['cat']} பொறுத்து மாறுபடும்
📌 வயது வரம்பு: பதவியைப் பொறுத்து மாறுபடும்
📌 விண்ணப்பக் கடைசி தேதி: விரைவில் அறிவிக்கப்படும்

🎯 யாரெல்லாம் Apply பண்ணலாம்?
✅ 10th Pass
✅ 12th Pass
✅ Degree முடித்தவர்கள்

⚠️ குறிப்பு: அதிகாரப்பூர்வ அறிவிப்பைப் பார்த்துத் தகுதியை உறுதிப்படுத்தவும்.

🔗 Apply Link: {job['link']}

📢 Job Updates பெற நம்ம Channel-ஐ Join பண்ணுங்க!
👉 @IndiaJobAlertTamil
🔥 JobSpark India 🇮🇳 Your Dream Job Starts Here!
"""
    await bot.send_message(chat_id=CHANNEL, text=msg)
    print(f"Posted: {job['cat']} - Hour {hour}")

asyncio.run(main())
