from pyrogram import idle
from kisan import config
from kisan import app


# pyrogram client
app = client(
          "banall",
          api_id=API_ID,
          api_hash=API_HASH,
          bot_token=BOT_TOKEN,
)

app.start()
print("Bot Booted Successfully")
idle()
