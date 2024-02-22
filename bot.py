import telebot
import json
from config import TOKEN, MY_ID


token = TOKEN
bot = telebot.TeleBot(token=token, parse_mode="HTML")

# https://t.me/gingerOner_bot адресс в телеграм


# Функция сохранения информации о пользователе (словаре user_data) в файл json
def save_user_data(user_data):
    with open("user_data.json", "w", encoding='utf8') as file:
        json.dump(user_data, file, ensure_ascii=False, indent=2)


# Функция загрузки данных о пользователях из json файла в словарь user_data
def load_user_data():
    try:
        with open("user_data.json", "r+", encoding='utf8') as file:
            return json.load(file)
    except:
        return {}


# Проверяем наличие файла с данными пользователей и если он есть, то считываем из него значения в переменную user_data
try:
    file_with_json = open('user_data.json', 'r+', encoding='utf8')  # Открываем файл
    try:
        user_data_file = json.load(file_with_json)  # Считываем содержимое в словарь
        user_data = user_data_file # Если в файле есть записи данных о пользователях, то передаем их в словарь user_data
        print('Начальное значение user_data_file: ', user_data_file)
    except json.decoder.JSONDecodeError as err:
        user_data = {} # Изначально пользователей нет, пустой словарь
        print('Начальное значение user_data_file: пустой файл')
    file_with_json.close()  # Закрываем файл
except FileNotFoundError:
    user_data = {}
    print('Файл user_data.json ещё не создан!')


print('Начальное значение user_data:', user_data)


# Кнопки
#markup = ReplyKeyboardMarkup(resize_keyboard=True) # заготовка для клавиатуры
#markup.add(KeyboardButton('Первый текст на кнопочке')) # добавляем кнопку
#markup.add(KeyboardButton('Второй текст на кнопочке'))

@bot.message_handler(commands=['start'])
def hello_message(message): # Функция для обработки сообщений
    global user_data
    user_id = str(message.from_user.id)  # Получаем `user_id` пользователя, переводим в str, чтобы потом использовать в json формате

    # Запоминаем ползователей в словарь
    # Проверяем, что user_id пользователя есть в словаре
    # Если нет -- записываем
    if user_id in user_data:
        print(f"Пользователь {user_data[user_id]} есть в моей базе!")
    else:
        user_data[(user_id)] = {}
        print(f"Пользователя {user_id} нет в словаре")
        user_data[user_id]['user_name'] = message.from_user.username
        user_data[user_id]['user_firstname'] = message.from_user.first_name
        user_data[user_id]['user_lastname'] = message.from_user.last_name
        print(f"Отлично, я его {user_data[user_id]} запомнил!")
        # записываем данные user_data в файл в json формате
        file_for_json = open('user_data.json', 'w',
                             encoding='utf8')  # Открываем файл file_name.json на чтение и запись.При открытии указывается кодировка utf8
        json.dump(user_data, file_for_json, ensure_ascii=False,
                  indent=2)  # Записываем в него словарь в JSON-формате, разрешив нестандартные символы
        file_for_json.close()  # Закрываем файл

    print(f'Итоговый словарь: {user_data}')


    bot.send_photo(message.chat.id, photo=open('./foto/stiсker/ginger_eyes.jpg', 'rb'))
    bot.send_message(message.chat.id, "Привет!")
    bot.send_message(message.chat.id, f"Это тг-бот 🤖 граффити-художника <strong>Ginger(Имбирь)</strong>!\n"
                                        f"Я помогу тебе лучше узнать о Ginger'е и его творчестве!\n"
                                        f"Покажу и помогу выбрать наш мерч :)\n"
                                        f"Хочешь ознакомиться с командами бота? Пиши /help") # Отправка ответа

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "У меня есть команды:")
    bot.send_message(message.chat.id, "/clothes - посмотреть одежду, которую можно заказать")
#      bot.send_message(message.chat.id, "/whoisGinger - кто такой Ginger?")
    bot.send_message(message.chat.id, f"t.me/gingerOnertop - ссылка на наш канал <strong>Ginger(Имбирь)</strong>. Присоединяйся, чтобы быть в курсе всяких интересностей от Ginger'a!)))")
    bot.send_message(message.chat.id, "/streets - поймать трафик онлайн 😎")
    
@bot.message_handler(commands=['clothes'])
def clothes(message):
    for i in range(4):
        bot.send_photo(message.chat.id, photo=open(f'./foto/t-short/t-short_{i+1}.jpg', 'rb'))
    bot.send_message(message.chat.id, f"Футболка с логотипом <strong>'Имбирь'</strong> 👆🏻")
    bot.send_message(message.chat.id, "Для заказа пиши: @gingerOner или @Anathrom")  # Отправка ответа

@bot.message_handler(commands=['streets'])
def streets(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "А здесь куски улиц от Ginger'а"
                              "Фото обновляются после каждого покраса📸")
    bot.send_message(chat_id, "GOLD GINGER")
    bot.send_photo(chat_id, photo=open('./foto/graffities/goldginger.jpg', 'rb'))

# Обработчик получения ответа пользователя для получения данных пользователей
@bot.message_handler(commands=['data_user_me'])
def data_user(message):
    global user_data
    chat_id = MY_ID
    total_user = 0
    
    for id in user_data:
        total_user+=1
        bot.send_message(chat_id, f"<strong>{id}</strong>: \n"
                                  f"<i>user_name</i>:          {user_data[id]['user_name']}\n"
                                  f"<i>user_firstname</i>:   {user_data[id]['user_firstname']}\n"
                                  f"<i>user_lastname</i>:   {user_data[id]['user_lastname']}")
    bot.send_message(chat_id,f"<strong>Всего пользователей:</strong> {total_user}")

# telephon=message.contact.phone_number



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



bot.polling(non_stop=True)
