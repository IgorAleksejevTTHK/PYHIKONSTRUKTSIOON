import smtplib, ssl
from email.message import EmailMessage
import random
import string
import os


DATA_FILE = "user_data.txt"

def load_data():
    """Загрузка данных из текстового файла."""
    

    with open(DATA_FILE, "r") as file:
        lines = file.readlines()
        logins = []
        passwords = []
        emails = []
        for line in lines:
            login, password, email = line.strip().split(", ")
            logins.append(login)
            passwords.append(password)
            emails.append(email)
        return logins, passwords, emails

def save_data(logins, passwords, emails):
    """Сохранение данных в текстовый файл."""
    with open(DATA_FILE, "w") as file:
        for login, password, email in zip(logins, passwords, emails):
            file.write(f"{login}, {password}, {email}\n")

def send_email_notification(email, subject, body):
    """Отправка уведомления на e-mail."""
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = "igoralekseje@gmail.com" 
    sender_password = "eeam jtoe otpf cxvz" 

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = email
    msg.set_content(body)

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print("Teavitus saadetud!")
    except Exception as e:
        print(f"Teavituse saatmine nurjus: {e}")

def checkpassword(password):
    """Проверяет, соответствует ли пароль требованиям безопасности."""
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

def register_user(logins, passwords, emails):
    """Регистрация пользователей."""
    print("\nKasutajade registratsioon")
    username = input("Sisestage kasutaja nimi: ")

    if username in logins:
        print("Kasutaja nimi on võetud.")
        return

    email = input("Sisestage e-mail: ")
    if email in emails:
        print("E-mail juba kasutusel.")
        return

    choice = input("Kas luua salasõna automaatselt? jah/ei: ").lower()
    if choice == "jah":
        password = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(9)])
        print(f"Teie parool: {password}")
    else:
        password = input("Sisestage salasõna: ")
        if not checkpassword(password):
            print("Salasõna ei ole õige.")
            return

    logins.append(username)
    passwords.append(password)
    emails.append(email)
    save_data(logins, passwords, emails)
    print("Registreerimine õnnestus!")

    send_email_notification(email, "Registreerimine õnnestus", f"Tere, {username}! Te olete edukalt registreerunud.")

def authorize_user(logins, passwords, emails):
    """Авторизация пользователя."""
    print("\nKasutaja autoriseerimine")
    username = input("Sisestage kasutaja nimi: ")
    password = input("Sisestage salasõna: ")

    if username in logins:
        index = logins.index(username)
        if passwords[index] == password:
            print("Autoriseerimine õnnestus!")
            email = emails[index]
            send_email_notification(email, "Autoriseerimine edukas", f"Tere, {username}! Te olete edukalt autoriseeritud.")
            return
        print("Vale salasõna!")
        return
    print("Kasutaja ei leitud!")

def change_password(logins, passwords, emails):
    """Изменение пароля пользователя."""
    print("\nSalasõna muutmine")
    username = input("Sisestage kasutajanimi: ")

    if username in logins:
        index = logins.index(username)
        new_password = input("Sisestage uue salasõna: ")
        if checkpassword(new_password):
            passwords[index] = new_password
            save_data(logins, passwords, emails)
            print("Parooli muutmine õnnestus!")
            email = emails[index]
            send_email_notification(email, "Salasõna muudetud", f"Tere, {username}! Teie salasõna on edukalt muudetud.")
            return
        print("Uus parool ei ole õige.")
        return
    print("Kasutaja ei leitud!")

def main_menu():
    """Главное меню программы."""
    logins, passwords, emails = load_data()

    while True:
        print("\nMenüü:")
        print("1. Registreerimine")
        print("2. Autoriseerimine")
        print("3. Muuda parooli")
        print("4. Välju")

        choice = input("Valige toiming: ")

        if choice == "1":
            register_user(logins, passwords, emails)
        elif choice == "2":
            authorize_user(logins, passwords, emails)
        elif choice == "3":
            change_password(logins, passwords, emails)
        elif choice == "4":
            print("Välju programmist.")
            break
        else:
            print("Vale valik, proovi uuesti.")

main_menu()
