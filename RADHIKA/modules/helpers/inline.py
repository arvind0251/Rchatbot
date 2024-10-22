from pyrogram.types import InlineKeyboardButton

DEV_OP = [
    [
        InlineKeyboardButton(
            text="˹ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ˼",
            url=f"https://t.me/BABY_MUSIC09_BOT?startgroup=true",  # MUSIC link inserted
        ),
    ],
    [
        InlineKeyboardButton(text="˹ ᴏᴡɴᴇʀ ˼", user_id=7403621976),  # OWNER_ID directly
        InlineKeyboardButton(text="˹ ʜᴇʟᴘ & ᴄᴍᴅs ˼", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="˹ ᴍᴜsɪᴄ ˼", url="https://t.me/BABY_MUSIC09_BOT"),  # MUSIC link
        InlineKeyboardButton(text="˹ ʀᴇᴘᴏ ˼", url="https://github.com/BABY-MUSIC/RADHIKA"),  # REPO link
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="˹ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ˼",
            url=f"https://t.me/BABY_MUSIC09_BOT?startgroup=true",  # MUSIC link
        ),
    ],
    [
        InlineKeyboardButton(
            text="˹ ᴄʟᴏsᴇ ˼",
            callback_data="CLOSE",
        ),
    ],
]

BACK = [
    [
        InlineKeyboardButton(text="◁", callback_data="BACK"),
    ],
]

HELP_BTN = [
    [
        InlineKeyboardButton(text="˹ ᴄʜᴀᴛʙᴏᴛ ˼", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="˹ ᴛᴏᴏʟs ˼", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text="◁", callback_data="BACK"),
        InlineKeyboardButton(text="˹ ᴄʟᴏsᴇ ˼", callback_data="CLOSE"),
    ],
]

CLOSE_BTN = [
    [
        InlineKeyboardButton(text="˹ ᴄʟᴏsᴇ ˼", callback_data="CLOSE"),
    ],
]

CHATBOT_ON = [
    [
        InlineKeyboardButton(text="˹ ᴇɴᴀʙʟᴇ ˼", callback_data="addchat"),
        InlineKeyboardButton(text="˹ ᴅɪsᴀʙʟᴇ ˼", callback_data="rmchat"),
    ],
]

MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="sᴏᴏɴ..", callback_data="soom"),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text="◁", callback_data="SBACK"),
        InlineKeyboardButton(text="˹ ᴄʟᴏsᴇ ˼", callback_data="CLOSE"),
    ],
]

CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="◁", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="˹ ᴄʟᴏsᴇ ˼", callback_data="CLOSE"),
    ],
]

HELP_START = [
    [
        InlineKeyboardButton(text="˹ ʜᴇʟᴘ ˼", callback_data="HELP"),
        InlineKeyboardButton(text="˹ ᴄʟᴏsᴇ ˼", callback_data="CLOSE"),
    ],
]

HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="˹ ʜᴇʟᴘ ˼", url=f"https://t.me/BABY_MUSIC09_BOT?start=help"  # BOT_USERNAME link
        ),
        InlineKeyboardButton(text="˹ ᴄʟᴏsᴇ ˼", callback_data="CLOSE"),
    ],
]

ABOUT_BTN = [
    [
        InlineKeyboardButton(text="˹ sᴜᴘᴘᴏʀᴛ ˼", url="https://t.me/OL6jdTL7JAJjYzVl"),  # SUPPORT_GRP link
        InlineKeyboardButton(text="˹ ʜᴇʟᴘ ˼", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="˹ ᴏᴡɴᴇʀ ˼", user_id=7403621976),  # OWNER_ID directly
        InlineKeyboardButton(text="˹ sᴏᴜʀᴄᴇ ˼", callback_data="SOURCE"),
    ],
    [
        InlineKeyboardButton(text="˹ ᴜᴘᴅᴀᴛᴇs ˼", url="https://t.me/BABY09_WORLD"),  # UPDATE_CHNL link
        InlineKeyboardButton(text="◁", callback_data="BACK"),
    ],
]
