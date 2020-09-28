import telebot
print("Бот запущен")
token = "1353842327:AAGPs6jgnTg7aQvwGvC9YqN1M_qU5kQDEPQ"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id,"Добро пожаловать,Создатель!!!")

@bot.message_handler(content_types=["text"])
def send_messages(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id,"Привет,Создатель!")
    elif message.text.lower() == "как дела":
        bot.send_message(message.chat.id, "пока не жалуюсь,сам как?")
    elif message.text.lower() == "отлично":
        bot.send_message(message.chat.id, "Завидую!")
    elif message.text.lower() == "хорошо":
        bot.send_message(message.chat.id, "Почему не отлично,ты же человек!")
    elif message.text.lower() == "кто лучший в мобле":
        bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAMVX3HkOo7X_Pw4ArQODlKZlrjS5lEAAggAA3j6-xc5Pgkkb_WMKxsE")
    elif message.text.lower() == "прикинь заказали фач на фольге":
        bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAMcX3Hlv_nrV6bCUMbTsWJu-7s8WuQAAqoJAAJ5XOIJVtUc2PayTC8bBA")
    elif message.text.lower() == "что ты умеешь":
        bot.send_message(message.chat.id, "да много чего,спроси что хочешь")
    elif message.text.lower() == "можешь найти фильм какой нибудь":
        bot.send_message(message.chat.id, "да без проблемб,что нравится")
        bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAMjX3HnvbCs1DvcYER8nf2lF-QdFZMAAqQJAAJ5XOIJFjblYY-cdjsbBA")
    elif message.text.lower() == "что нибудь из марвел":
        bot.send_message(message.chat.id, "лови ссылку")
        bot.send_message(message.chat.id, "https://oc.kg/?s=4&v=s#/catalog/selection/4/page/1")
        bot.send_message(message.chat.id, "Приятного просмотра")
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAM0X3HqQigyXeAZe0c6sRckmYx-qzMAAkABAAKKEqoOhS62MJr28F8bBA")


@bot.message_handler(content_types=["sticker"])
def send_sticker(message):
    print(message)


bot.polling()