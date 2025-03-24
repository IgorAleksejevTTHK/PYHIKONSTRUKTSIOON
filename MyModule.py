import random
import string


logins = []
passwords = []


def checkpassword(password):
    val1 = list(".,:;!_*-+()/#¤%&")
    val2 = list("0123456789")
    val3 = list('qwertyuiopasdfghjklzxcvbnm')
    val4 = list('QWERTYUIOPASDFGHJKLZXCVBNM')

    has_symbols = False
    has_digits = False
    has_lowercase = False
    has_uppercase = False

    for char in password:
        if char in val1:
            has_symbols = True
        if char in val2:
            has_digits = True
        if char in val3:
            has_lowercase = True
        if char in val4:
            has_uppercase = True

        if has_symbols and has_digits and has_lowercase and has_uppercase:
            return True
    return False


def register_user(logins, passwords):
    print("\nРегистрация пользователя")
    username = input("Введите имя пользователя: ")

    if username in logins:
        print("Имя пользователя занято.")
        return

    choice = input("Создать пароль автоматически? да/нет: ").lower()
    if choice == "да":
        password = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(9)])
        print(f"Ваш пароль: {password}")
    else:
        password = input("Введите пароль: ")
        if not checkpassword(password):
            print("Пароль не соответствует норме.")
            return

    logins.append(username)
    passwords.append(password)
    print("Регистрация прошла успешно!")


def authorize_user(logins, passwords):
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
    print("\nСмена пароля")
    username = input("Введите имя пользователя: ")
   

    if username in logins:
        index = logins.index(username)
        
        new_password = input("Введите новый пароль: ")
        if checkpassword(new_password):
                passwords[index] = new_password
                print("Пароль успешно изменён!")
                return
        print("Новый пароль не соответствует норме.")
        return
    print("Пользователь не найден!")


def main_menu():
    while True:
        print("\nМеню:")
        print("1. Регистрация")
        print("2. Авторизация")
        print("3. Смена пароля")
        print("4. Выход")

        choice = input("Выберите действие: ")

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



main_menu()
