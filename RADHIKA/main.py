import logging
import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import BotCommand, Message
from pymongo import MongoClient

# Set up logging for simple output (Only info level)
logging.basicConfig(level=logging.INFO)

# Environment variables (ensure these are set correctly)
API_ID = os.environ.get("API_ID", "16457832")
API_HASH = os.environ.get("API_HASH", "3030874d0befdb5d05597deacc3e83ab")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7383809543:AAGaHCQb8b9C7-cB1fU5tlm3vrUFa8nj_wM")
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://teamdaxx123:teamdaxx123@cluster0.ysbpgcp.mongodb.net/?retryWrites=true&w=majority")

# MongoDB connection
try:
    client = MongoClient(MONGO_URL, connectTimeoutMS=30000, serverSelectionTimeoutMS=30000)
    client.server_info()  # Check if connection is successful
    logging.info("MongoDB connection successful!")
except Exception as e:
    logging.error(f"MongoDB connection error: {e}")
    exit()

# Initialize MongoDB collections
db = client["Word"]
chatai = db["WordDb"]
clonebotdb = db["CloneBotDb"]

# Initialize the bot client
RADHIKA = Client(
    "chat-gpt",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Define the anony_boot function that starts the bot and sets up the commands.
async def anony_boot():
    try:
        # Start the bot
        await RADHIKA.start()
        logging.info(f"Bot @{RADHIKA.me.username} started successfully.")
        
        # Set bot commands (Simple version with just basic commands)
        await RADHIKA.set_bot_commands([
            BotCommand("start", "Start the bot"),
            BotCommand("help", "Get the help menu"),
        ])
        logging.info("Bot commands set successfully.")
        
    except Exception as ex:
        logging.error(f"Error during bot startup: {ex}")
        return

    # Keep the bot running
    await RADHIKA.idle()

# Command handler for /start
@RADHIKA.on_message(filters.command("start") & filters.private)
async def start(client: Client, message: Message):
    # Send a simple reply for /start command
    await message.reply("Hii, I am Radhika Baby, How are you?")

# Command handler for /help
@RADHIKA.on_message(filters.command("help") & filters.private)
async def help(client: Client, message: Message):
    # Send a simple help message
    await message.reply("This is a bot that does X, Y, and Z.\nUse /start to begin!")

# Clone Bot Logic: /clone command
@RADHIKA.on_message(filters.command(["clone", "host", "deploy"]))
async def clone_txt(client, message: Message):
    if len(message.command) > 1:
        bot_token = message.command[1].strip()
        mi = await message.reply_text("Please wait while I check the bot token.")
        
        try:
            ai = Client(bot_token, API_ID, API_HASH, bot_token=bot_token)
            await ai.start()
            bot = await ai.get_me()
            bot_id = bot.id
            user_id = message.from_user.id
            
            details = {
                "bot_id": bot.id,
                "is_bot": True,
                "user_id": user_id,
                "name": bot.first_name,
                "token": bot_token,
                "username": bot.username,
            }
            # Insert clone details in the DB
            await clonebotdb.insert_one(details)
            await mi.edit_text(f"**Bot @{bot.username} has been successfully cloned ✅.**")
        except Exception as e:
            logging.exception("Error while cloning bot.")
            await mi.edit_text(f"⚠️ Error: {e}")
    else:
        await message.reply_text("**Provide Bot Token after /clone Command from @Botfather.**")

# List cloned bots: /cloned command
@RADHIKA.on_message(filters.command("cloned"))
async def list_cloned_bots(client, message: Message):
    try:
        cloned_bots = clonebotdb.find()
        cloned_bots_list = await cloned_bots.to_list(length=None)
        if not cloned_bots_list:
            await message.reply_text("No bots have been cloned yet.")
            return
        total_clones = len(cloned_bots_list)
        text = f"**Total Cloned Bots:** {total_clones}\n\n"
        for bot in cloned_bots_list:
            text += f"**Bot ID:** `{bot['bot_id']}`\n"
            text += f"**Bot Name:** {bot['name']}\n"
            text += f"**Bot Username:** @{bot['username']}\n\n"
        await message.reply_text(text)
    except Exception as e:
        logging.exception(e)
        await message.reply_text("**An error occurred while listing cloned bots.**")

# Delete cloned bot: /delclone command
@RADHIKA.on_message(filters.command(["deletecloned", "delcloned", "delclone", "deleteclone", "removeclone", "cancelclone"]))
async def delete_cloned_bot(client, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text("**⚠️ Please provide the bot token after the command.**")
            return

        bot_token = " ".join(message.command[1:])
        ok = await message.reply_text("**Checking the bot token...**")

        cloned_bot = await clonebotdb.find_one({"token": bot_token})
        if cloned_bot:
            await clonebotdb.delete_one({"token": bot_token})
            await ok.edit_text(
                "**🤖 your cloned bot has been disconnected from my server ☠️**\n**Clone by :- /clone**"
            )
        else:
            await message.reply_text("**⚠️ The provided bot token is not in the cloned list.**")
    except Exception as e:
        await message.reply_text(f"**An error occurred while deleting the cloned bot:** {e}")
        logging.exception(e)

# Delete all cloned bots: /delallclone command
@RADHIKA.on_message(filters.command("delallclone"))
async def delete_all_cloned_bots(client, message: Message):
    try:
        if message.from_user.id != OWNER_ID:
            await message.reply_text("**You don't have permission to delete all cloned bots.**")
            return

        a = await message.reply_text("**Deleting all cloned bots...**")
        await clonebotdb.delete_many({})
        await a.edit_text("**All cloned bots have been deleted successfully ✅**")
    except Exception as e:
        await a.edit_text(f"**An error occurred while deleting all cloned bots.** {e}")
        logging.exception(e)

# Non-private chats handler (both text and stickers)
@RADHIKA.on_message((filters.text | filters.sticker) & ~filters.private & ~filters.bot)
async def vickai(client: Client, message: Message):
    if not message.reply_to_message:
        vick = db["VickDb"]["Vick"]
        is_vick = vick.find_one({"chat_id": message.chat.id})

        if not is_vick:
            await RADHIKA.send_chat_action(message.chat.id, "typing")

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
        await RADHIKA.send_chat_action(message.chat.id, "typing")

        results = chatai.find({"word": message.text})
        results_list = [result for result in results]

        if results_list:
            result = random.choice(results_list)
            if result.get('check') == "sticker":
                await message.reply_sticker(result['text'])
            else:
                await message.reply_text(result['text'])

# Main entry point to run the bot
if __name__ == "__main__":
    try:
        logging.info("Starting bot...")
        asyncio.run(anony_boot())  # Run the bot asynchronously
    except Exception as e:
        logging.error(f"Failed to start the bot: {e}")
