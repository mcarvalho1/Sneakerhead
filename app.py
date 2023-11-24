import json
import os
import random
from telegram import Bot
from telegram.ext import Application, MessageHandler, filters

TOKEN = os.environ.get("API_TOKEN")
GROUP_CHAT_ID = -1002024036980
CHANNEL_CHAT_ID = -1002100933699

async def forward_message(update, context):
    text = update.message.text
    
    if text.startswith("BOT_ADD_PRODUCT"):
        product_name, price, discount, percentage, link, brand, model, _type, genre, voucher, store  = text.split("\n")[1:]
        
        data = {
            "product_name": product_name.split(":")[1].strip(),
            "price": price.split(":")[1].strip(),
            "discount": discount.split(":")[1].strip(),
            "percentage": percentage.split(":")[1].strip(),
            "link": ":".join(link.split(":")[1:]).strip(),
            "brand": brand.split(":")[1].strip(),
            "model": model.split(":")[1].strip(),
            "type": _type.split(":")[1].strip(),
            "genre": genre.split(":")[1].strip(),
            "voucher": voucher.split(":")[1].strip(),
            "store": store.split(":")[1].strip(),
        }
        
        # Montar mensagem amigável
        friendly_message = format_friendly_message(data)
        
        # Converta a estrutura JSON para uma string
        json_text = json.dumps(data, indent=2)
        
        # Enviar a mensagem amigável para o canal
        await context.bot.send_message(chat_id=CHANNEL_CHAT_ID, text=friendly_message)
        
        # Enviar o JSON para o canal
        # await context.bot.send_message(chat_id=CHANNEL_CHAT_ID, text=json_text)

def format_friendly_message(data):
    titles = [
        "🚨 Super Promo: Baixou mais!",
        "🌟 Oferta Incrível: Não perca!",
        "🔥 Descontão do Dia: Imperdível!",
    ]

    sub_titles = [ 
        "⏰ É agora, ou nunca.",
        "⏰ Corre que ainda dá tempo.",
        "🤯 AGORA É A HORA!",
        "⚠️ Nesse valor esgota!",
    ]

    brands = [ 
        f"A {data['store']} surpreendeu todo mundo com os descontos incríveis desta temporada!",
        f"A {data['store']} não está para brincadeira e está arrasando com as ofertas imperdíveis!",
        f"A {data['store']} enlouqueceu com os preços baixos nesta liquidação!",
        f"A {data['store']} está dando um show de promoções que você não pode perder!",
     ]

    random_title = random.choice(titles)
    random_sub_titles = random.choice(sub_titles)
    random_brands = random.choice(brands)

    message = (
        f"{random_title}\n"
        f"{random_sub_titles}\n\n"
        f"{data['product_name']}\n"
        f"De R${data['price']} | Por R${data['discount']} "
        f"(Desconto de {data['percentage']}%)\n\n"
        f"Agora, na {data['store']}:\n"
        f"➡️ {data['link']}\n"
        f"{data['voucher']}\n"
        f"{random_brands}"
    )
    return message

def main():
    bot = Bot(token=TOKEN)
    application = Application.builder().token(TOKEN).build()

    application.add_handler(MessageHandler(filters.TEXT & filters.Chat(chat_id=GROUP_CHAT_ID), forward_message))

    application.run_polling(1.0)

if __name__ == '__main__':
    main()
