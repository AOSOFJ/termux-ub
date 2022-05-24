from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID = input("Enter API_ID: ")
API_HASH = input("Enter API_HASH: ")

with TelegramClient(StringSession(),API_ID,API_HASH) as termuxUb:
  termuxUb.send_message("me",f"**This Is You Session:-**\n\n{termuxUb.session.save()}")
