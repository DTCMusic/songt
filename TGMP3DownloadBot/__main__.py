# TG_MP3_Download_Bot

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from TGMP3DownloadBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from TGMP3DownloadBot import MP3DownloadBot as app
from TGMP3DownloadBot import LOGGER

pm_start_text = """
 🎧 Telegram Mahnı Yükləmə Botu 🎧
Salam [{}](tg://user?id={}) 👋 Mən Telegram manhi  yükləyən Botu 🎧

⚫ İstədiyiniz Mahnını MP3 şəklində yükləyə bilərsiz✨: `/song upamawak `

⚪ 𝐍𝐮̈𝐦𝐮𝐧𝐞: /song zawanbeatsz

~ 🛠️ 𝑺𝒖𝒑𝒑𝒐𝒓𝒕 @SOQrup  
"""


@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                    [
                        InlineKeyboardButton(
                             text=" 🛠️ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐂𝐡𝐚𝐭 ",
                             url="https://t.me/SOQrup"),
                         InlineKeyboardButton(
                             text=" 🔔 𝐘𝐞𝐧𝐢𝐥𝐢𝐤𝐥𝐞𝐫 𝐊𝐚𝐧𝐚𝐥ı ",
                             url="https://t.me/ledyplaylist")
                    ],
                    [
                        InlineKeyboardButton(
                             text="👨‍💻 𝐒𝐚𝐡𝐢𝐛 ",
                             url="https://t.me/Tenha055"),
                         InlineKeyboardButton(
                             text=" 𝐌𝐮𝐬𝐢𝐜 𝐏𝐥𝐚𝐲𝐞𝐫 ",
                             url="https://t.me/musicplayerasistant_bot")
                    ],
                    [
                        InlineKeyboardButton(
                            text=" ⚜️ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 ",
                             url="https://t.me/ruzgar_alican") 
                    
                    ]
            ]
        ),
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


app.start()
LOGGER.info("TG Song  Download Bot is online 👨‍💻 .")
idle()
