import telebot
from config import TOKEN

token= TOKEN
bot = telebot.TeleBot(token=token)

# https://t.me/gingerOner_bot адресс в телеграм

@bot.message_handler(commands=['start'])
def hello_message(message): # Функция для обработки сообщений
      bot.send_photo(message.chat.id, photo=open('./foto/stiсker/ginger_eyes.jpg', 'rb'))
      bot.send_message(message.chat.id, "Привет!")
      bot.send_message(message.chat.id, f"Это тг-бот 🤖 граффити-художника Ginger(Имбирь)!\n"
                                        f"Я помогу тебе лучше узнать о Ginger'е и его творчестве!\n"
                                        f"Покажу и помогу выбрать наш мерч :)\n"
                                        f"Хочешь ознакомиться с командами бота? Пиши /help") # Отправка ответа

@bot.message_handler(commands=['help'])
def help(message):
      bot.send_message(message.chat.id, "У меня есть команды:")
      bot.send_message(message.chat.id, "/clothes - посмотреть одежду, которую можно заказать")
#      bot.send_message(message.chat.id, "/whoisGinger - кто такой Ginger?")
      bot.send_message(message.chat.id, "t.me/gingerOnertop - ссылка на наш канал Ginger(Имбирь). Присоединяйся, чтобы быть в курсе всяких интересностей от Ginger'a!)))")

@bot.message_handler(commands=['clothes'])
def clothes(message):
      for i in range(4):
        bot.send_photo(message.chat.id, photo=open(f'./foto/t-short/t-short_{i+1}.jpg', 'rb'))
      bot.send_message(message.chat.id, "Футболка с логотипом 'Имбирь' 👆🏻")
      bot.send_message(message.chat.id, "Для заказа пиши: @gingerOner или @Anathrom")  # Отправка ответа

@bot.message_handler(content_types=['text', 'audio', 'foto'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "привет":
        bot.send_message(chat_id, "Это тг-бот граффити-художника Ginger(Имбирь)! Я помогу тебе выбрать наш мерч :) Хочешь ознакомиться с командами бота? Пиши /help")
    elif text == "как дела?" or text == "как дела":
        bot.send_message(chat_id, "Хорошо, спасибо!")
    else:
        bot.send_message(chat_id, "Простите, я Ваc не понял :( Я умею выполнять только определённые команды! Хочешь ознакомиться с командами бота? Пиши /help")

bot.polling()