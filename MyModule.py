import random
import string

logins = []  # Список для хранения имен пользователей / Kasutajate nimede loend
passwords = []  # Список для хранения паролей / Paroolide loend

def checkpassword(password):
    """Проверяет, соответствует ли пароль требованиям безопасности.
    Kontrollib, kas parool vastab turvanõuetele."""
    val1 = list(".,:;!_*-+()/#¤%&")  # Список символов / Sümbolite loend
    val2 = list("0123456789")  # Список цифр / Numbrite loend
    val3 = list('qwertyuiopasdfghjklzxcvbnm')  # Список строчных букв / Väiketähtede loend
    val4 = list('QWERTYUIOPASDFGHJKLZXCVBNM')  # Список заглавных букв / Suurtähtede loend

    # проверка наличия различных типов символов в пароле / Lipud parooli tüüpide kontrollimiseks
    has_symbols = False
    has_digits = False
    has_lowercase = False
    has_uppercase = False

    for char in password:
        if char in val1:  # Если символ есть в списке специальных символов / Kas sümbol on spetsiaalsete sümbolite loendis
            has_symbols = True
        if char in val2:  # Если символ есть в списке цифр / Kas sümbol on numbrite loendis
            has_digits = True
        if char in val3:  # Если символ есть в списке строчных букв / Kas sümbol on väiketähtede loendis
            has_lowercase = True
        if char in val4:  # Если символ есть в списке заглавных букв / Kas sümbol on suurtähtede loendis
            has_uppercase = True

        # Если все условия выполнены, возвращаем True / Kui kõik tingimused on täidetud, tagastatakse True
        if has_symbols and has_digits and has_lowercase and has_uppercase:
            return True
    return False  # Если одно из условий не выполнено, возвращаем False / Kui üks tingimus pole täidetud, tagastatakse False

def register_user(logins, passwords):
    """Регистрация пользователей.
    Kasutajade registratsioon."""
    print("\nKasutajade registratsioon")
    username = input("Sisestage kasutaja nimi: ")

    # Проверяем, существует ли уже введенный логин / Kontrollime, kas sisestatud kasutajanimi on juba olemas
    if username in logins:
        print("Kasutaja nimi on võetud.")  
        return  # Завершаем функцию / Funktsioon lõpetatakse

    choice = input("Kas luua salasõna automaatselt? jah/ei: ").lower()
    if choice == "jah":
        # Генерация случайного пароля длиной 9 символов / Juhusliku 9-tähemärgilise parooli genereerimine
        password = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(9)])
        print(f"Teie parool: {password}")
    else:
        
        password = input("Sisestage salasõna: ")
        if not checkpassword(password):  # Проверяем, соответствует ли пароль требованиям / Kontrollime, kas parool vastab nõuetele
            print("Salasõna ei ole õige.")  
            return 

    # Добавляем логин и пароль в соответствующие списки / Lisame kasutajanime ja parooli vastavatesse loenditesse
    logins.append(username)
    passwords.append(password)
    print("Registreerimine õnnestus!") 

def authorize_user(logins, passwords):
    """Авторизация пользователя.
    Kasutaja autoriseerimine."""
    print("\nKasutaja autoriseerimine")
    username = input("Sisestage kasutaja nimi: ")
    password = input("Sisestage salasõna: ")

      # Проверяем, есть ли пользователь в списке логинов / Kontrollime, kas kasutajanimi on loendis
    if username in logins:
        index = logins.index(username)  # Получаем индекс логина в списке / Saame kasutajanime indeksi loendis
        if passwords[index] == password:  # Проверяем, соответствует ли пароль / Kontrollime, kas parool klapib
            print("Autoriseerimine õnnestus!")  
            return  
        print("Vale salasõna!")  
        return  
    print("Kasutaja ei leitud!")  

def change_password(logins, passwords):
    """Изменение пароля пользователя.
    Kasutaja parooli muutmine."""
    print("\nSalasõna muutmine")
    username = input("Sisestage kasutajanimi: ")

    if username in logins:
        index = logins.index(username)  # Получаем индекс логина / Saame kasutajanime indeksi
        new_password = input("Sisestage uue salasõna: ")
        if checkpassword(new_password):  # Проверяем, соответствует ли новый пароль требованиям / Kontrollime uue parooli nõuetele vastavust
            passwords[index] = new_password  # Обновляем пароль в списке / Uuendame parooli loendis
            print("Parooli muutmine õnnestus!")  
            return  
        print("Uus parool ei ole õige.") 
        return  
    print("Kasutaja ei leitud!")  

def main_menu():
    """Главное меню программы.
    Programmi peamenüü."""
    while True:
        print("\nMenüü:")
        print("1. Registreerimine")
        print("2. Autoriseerimine")
        print("3. Muuda parooli")
        print("4. Välju")

        choice = input("Valige toiming: ")

        if choice == "1":
            register_user(logins, passwords)
        elif choice == "2":
            authorize_user(logins, passwords)
        elif choice == "3":
            change_password(logins, passwords)
        elif choice == "4":
            print("Välju programmist.")  
            break  
        else:
            print("Vale valik, proovi uuesti.") 

main_menu()
