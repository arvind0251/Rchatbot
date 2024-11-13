from pyrogram import Client, filters
from pyrogram.types import *
from pyrogram.enums import ChatAction
from pymongo import MongoClient
import random
import os
import time
from datetime import datetime

API_ID = os.environ.get("API_ID", "16457832") 
API_HASH = os.environ.get("API_HASH", "3030874d0befdb5d05597deacc3e83ab") 
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7242058454:AAH24Hp_LNk-QO422ERYmySTnrUn3rYn5A8") 
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://TEAMBABY01:UTTAMRATHORE09@cluster0.vmjl9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# MongoDB connection
client = MongoClient(MONGO_URL, connectTimeoutMS=30000, serverSelectionTimeoutMS=30000)

BOT_USERNAME = os.environ.get("BOT_USERNAME", "RADHIKA_CHAT_RROBOT") 
UPDATE_CHNL = os.environ.get("UPDATE_CHNL", "BABY09_WORLD")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "UTTAM470")
SUPPORT_GRP = os.environ.get("SUPPORT_GRP", "+OL6jdTL7JAJjYzVl")
BOT_NAME = os.environ.get("BOT_NAME", "🐰⃟⃞⍣Rᴀᴅʜɪᴋᴀ❥")
START_IMG = os.environ.get("START_IMG", "https://files.catbox.moe/5dp75k.jpg")
CHANNEL_IMG = os.environ.get("CHANNEL_IMG", "https://files.catbox.moe/3ni0t3.jpg")
STKR = os.environ.get("STKR", "CAACAgEAAx0Cd5L74gAClqVmhNlbqSgKMe5TIswcgft9l6uSpgACEQMAAlEpDTnGkK-OP8PZpzUE")

StartTime = time.time()

# Initialize bot client
RADHIKA = Client(
    "chat-gpt",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@RADHIKA.on_message(
    (filters.text | filters.sticker) & ~filters.private & ~filters.bot,
)
async def vickai(client: Client, message: Message):
    chatdb = MongoClient(MONGO_URL)
    chatai = chatdb["Word"]["WordDb"]   

    if not message.reply_to_message:
        vickdb = MongoClient(MONGO_URL)
        vick = vickdb["VickDb"]["Vick"] 
        is_vick = vick.find_one({"chat_id": message.chat.id})
        if not is_vick:
            await RADHIKA.send_chat_action(message.chat.id, ChatAction.TYPING)
            K = []  
            is_chat = chatai.find({"word": message.text})  
            k = chatai.find_one({"word": message.text})      
            if k:               
                for x in is_chat:
                    K.append(x['text'])          
                hey = random.choice(K)
                is_text = chatai.find_one({"text": hey})
                Yo = is_text['check']
                if Yo == "sticker":
                    await message.reply_sticker(f"{hey}")
                if not Yo == "sticker":
                    await message.reply_text(f"{hey}")

    if message.reply_to_message:  
        vickdb = MongoClient(MONGO_URL)
        vick = vickdb["VickDb"]["Vick"] 
        is_vick = vick.find_one({"chat_id": message.chat.id})    
        getme = await RADHIKA.get_me()
        bot_id = getme.id                             
        if message.reply_to_message.from_user.id == bot_id: 
            if not is_vick:                   
                await RADHIKA.send_chat_action(message.chat.id, ChatAction.TYPING)
                K = []  
                is_chat = chatai.find({"word": message.text})
                k = chatai.find_one({"word": message.text})      
                if k:       
                    for x in is_chat:
                        K.append(x['text'])
                    hey = random.choice(K)
                    is_text = chatai.find_one({"text": hey})
                    Yo = is_text['check']
                    if Yo == "sticker":
                        await message.reply_sticker(f"{hey}")
                    if not Yo == "sticker":
                        await message.reply_text(f"{hey}")
        if not message.reply_to_message.from_user.id == bot_id:          
            if message.sticker:
                is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
                if not is_chat:
                    chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
            if message.text:                 
                is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
                if not is_chat:
                    chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})

# Other handlers omitted for brevity...

print(f"{BOT_NAME} ɪs ᴀʟɪᴠᴇ!")      
RADHIKA.run()
