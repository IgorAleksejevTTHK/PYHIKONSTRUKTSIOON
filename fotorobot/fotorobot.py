import tkinter as tk
from tkinter import ttk, messagebox
import os

# --- Функция для получения координат центра каждой части ---
def part_coords(part):
    return {
        "naovorm": (200, 200),
        "silmad": (200, 170),
        "nina": (200, 170),
        "suu": (200, 140),
    }[part]

# --- Отрисовка одной части ---
def draw_part(part, image_dict, variable, var_check):
    canvas.delete(part)
    if var_check.get():
        variant = variable.get()
        path = f"fotorobot/{part}{variant}.png"
        if os.path.exists(path):
            image = tk.PhotoImage(file=path)
            images[part] = image  # чтобы не удалялся из памяти
            x, y = part_coords(part)
            canvas.create_image(x, y, image=image, tags=part)

# --- Обновление всех частей ---
def update_all():
    draw_part("naovorm", images, naovorm_var, naovorm_check)
    draw_part("silmad", images, silmad_var, silmad_check)
    draw_part("nina", images, nina_var, nina_check)
    draw_part("suu", images, suu_var, suu_check)

# --- Сохранение состояния ---
def save_robot():
    data = []
    for part, check_var, combo_var in [
        ("naovorm", naovorm_check, naovorm_var),
        ("silmad", silmad_check, silmad_var),
        ("nina", nina_check, nina_var),
        ("suu", suu_check, suu_var),
    ]:
        if check_var.get():
            data.append(f"{part}:{combo_var.get()}")
    with open("fotorobotid.txt", "a") as f:
        f.write(",".join(data) + "\n")
    messagebox.showinfo("Сохранено", "Фоторобот сохранен!")

# --- Загрузка последнего фоторобота ---
def load_last_robot():
    try:
        with open("fotorobotid.txt", "r") as f:
            lines = f.readlines()
        if not lines:
            raise FileNotFoundError
        last = lines[-1].strip().split(",")
        for part_data in last:
            part, variant = part_data.split(":")
            if part == "naovorm":
                naovorm_check.set(True)
                naovorm_var.set(variant)
            elif part == "silmad":
                silmad_check.set(True)
                silmad_var.set(variant)
            elif part == "nina":
                nina_check.set(True)
                nina_var.set(variant)
            elif part == "suu":
                suu_check.set(True)
                suu_var.set(variant)
        update_all()
    except FileNotFoundError:
        messagebox.showwarning("Внимание", "Файл с фотороботами не найден!")

# --- Интерфейс ---
root = tk.Tk()
root.title("Фоторобот")

left = tk.Frame(root)
left.pack(side="left", padx=10, pady=10)

right = tk.Frame(root)
right.pack(side="right", padx=10, pady=10)

canvas = tk.Canvas(right, width=400, height=400, bg="white")
canvas.pack()

# Словарь для хранения изображений
images = {}

# Переменные Checkbutton и Combobox
naovorm_check = tk.BooleanVar(value=True)
silmad_check = tk.BooleanVar(value=True)
nina_check = tk.BooleanVar(value=True)
suu_check = tk.BooleanVar(value=True)

naovorm_var = tk.StringVar(value="1")
silmad_var = tk.StringVar(value="1")
nina_var = tk.StringVar(value="1")
suu_var = tk.StringVar(value="1")

# --- Компоненты GUI ---
def add_selector(label_text, check_var, combo_var, part, max_val):
    tk.Checkbutton(left, text=label_text, variable=check_var, command=update_all).pack(anchor="w")
    tk.Label(left, text=f"Вариант {label_text.lower()}:").pack(anchor="w")
    combo = ttk.Combobox(left, textvariable=combo_var, values=[str(i) for i in range(1, max_val + 1)], width=5)
    combo.bind("<<ComboboxSelected>>", lambda e: update_all())
    combo.pack(anchor="w", pady=(0, 5))

add_selector("Naovorm", naovorm_check, naovorm_var, "naovorm", 5)
add_selector("Silmad", silmad_check, silmad_var, "silmad", 5)
add_selector("Nina", nina_check, nina_var, "nina", 5)
add_selector("Suu", suu_check, suu_var, "suu", 5)

tk.Button(left, text="Сохранить фоторобот", command=save_robot).pack(pady=5)
tk.Button(left, text="Загрузить последний фоторобот", command=load_last_robot).pack()

update_all()
root.mainloop()
