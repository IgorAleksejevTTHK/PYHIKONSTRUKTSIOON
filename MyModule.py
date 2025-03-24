import random
import string

logins = []
passwords = []

def check_password(password):
    """
    Проверяет, соответствует ли пароль требованиям безопасности.

    Требования:
    - Содержит хотя бы один символ из набора специального символа.
    - Содержит хотя бы одну цифру.
    - Содержит хотя бы одну строчную букву.
    - Содержит хотя бы одну заглавную букву.

    Args:
        password (str): Пароль, который нужно проверить.

    Returns:
        bool: True, если пароль соответствует требованиям, иначе False.
    """
    symbols = ".,:;!_*-+()/#¤%&"
    digits = "0123456789"
    lowercase = 'qwertyuiopasdfghjklzxcvbnm'
    uppercase = 'QWERTYUIOPASDFGHJKLZXCVBNM'

    return (any(char in symbols for char in password) and
            any(char in digits for char in password) and
            any(char in lowercase for char in password) and
            any(char in uppercase for char in password))

def register_user(logins, passwords):
    """
    Регистрирует нового пользователя и сохраняет его имя и пароль.

    Процесс:
    - Пользователь вводит имя и выбирает, создавать ли пароль автоматически.
    - Пароль проверяется на соответствие требованиям безопасности.

    Args:
        logins (list): Список зарегистрированных имён пользователей.
        passwords (list): Список зарегистрированных паролей.

    Returns:
        None
    """
    print("\nРегистрация пользователя")
    username = input("Введите имя пользователя: ")

    if username in logins:
        print("Имя пользователя занято.")
        return

    choice = input("Создать пароль автоматически? да/нет: ").lower()
    if choice == "да":
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=9))
        print(f"Ваш пароль: {password}")
    else:
        password = input("Введите пароль: ")
        if not check_password(password):
            print("Пароль не соответствует норме.")
            return

    logins.append(username)
    passwords.append(password)
    print("Регистрация прошла успешно!")

def authorize_user(logins, passwords):
    """
    Авторизует пользователя, проверяя его имя и пароль.

    Процесс:
    - Пользователь вводит имя и пароль.
    - Проверяются совпадения имени и пароля.

    Args:
        logins (list): Список зарегистрированных имён пользователей.
        passwords (list): Список зарегистрированных паролей.

    Returns:
        None
    """
    print("\nАвторизация пользователя")
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    if username in logins:
        index = logins.index(username)
        if passwords[index] == password:
            print("Авторизация успешна!")
            return
        print("Неверный пароль!")
        return
    print("Пользователь не найден!")

def change_password(logins, passwords):
    """
    Изменяет пароль для зарегистрированного пользователя.

    Процесс:
    - Пользователь вводит имя и новый пароль.
    - Проверяется, соответствует ли новый пароль требованиям безопасности.

    Args:
        logins (list): Список зарегистрированных имён пользователей.
        passwords (list): Список зарегистрированных паролей.

    Returns:
        None
    """
    print("\nСмена пароля")
    username = input("Введите имя пользователя: ")

    if username in logins:
        index = logins.index(username)
        new_password = input("Введите новый пароль: ")
        if check_password(new_password):
            passwords[index] = new_password
            print("Пароль успешно изменён!")
        else:
            print("Новый пароль не соответствует норме.")
    else:
        print("Пользователь не найден!")

def main_menu():
    """
    Основное меню программы.

    Пользователь может выбрать одно из действий:
    1. Регистрация.
    2. Авторизация.
    3. Смена пароля.
    4. Выход из программы.

    Returns:
        None
    """
    while True:
        print("\nМеню:")
        print("1. Регистрация")
        print("2. Авторизация")
        print("3. Смена пароля")
        print("4. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            register_user(logins, passwords)
        elif choice == "2":
            authorize_user(logins, passwords)
        elif choice == "3":
            change_password(logins, passwords)
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

# Запуск программы
main_menu()
