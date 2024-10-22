from flask import Flask
import threading
from RADHIKA import LOGGER, AMBOT

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

def run_flask():
    app.run(host="0.0.0.0", port=8000)

def run_bot():
    LOGGER.info("RADHIKA ON.\n╔═════ஜ۩۞۩ஜ════╗\n  ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 𝗨𝗧𝗧𝗔𝗠 𝗥𝗔𝗧𝗛𝗢𝗥𝗘♨️\n╚═════ஜ۩۞۩ஜ════╝")
    AMBOT().run()

if __name__ == "__main__":
    # Create a thread for Flask server
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Run the bot in the main thread
    run_bot()
