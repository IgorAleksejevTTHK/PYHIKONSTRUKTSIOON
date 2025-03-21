﻿import random
import string

def register_user(logins, passwords):
    print("\nРегистрация пользователя")
    username = input("Введите имя пользователя: ")

    # Проверяем, занято ли имя
    if username in logins:
        return "Имя пользователя занято."

    # Выбор способа создания пароля
    choice = input("Создать пароль автоматически? да/нет: ").lower()
    if choice == "да":
        password = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(8)])
        print(f"Ваш пароль: {password}")
    else:
        password = input("Введите пароль: ")

    # Добавляем имя и пароль в списки
    logins.append(username)
    passwords.append(password)
    return "Регистрация прошла успешно!"

def authorize_user(logins, passwords):
    print("\nАвторизация пользователя")
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    # Проверяем, существует ли пользователь
    if username in logins:
        index = logins.index(username)
        if passwords[index] == password:
            return "Авторизация успешна!"
        return "Неверный пароль!"
    return "Пользователь не найден!"
 
logins = []
passwords = []


message = register_user(logins, passwords)
print(message)


message = authorize_user(logins, passwords)
print(message)


print("Список пользователей:", logins)
print("Список паролей:", passwords)

