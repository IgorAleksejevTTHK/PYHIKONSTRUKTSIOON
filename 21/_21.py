import tkinter as tk
from PIL import Image, ImageTk  # Импортируем Pillow для работы с изображениями
import random
# Исходный баланс
balance = 1000  
player_name = ""

# Значения карт
cards_values = {
    "2": {"count": 4, "value": 2}, "3": {"count": 4, "value": 3}, "4": {"count": 4, "value": 4}, 
    "5": {"count": 4, "value": 5}, "6": {"count": 4, "value": 6}, "7": {"count": 4, "value": 7}, 
    "8": {"count": 4, "value": 8}, "9": {"count": 4, "value": 9}, "10": {"count": 4, "value": 10},
    "Vajet": {"count": 4, "value": 10}, "Dama": {"count": 4, "value": 10}, "Kuningas": {"count": 4, "value": 10}, 
    "Äss": {"count": 4, "value": [1, 11]}  
}

# Игра
player_cards = []
player_score = 0
computer_cards = []
computer_score = 0
bet = 0

# Tkinter окно
aken = tk.Tk()
aken.title("Blackjack - LUX")
aken.geometry("600x600")
aken.configure(bg="#d5f5a7")
icon = tk.PhotoImage(file="dota2_93574.png")  # или .ico
aken.iconphoto(True, icon)  
aken.resizable(False, False)  # Окно не растягиваемое

# Функции
def loe_kaart(current_score):
    available_cards = [card for card in cards_values if cards_values[card]["count"] > 0]
    if not available_cards:
        return None, None  # Если карт нет, возвращаем None

    card = random.choice(available_cards)  # Выбираем случайную карту
    cards_values[card]["count"] -= 1  # Уменьшаем количество карт

    if card == "Äss":
        # Если выпала "Äss" (туз), выбираем 1 или 11 в зависимости от текущего счета
        value = 11 if current_score + 11 <= 21 else 1
    else:
        value = cards_values[card]["value"]

    return card, value

def start_game():
    global player_name, balance, player_cards, player_score, bet
    
    player_name = name_entry.get()
    try:
        bet = int(bet_entry.get())
        if bet <= 0 or bet > balance:
            result_label.config(text="❌ Неверная ставка!")
            return
    except ValueError:
        result_label.config(text="❌ Введите число!")
        return
    
    player_cards = []
    player_score = 0
    
    for _ in range(2):
        card, value = loe_kaart(player_score)
        if card:
            player_score += value
            player_cards.append(card)

    balance_label.config(text=f"Баланс: {balance}")
    result_label.config(text=f"{player_name} получил карты: {player_cards}, счет: {player_score}")

def player_take_card():
    global player_score
    if player_score >= 21:
        result_label.config(text="Нельзя взять больше карт!")
        return
    
    card, value = loe_kaart(player_score)
    if card:
        player_score += value
        player_cards.append(card)
        result_label.config(text=f"{player_name} взял карту: {card}, счет: {player_score}")

def arvuti_mang():
    global computer_score, computer_cards
    score = 0
    computer_cards = []

    for _ in range(2):
        card, value = loe_kaart(score)
        if card:
            score += value
            computer_cards.append(card)

    while score < 16:  # Если у компьютера меньше 16, он берет карты
        card, value = loe_kaart(score)
        if card is None:
            break  # Если карт нет, выходим
        score += value
        computer_cards.append(card)

    # Если у компьютера 16, 17 или 18, он может попробовать взять еще карты
    for limit, chance in [(16, 73), (17, 53), (18, 23)]:
        if score == limit:
            if random.randint(0, 100) < chance:
                card, value = loe_kaart(score)
                if card:
                    score += value
                    computer_cards.append(card)

    computer_score = score

def stop_game():
    global balance
    arvuti_mang()
    
    if player_score > 21:
        winner = "Компьютер (Игрок перебрал 21)"
        balance -= bet
    elif computer_score > 21:
        winner = "Игрок (Компьютер перебрал 21)"
        balance += int(bet * 2 * 0.95)
    elif player_score > computer_score:
        winner = "Игрок"
        balance += int(bet * 2 * 0.95)
    elif player_score < computer_score:
        winner = "Компьютер"
        balance -= bet
    else:
        winner = "Ничья"

    balance_label.config(text=f"Баланс: {balance}")  # Обновляем баланс
    result_label.config(text=f"🏆 Победитель: {winner}\nСчет игрока: {player_score}, Счет компьютера: {computer_score}\n💰 Новый баланс: {balance}")
    save_result(winner)

def save_result(winner):
    """Сохраняет результат игры в файл"""
    with open("tulemus.txt", "a", encoding="utf-8") as file:
        file.write(f"Игрок: {player_score} ({', '.join(player_cards)}) / "
                   f"Компьютер: {computer_score} ({', '.join(computer_cards)}) - {winner} | "
                   f"Ставка: {bet} | Баланс: {balance}\n")

def view_history():
    """Показывает историю игр"""
    try:
        with open("tulemus.txt", "r", encoding="utf-8") as file:
            history = file.read()
        result_label.config(text=history)  # Показываем всю историю
    except FileNotFoundError:
        result_label.config(text="❌ История пуста!")

# GUI элементы
bg_image = tk.PhotoImage(file="13631463_090753191131_2.png")

# Устанавливаем изображение в Label
bg_label = tk.Label(aken, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Загружаем изображения для кнопок
start_image = Image.open("start_button_image.png")  # Замените на путь к вашему изображению
start_image = start_image.resize((100, 50))  # Меняем размер изображения под кнопку
start_photo = ImageTk.PhotoImage(start_image)

take_image = Image.open("take.png")  # Замените на путь к вашему изображению
take_image = take_image.resize((100, 50))  # Меняем размер изображения под кнопку
take_photo = ImageTk.PhotoImage(take_image)

stop_image = Image.open("realniystart.png")  # Замените на путь к вашему изображению
stop_image = stop_image.resize((100, 50))  # Меняем размер изображения под кнопку
stop_photo = ImageTk.PhotoImage(stop_image)

history_image = Image.open("story.png")  # Замените на путь к вашему изображению
history_image = history_image.resize((100, 50))  # Меняем размер изображения под кнопку
history_photo = ImageTk.PhotoImage(history_image)

name_label = tk.Label(aken, text="Имя игрока:", fg='purple', font=("Arial", 12, "bold"))
name_label.pack()
name_entry = tk.Entry(aken, width=30)
name_entry.pack()

balance_label = tk.Label(aken, text=f"Баланс: {balance}", fg='purple', font=("Arial", 12, "bold"))
balance_label.pack()

bet_label = tk.Label(aken, text="Введите ставку:", fg='purple', font=("Arial", 12, "bold"))
bet_label.pack()
bet_entry = tk.Entry(aken, width=30)
bet_entry.pack()

# Используем изображения для кнопок
start_button = tk.Button(aken, image=start_photo, command=start_game)
start_button.pack(pady=10)

take_button = tk.Button(aken, image=take_photo, command=player_take_card)
take_button.pack(pady=10)

stop_button = tk.Button(aken, image=stop_photo, command=stop_game)
stop_button.pack(pady=10)

history_button = tk.Button(aken, image=history_photo, command=view_history)
history_button.pack(pady=10)

result_label = tk.Label(aken, text="Здесь появится статус игры...", fg='purple', font=("Arial", 10))
result_label.pack()

aken.mainloop()
