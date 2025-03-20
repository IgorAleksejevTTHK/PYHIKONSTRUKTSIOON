import MyModule
logins = []
passwords = []

# Регистрация нового пользователя
message = register_user(logins, passwords)
print(message)

# Авторизация
message = authorize_user(logins, passwords)
print(message)

# Проверка списков после регистрации
print("Список пользователей:", logins)
print("пароль:", passwords)
