import os
import asyncio
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@IndiaJobAlertTamil"

async def main():
    bot = Bot(token=TOKEN)
    await bot.send_message(
        chat_id=CHANNEL,
        text="✅ India Job Alert Bot is Live!\n\nDaily Govt & Private jobs varum da! Stay tuned 🔥"
    )
    print("Message sent!")

asyncio.run(main())
