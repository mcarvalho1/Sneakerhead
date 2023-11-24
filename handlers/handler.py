import json
import logging
from telegram.ext import MessageHandler, filters
from utils.utils import format_friendly_message, format_news_message

CHANNEL_CHAT_ID = -1002100933699

async def send_product(update, context, text, caption):
    try:
        if text:
            product_info = text.split("\n")[1:]
        else:
            product_info = caption.split("\n")[1:]

        data = {
            "product_name": product_info[0].split(":")[1].strip(),
            "price": product_info[1].split(":")[1].strip(),
            "discount": product_info[2].split(":")[1].strip(),
            "percentage": product_info[3].split(":")[1].strip(),
            "link": ":".join(product_info[4].split(":")[1:]).strip(),
            "brand": product_info[5].split(":")[1].strip(),
            "model": product_info[6].split(":")[1].strip(),
            "type": product_info[7].split(":")[1].strip(),
            "genre": product_info[8].split(":")[1].strip(),
            "voucher": product_info[9].split(":")[1].strip(),
            "store": product_info[10].split(":")[1].strip(),
        }

        friendly_message = format_friendly_message(data)

        json_text = json.dumps(data, indent=2)

        if update.message.photo:
            photo = update.message.photo[-1]

            message_text = f"{friendly_message}\n"

            await context.bot.send_photo(chat_id=CHANNEL_CHAT_ID, photo=photo.file_id, caption=message_text)
        else:
            await context.bot.send_message(chat_id=CHANNEL_CHAT_ID, text=friendly_message, parse_mode='MarkdownV2')

    except Exception as e:
        print("Error:", str(e))

async def send_news(update, context, text, caption):
    try:
        if text:
            news_info = text.split("\n")[1:]
        else:
            news_info = caption.split("\n")[1:]

        news_data = {
            "news_title": news_info[0].split(":")[1].strip(),
            "news_subtitle": news_info[1].split(":")[1].strip(),
            "body": news_info[2].split(":")[1].strip(),
            "img_caption": news_info[3].split(":")[1].strip(),
            "link": ":".join(news_info[4].split(":")[1:]).strip(),
        }

        friendly_message = format_news_message(news_data)

        json_text = json.dumps(news_data, indent=2)

        if update.message.photo:
            photo = update.message.photo[-1]

            message_text = f"{friendly_message}\n"

            await context.bot.send_photo(chat_id=CHANNEL_CHAT_ID, photo=photo.file_id, caption=message_text)
        else:
            await context.bot.send_message(chat_id=CHANNEL_CHAT_ID, text=friendly_message, parse_mode='MarkdownV2')

    except Exception as e:
        print("Error:", str(e))

async def forward(update, context):
    text = update.message.text
    caption = update.message.caption
    has_product = text and text.startswith("BOT_ADD_PRODUCT") or (caption and caption.startswith("BOT_ADD_PRODUCT"))
    has_news = text and text.startswith("BOT_NEWS") or (caption and caption.startswith("BOT_NEWS"))

    if has_product:
        await send_product(update, context, text, caption)
    elif has_news:
        await send_news(update, context, text, caption)
    else:
        pass
