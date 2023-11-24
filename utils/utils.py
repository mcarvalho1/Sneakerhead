import random

def escape_markdown_special_characters(text):
    special_characters = ['-', '.', '*', '_', '`', '[', ']', '(', ')', '{', '}', '#', '+', '!', '|']
    for char in special_characters:
        text = text.replace(char, fr'\{char}')
    return text

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
        f"De R${data['price']} | Por R${data['discount']}"
        f"(Desconto de {data['percentage']}%)\n\n"
        f"Agora, na {data['store']}:\n"
        f"➡️ {data['link']}\n"
        f"{data['voucher']}\n"
        f"{random_brands}"
    )
    return message

def format_news_message(data):
    news_title = escape_markdown_special_characters(data['news_title'])
    news_subtitle = escape_markdown_special_characters(data['news_subtitle'])
    body = escape_markdown_special_characters(data['body'])
    link = escape_markdown_special_characters(data['link'])

    message = (
        f"*{news_title}*\n"
        f'_{news_subtitle}_\n\n'
        f'{body}\n\n'
        f"*Leia mais:* {link}\n"
    )
    return message



