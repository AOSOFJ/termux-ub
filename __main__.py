import os

e = "Lul Error"

def setup():
  os.system("pip install telethon")
  from telethon import TelegramClient 

setup()

API_ID = input("Enter API_ID: ")
API_HASH = input("Enter API_HASH: ")
SESSION = input("Enter SESSION: ")

try:
  user = TelegramClient(API_ID, API_HASH, SESSION)
except:
  print(f"Error: {e}")
