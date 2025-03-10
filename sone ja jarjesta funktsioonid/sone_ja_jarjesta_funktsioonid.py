﻿lst = []

while True:
    # Выводим меню для выбора функций
    print("\nМеню функций:")
    print("1. Добавить элемент в список")
    print("2. Удалить элемент из списка")
    print("3. Найти максимальный элемент в списке")
    print("4. Найти минимальный элемент в списке")
    print("5. Проверить наличие элемента в списке")
    print("6. Развернуть строку")
    print("7. Преобразовать строку в верхний регистр")
    print("0. Выйти")

    choice = int(input("Выберите функцию: "))

    if choice == 0:
        # Если выбрано "0", выходим из цикла и программы
        break
    elif choice == 1:
        # Добавление элемента в список
        element = input("Введите элемент для добавления: ")
        lst.append(element)
        print(f"Элемент {element} добавлен в список.")
    elif choice == 2:
        # Удаление элемента из списка
        element = input("Введите элемент для удаления: ")
        if element in lst:
            lst.remove(element)
            print(f"Элемент {element} удален из списка.")
        else:
            print(f"Элемент {element} не найден в списке.")
    elif choice == 3:
        # Поиск максимального элемента в списке
        if lst:
            print("Максимальный элемент:", max(lst))
        else:
            print("Список пуст.")
    elif choice == 4:
        # Поиск минимального элемента в списке
        if lst:
            print("Минимальный элемент:", min(lst))
        else:
            print("Список пуст.")
    elif choice == 5:
        # Проверка наличия элемента в списке
        element = input("Введите элемент для проверки: ")
        print(f"Элемент {'найден' if element in lst else 'не найден'} в списке.")
    elif choice == 6:
        # Разворот строки
        s = input("Введите строку для разворота: ")
        print("Развернутая строка:", s[::-1])
    elif choice == 7:
        # Преобразование строки в верхний регистр
        s = input("Введите строку для преобразования: ")
        print("Строка в верхнем регистре:", s.upper())
    else:
        # Обработка неверного выбора
        print("Неверный выбор, попробуйте снова.")
