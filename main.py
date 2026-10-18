import os, asyncio, datetime
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@IndiaJobAlertTamil"

CATEGORIES = [
    {"cat": "TNPSC", "emoji": "📚", "title": "TNPSC Group 4 & Group 2 Recruitment", "link": "https://www.tnpsc.gov.in/"},
    {"cat": "UPSC", "emoji": "🏛️", "title": "UPSC Civil Services 2026", "link": "https://www.upsc.gov.in/"},
    {"cat": "SSC", "emoji": "📝", "title": "SSC CGL & CHSL 2026 Notification", "link": "https://ssc.nic.in/"},
    {"cat": "Railway Jobs", "emoji": "🚂", "title": "Railway RRB NTPC & Group D", "link": "https://indianrailways.gov.in/"},
    {"cat": "Bank Jobs", "emoji": "🏦", "title": "IBPS PO / Clerk & SBI Recruitment", "link": "https://www.ibps.in/"},
    {"cat": "Defence", "emoji": "🪖", "title": "Indian Army & Navy Agniveer", "link": "https://joinindianarmy.nic.in/"},
    {"cat": "Police Jobs", "emoji": "👮", "title": "TNUSRB Police Constable & SI", "link": "https://tnusrb.tn.gov.in/"},
    {"cat": "Teaching", "emoji": "👩‍🏫", "title": "TRB & TET Teachers Recruitment", "link": "https://trb.tn.gov.in/"},
    {"cat": "Engineering", "emoji": "⚙️", "title": "TNEB & ISRO Engineer Vacancy", "link": "https://www.tnebnet.org/"},
    {"cat": "IT Jobs", "emoji": "💻", "title": "TCS, Infosys & Wipro IT Jobs", "link": "https://www.naukri.com/it-jobs"},
    {"cat": "TN Govt", "emoji": "🏢", "title": "Tamil Nadu Govt Jobs Today", "link": "https://www.tn.gov.in/"},
    {"cat": "Central Govt", "emoji": "🇮🇳", "title": "Central Govt Jobs All India", "link": "https://www.india.gov.in/"},
    {"cat": "10th Pass", "emoji": "✅", "title": "10th Pass Govt Jobs", "link": "https://www.tnpsc.gov.in/"},
    {"cat": "12th Pass", "emoji": "✅", "title": "12th Pass Railway & SSC Jobs", "link": "https://ssc.nic.in/"},
    {"cat": "Degree Jobs", "emoji": "🎓", "title": "Degree Holders Govt Jobs", "link": "https://www.tnpsc.gov.in/"},
    {"cat": "Work From Home", "emoji": "🏠", "title": "WFH Jobs for Freshers", "link": "https://www.naukri.com/wfh-jobs"},
    {"cat": "Private Jobs", "emoji": "💼", "title": "Private Company Jobs Chennai", "link": "https://www.naukri.com/"},
    {"cat": "Fresher Jobs", "emoji": "🆕", "title": "Fresher Jobs 2026 Tamil Nadu", "link": "https://www.freshersworld.com/"},
    {"cat": "Medical", "emoji": "🏥", "title": "TN Medical & Nurse Recruitment", "link": "https://www.tn.gov.in/"},
    {"cat": "Office Jobs", "emoji": "🖥️", "title": "Office Assistant & Clerk Jobs", "link": "https://www.naukri.com/"},
    {"cat": "Part Time", "emoji": "⏰", "title": "Part Time Evening Jobs", "link": "https://www.indeed.co.in/"},
    {"cat": "Abroad Jobs", "emoji": "✈️", "title": "Gulf & Abroad Jobs for Indians", "link": "https://www.naukri.com/abroad-jobs"},
]

async def main():
    bot = Bot(token=TOKEN)
    hour = datetime.datetime.now().hour
    job = CATEGORIES[hour % 22]
    
    msg = f"""{job['emoji']} **{job['title']}** {job['emoji']}
**Category: {job['cat']}**

📌 **வேலை இடம்:** தமிழ்நாடு / இந்தியா முழுவதும்
📌 **கல்வித் தகுதி:** {job['cat']} தகுதிக்கேற்ப
📌 **வயது:** 18 - 40 வரை
📌 **சம்பளம்:** ₹18,000 - ₹65,000

🎯 **யார் Apply பண்ணலாம்?**
✅ 10th / 12th / Degree

⚠️ அதிகாரப்பூர்வ அறிவிப்பை பார்த்து Apply பண்ணுங்க!

👇 **கீழே உள்ள Button-ஐ Click பண்ணி Apply பண்ணுங்க**
"""
    keyboard = [
        [InlineKeyboardButton(f"🔗 {job['cat']} Apply Now", url=job['link'])],
        [InlineKeyboardButton("📢 Join Our Channel", url="https://t.me/IndiaJobAlertTamil")]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    
    await bot.send_message(chat_id=CHANNEL, text=msg, reply_markup=markup, parse_mode="Markdown")
    print(f"Posted with Button: {job['cat']}")

asyncio.run(main())
