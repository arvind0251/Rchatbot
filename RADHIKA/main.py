from pyrogram import Client, filters
from pyrogram.types import *
from pyrogram.enums import ChatAction
from pymongo import MongoClient
from flask import Flask
import threading
import random
import os
import time
from datetime import datetime
import requests

# Environment variables
API_ID = os.environ.get("API_ID", "16457832")
API_HASH = os.environ.get("API_HASH", "3030874d0befdb5d05597deacc3e83ab")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7242058454:AAH24Hp_LNk-QO422ERYmySTnrUn3rYn5A8")
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://TEAMBABY01:UTTAMRATHORE09@cluster0.vmjl9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# MongoDB connection
client = MongoClient(MONGO_URL, connectTimeoutMS=30000, serverSelectionTimeoutMS=30000)
db = client["Word"]
chatai = db["WordDb"]

BOT_NAME = os.environ.get("BOT_NAME", "🐰⃟⃞⍣Rᴀᴅʜɪᴋᴀ❥")

RADHIKA = Client(
    "chat-gpt",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Start command handler for private chats
@RADHIKA.on_message(filters.command("start") & filters.private)
async def start(client: Client, message: Message):
    keyboard = [
        [
            InlineKeyboardButton("Join 🤒", url="https://t.me/BABY09_WORLD")
        ]
    ]
    await message.reply(
        "Hii, I am Radhika Baby, How are you?",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# Non-private chats handler (both text and stickers)
@RADHIKA.on_message((filters.text | filters.sticker) & ~filters.private & ~filters.bot)
async def vickai(client: Client, message: Message):
    if not message.reply_to_message:
        vick = db["VickDb"]["Vick"]
        is_vick = vick.find_one({"chat_id": message.chat.id})

        if not is_vick:
            await RADHIKA.send_chat_action(message.chat.id, ChatAction.TYPING)

            results = chatai.find({"word": message.text})
            results_list = [result for result in results]

            if results_list:
                result = random.choice(results_list)
                if result.get('check') == "sticker":
                    await message.reply_sticker(result['text'])
                else:
                    await message.reply_text(result['text'])

# Private chats handler (both text and stickers)
@RADHIKA.on_message((filters.text | filters.sticker) & filters.private & ~filters.bot)
async def vickprivate(client: Client, message: Message):
    if not message.reply_to_message:
        await RADHIKA.send_chat_action(message.chat.id, ChatAction.TYPING)

        results = chatai.find({"word": message.text})
        results_list = [result for result in results]

        if results_list:
            result = random.choice(results_list)
            if result.get('check') == "sticker":
                await message.reply_sticker(result['text'])
            else:
                await message.reply_text(result['text'])

# Flask Web Server (for keep-alive)
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

# Flask ko alag thread mein run karne ka function
def run_flask():
    app.run(host="0.0.0.0", port=8000)

# Keep-alive function jo periodic ping bhejta hai
def keep_alive():
    while True:
        try:
            # Apne Render app ya kisi bhi remote URL ko ping karein
            requests.get("https://satya-userbot.onrender.com")
        except Exception as e:
            print(f"Ping error: {e}")
        time.sleep(300)  # Har 5 minute mein ping bhejna

# Bot ko run karne ka function
def run_bot():
    print(f"{BOT_NAME} ɪs ᴀʟɪᴠᴇ!")
    RADHIKA.run()

if __name__ == "__main__":
    # Flask server ko alag thread mein run karna
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Keep-alive function ko alag thread mein run karna
    keep_alive_thread = threading.Thread(target=keep_alive)
    keep_alive_thread.daemon = True
    keep_alive_thread.start()

    # Bot ko main thread mein run karna
    run_bot()
    
