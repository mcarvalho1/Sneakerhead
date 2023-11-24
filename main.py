from telegram import Bot
from telegram.ext import Application, MessageHandler, filters
from handlers.handler import forward

import os

TOKEN = os.environ.get("API_TOKEN")
GROUP_CHAT_ID = -1002024036980
CHANNEL_CHAT_ID = -1002100933699

def main():
    bot = Bot(token=TOKEN)
    application = Application.builder().token(TOKEN).build()

    application.add_handler(MessageHandler(filters.TEXT & filters.Chat(chat_id=GROUP_CHAT_ID), forward))
    application.add_handler(MessageHandler(filters.PHOTO & filters.Chat(chat_id=GROUP_CHAT_ID), forward))

    application.run_polling(1.0)

if __name__ == '__main__':
    main()
