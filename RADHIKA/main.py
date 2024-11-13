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

# Environment variables
API_ID = os.environ.get("API_ID", "16457832")
API_HASH = os.environ.get("API_HASH", "3030874d0befdb5d05597deacc3e83ab")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7242058454:AAH24Hp_LNk-QO422ERYmySTnrUn3rYn5A8")
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://TEAMBABY01:UTTAMRATHORE09@cluster0.vmjl9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# MongoDB connection
client = MongoClient(MONGO_URL, connectTimeoutMS=30000, serverSelectionTimeoutMS=30000)
db = client["Word"]
chatai = db["WordDb"]

# Bot and user details
BOT_USERNAME = os.environ.get("BOT_USERNAME", "RADHIKA_CHAT_RROBOT")
UPDATE_CHNL = os.environ.get("UPDATE_CHNL", "BABY09_WORLD")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "UTTAM470")
SUPPORT_GRP = os.environ.get("SUPPORT_GRP", "+OL6jdTL7JAJjYzVl")
BOT_NAME = os.environ.get("BOT_NAME", "🐰⃟⃞⍣Rᴀᴅʜɪᴋᴀ❥")
START_IMG = os.environ.get("START_IMG", "https://files.catbox.moe/5dp75k.jpg")
CHANNEL_IMG = os.environ.get("CHANNEL_IMG", "https://files.catbox.moe/3ni0t3.jpg")
STKR = os.environ.get("STKR", "CAACAgEAAx0Cd5L74gAClqVmhNlbqSgKMe5TIswcgft9l6uSpgACEQMAAlEpDTnGkK-OP8PZpzUE")

# Initialize bot client
RADHIKA = Client(
    "chat-gpt",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Start command handler for private chats
@RADHIKA.on_message(filters.command("start") & filters.private)
async def start(client: Client, message: Message):
    # Send message with a button
    keyboard = [
        [
            InlineKeyboardButton("Join 🤒", url="https://t.me/BABY09_WORLD")
        ]
    ]
    await message.reply(
        "Hii, I am Radhika Baby, How are you?",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# Handler for non-private chats (both text and stickers)
@RADHIKA.on_message((filters.text | filters.sticker) & ~filters.private & ~filters.bot)
async def vickai(client: Client, message: Message):
    if not message.reply_to_message:
        vick = db["VickDb"]["Vick"]
        is_vick = vick.find_one({"chat_id": message.chat.id})

        if not is_vick:
            await RADHIKA.send_chat_action(message.chat.id, ChatAction.TYPING)

            # Fetch all matching results for the word
            results = chatai.find({"word": message.text})

            # Ensure that `results` is converted correctly to a list
            # Instead of using `list()`, use a list comprehension
            results_list = [result for result in results]

            if results_list:
                # Randomize the response from the results
                result = random.choice(results_list)
                if result.get('check') == "sticker":
                    await message.reply_sticker(result['text'])
                else:
                    await message.reply_text(result['text'])

# Handler for private chats (both text and stickers)
@RADHIKA.on_message((filters.text | filters.sticker) & filters.private & ~filters.bot)
async def vickprivate(client: Client, message: Message):
    if not message.reply_to_message:
        await RADHIKA.send_chat_action(message.chat.id, ChatAction.TYPING)

        # Fetch all matching results for the word
        results = chatai.find({"word": message.text})

        # Ensure that `results` is converted correctly to a list
        # Instead of using `list()`, use a list comprehension
        results_list = [result for result in results]

        if results_list:
            # Randomize the response from the results
            result = random.choice(results_list)
            if result.get('check') == "sticker":
                await message.reply_sticker(result['text'])
            else:
                await message.reply_text(result['text'])

# Flask web server (to keep the bot alive)
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

def run_flask():
    app.run(host="0.0.0.0", port=8000)

def run_bot():
    print(f"{BOT_NAME} ɪs ᴀʟɪᴠᴇ!")
    RADHIKA.run()

if __name__ == "__main__":
    # Create a thread for Flask server
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Run the bot in the main thread
    run_bot()
    
