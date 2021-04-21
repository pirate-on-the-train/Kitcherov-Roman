import vk_api, config
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token=config.token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def sender(id, text):
    vk.messages.send(user_id = id, message = text, random_id = 0, keyboard = open('keyboard.json', 'r', encoding="UTF-8").read())

def sender_sticker(id, number):
    vk.messages.send(user_id = id, sticker_id = number, random_id = 0)

def sender_photo(id, url):
    vk.messages.send(user_id = id, attachment = url, random_id = 0)

for event in longpoll.listen():                             # Прослушиваем все события в longpoll
    if event.type == VkEventType.MESSAGE_NEW:               # Если тип события "Новое сообщение"
        if event.to_me:                                     # Если сообщение адресовано нам
            msg = event.text.lower()                        # Переводим полученное сообщение в нижний регистр
            id = event.user_id                              # Сохраняем id пользователя в переменной id
            if msg == 'привет':                             # Если сообщение "привет"
                sender(id, 'Привет, я бот!')                # Вызываем метод sender, в который передаём id пользователя и что бот должен ответить
                sender_sticker(id, 67)                      # Вызываем метод sender_sticker, в который передаём id пользователя и id стикера
                sender_photo(id, 'photo63475836_457252307') # Вызываем метод sender_photo, в который передаём id пользователя и id фото
            if msg == 'здравствуйте':                       # Если сообщение "привет"
                sender(id, 'Добрый день!')                  # Вызываем метод sender, в который передаём id пользователя и что бот должен ответить