from selenium import webdriver                                          # Подключение модуля webdriver для работы с браузером
from selenium.webdriver.common.keys import Keys                         # Подключение модуля Keys для работы с клавиатурой
from config import username, password                                   # Подключение переменных username и password из модуля config
import time, random                                                     # Подключение модулей random и time

def login(username, password):                                          # Определяем метод для авторизации в Instagram
    browser = webdriver.Chrome('chromedriver/chromedriver.exe')         # Создаём экземпляр объекта Chrome (в скобках указан путь к файлу)
    try:                                                                # Помещаем дальнейший код в блок try, чтобы можно было отлавливать ошибки
        browser.get('https://instagram.com')                            # Открываем в браузере вкладку с Instagram
        time.sleep(random.randint(3,5))                                 # Делаем задержку от 3 до 4 секунд (5 не входит в диапазон)

        username_input = browser.find_element_by_name('username')       # Создаём переменную username_input, в которую подаём элемент с именем 'username'
        username_input.clear()                                          # Очищаем строку
        username_input.send_keys(username)                              # Подаём нажатие клавиш в виде нашего логина, т.е. username

        time.sleep(2)                                                   # Ждём 2 секунды

        password_input = browser.find_element_by_name('password')       # Создаём переменную password_input, в которую подаём элемент с именем 'password'
        password_input.clear()                                          # Очищаем строку
        password_input.send_keys(password)                              # Подаём нажатие клавиш в виде нашего пароля, т.е. password
        password_input.send_keys(Keys.ENTER)                            # Подаём нажатие клавиши ENTER
        time.sleep(10)                                                  # Ждём 10 секунд

        browser.close()                                                 # Закрываем браузер
        browser.quit()                                                  # Выходим из браузера, т.е. освобождаем ресурсы компьютера
    except Exception as ex:                                             # Если произойдёт исключение, то отлавливаем его тут и записываем, как ex
        print(ex)                                                       # Вывести текст ошибки в консоль
        browser.close()                                                 # Закрываем браузер
        browser.quit()                                                  # Выходим из браузера, т.е. освобождаем ресурсы компьютера

login(username, password)                                               # Вызываем наш метод для авторизации в Instagram