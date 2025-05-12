import tkinter as tk
import random

# Algne balanss
balance = 1000  
player_name = ""

# Kaartide väärtused
cards_values = {
    "2": {"count": 4, "value": 2}, "3": {"count": 4, "value": 3}, "4": {"count": 4, "value": 4}, 
    "5": {"count": 4, "value": 5}, "6": {"count": 4, "value": 6}, "7": {"count": 4, "value": 7}, 
    "8": {"count": 4, "value": 8}, "9": {"count": 4, "value": 9}, "10": {"count": 4, "value": 10},
    "Vajet": {"count": 4, "value": 10}, "Dama": {"count": 4, "value": 10}, "Kuningas": {"count": 4, "value": 10}, 
    "Äss": {"count": 4, "value": [1, 11]}  
}

# Mängu seis
player_cards = []
player_score = 0
computer_cards = []
computer_score = 0
bet = 0

# Tkinteri aken
aken = tk.Tk()
aken.title("Blackjack - LUX")
aken.geometry("900x900")
aken.configure(bg="#d5f5a7")
icon = tk.PhotoImage(file="dota2_93574.png")  # или .ico
aken.iconphoto(True, icon)  
aken.resizable(False, False)  # Aken ei ole venitatav
# Funktsioonid
def loe_kaart(current_score):
    available_cards = [card for card in cards_values if cards_values[card]["count"] > 0]
    if not available_cards:
        return None, None  

    card = random.choice(available_cards)  
    cards_values[card]["count"] -= 1  

    if card == "Äss":
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
            result_label.config(text="❌ Vigane panus!")
            return
    except ValueError:
        result_label.config(text="❌ Sisesta arv!")
        return
    
    player_cards = []
    player_score = 0
    
    for _ in range(2):
        card, value = loe_kaart(player_score)
        if card:
            player_score += value
            player_cards.append(card)

    result_label.config(text=f"{player_name} sai kaardid: {player_cards}, skoor: {player_score}")

def player_take_card():
    global player_score
    if player_score >= 21:
        result_label.config(text="Ei saa rohkem kaarte võtta!")
        return
    
    card, value = loe_kaart(player_score)
    if card:
        player_score += value
        player_cards.append(card)
        result_label.config(text=f"{player_name} võttis kaardi: {card}, skoor: {player_score}")

def arvuti_mang():
    global computer_score, computer_cards
    score = 0
    computer_cards = []

    for _ in range(2):
        card, value = loe_kaart(score)
        if card:
            score += value
            computer_cards.append(card)

    while score < 16:  
        card, value = loe_kaart(score)
        if card is None:
            break  
        score += value
        computer_cards.append(card)

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
        winner = "Arvuti (Mängija ületas 21)"
        balance -= bet
    elif computer_score > 21:
        winner = "Mängija (Arvuti ületas 21)"
        balance += int(bet * 2 * 0.95)
    elif player_score > computer_score:
        winner = "Mängija"
        balance += int(bet * 2 * 0.95)
    elif player_score < computer_score:
        winner = "Arvuti"
        balance -= bet
    else:
        winner = "Viik"

    result_label.config(text=f"🏆 Võitja: {winner}\nMängija skoor: {player_score}, Arvuti skoor: {computer_score}\n💰 Uus balanss: {balance}")
    save_result(winner)

def save_result(winner):
    """Salvestab tulemuse faili"""
    with open("tulemus.txt", "a", encoding="utf-8") as file:
        file.write(f"Mängija: {player_score} ({', '.join(player_cards)}) / "
                   f"Arvuti: {computer_score} ({', '.join(computer_cards)}) - {winner} | "
                   f"Panus: {bet} | Balanss: {balance}\n")

def view_history():
    """Näitab mänguajalugu"""
    try:
        with open("tulemus.txt", "r", encoding="utf-8") as file:
            history = file.read()
        result_label.config(text=history[-300:])
    except FileNotFoundError:
        result_label.config(text="❌ Ajalugu puudub!")

# GUI elemendid
bg_image = tk.PhotoImage(file="13631463_090753191131_2.png")

# Устанавливаем изображение в Label
bg_label = tk.Label(aken, image=bg_image)
bg_label.place(relwidth=1, relheight=1) 

name_label = tk.Label(aken, text="Mängija nimi:",fg='purple',  font=("Arial", 12, "bold"))
name_label.pack()
name_entry = tk.Entry(aken, width=30)
name_entry.pack()

balance_label = tk.Label(aken, text=f"Balanss: {balance}",fg='purple', font=("Arial", 12, "bold"))
balance_label.pack()

bet_label = tk.Label(aken, text="Sisesta panus:",fg='purple', font=("Arial", 12, "bold"))
bet_label.pack()
bet_entry = tk.Entry(aken, width=30)
bet_entry.pack()

start_button = tk.Button(aken, text="Alusta mängu",fg='purple', command=start_game, font=("Arial", 12))
start_button.pack()

take_button = tk.Button(aken, text="Võta kaart",fg='purple', command=player_take_card,  font=("Arial", 12))
take_button.pack()

stop_button = tk.Button(aken, text="Peatu",fg='purple', command=stop_game,  font=("Arial", 12))
stop_button.pack()

history_button = tk.Button(aken, text="Vaata ajalugu",fg='purple', command=view_history,  font=("Arial", 12))
history_button.pack()

result_label = tk.Label(aken, text="Mänguseis ilmub siia...", fg='purple', font=("Arial", 10))
result_label.pack()

aken.mainloop()
