import smtplib, ssl
from email.message import EmailMessage
import tkinter as tk
from tkinter import filedialog, messagebox
import mimetypes
import os

failitee = None
valitud_allkiri = ""  
tume_režiim = False  # Muutuja tumeda režiimi jälgimiseks
text_color = "#000000"  # Algne tekstivärv tekstikastis (must)

def saada_kiri():
    """Saatke kiri, võimaliku manuse ja valitud allkirjaga."""
    kellele = email_box.get()
    teema = teema_box.get()
    kiri = kiri_box.get("1.0", tk.END).strip() + "\n\n" + valitud_allkiri  

    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "igoralekseje@gmail.com"
    password = "eeam jtoe otpf cxvz"

    msg = EmailMessage()
    msg.set_content(kiri)
    msg['Subject'] = teema
    msg['From'] = "Igor Aleksejev"
    msg['To'] = kellele

    if failitee:
        try:
            mime_type, _ = mimetypes.guess_type(failitee)
            if mime_type:
                maintype, subtype = mime_type.split("/")
            else:
                maintype, subtype = "application", "octet-stream"
            with open(failitee, "rb") as file:
                msg.add_attachment(file.read(), maintype=maintype, subtype=subtype, filename=os.path.basename(failitee))
        except Exception as e:
            messagebox.showerror("Faili viga", f"Ei saa manust lisada: {e}")
            return

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(sender_email, password)
            server.send_message(msg)
            messagebox.showinfo("Informatsioon", "Kiri oli saadetud!")
    except Exception as e:
        messagebox.showerror("Tekkis viga!", f"Viga saatmisel: {e}")

def vali_fail():
    global failitee
    failitee = filedialog.askopenfilename()

def puhasta_vorm():
    email_box.delete(0, tk.END)
    teema_box.delete(0, tk.END)
    kiri_box.delete("1.0", tk.END)
    allkiri_box.delete("1.0", tk.END)

def salvesta_allkiri():
    """Salvestab allkirja faili."""
    allkiri = allkiri_box.get("1.0", tk.END).strip()
    if allkiri:
        with open("allkirjad.txt", "a") as file:
            file.write(allkiri + "\n")
        messagebox.showinfo("Informatsioon", "Allkiri salvestatud!")

def vali_allkiri():
    """Avab allkirja valimise akna salvestatud allkirjadest."""
    global valitud_allkiri
    try:
        with open("allkirjad.txt", "r") as file:
            allkirjad = [line.strip() for line in file.readlines()]

        if allkirjad:
            valik_aken = tk.Toplevel(aken)
            valik_aken.title("Vali allkiri")
            valik_aken.geometry("300x200")
            valik_aken.configure(bg="#d5f5a7")  

            tk.Label(valik_aken, text="Vali allkiri:", font=("Arial", 12, "bold"), bg="#d5f5a7").pack()
            
            for allkiri in allkirjad:
                tk.Button(valik_aken, text=allkiri, command=lambda a=allkiri: set_allkiri(a, valik_aken), font=("Arial", 10), bg="#7fbf4d").pack()

        else:
            messagebox.showinfo("Informatsioon", "Allkirjad puuduvad!")
    except FileNotFoundError:
        messagebox.showinfo("Informatsioon", "Allkirjad puuduvad!")

def set_allkiri(allkiri, valik_aken):
    """Seab valitud allkirja ja sulgeb allkirja valimise akna."""
    global valitud_allkiri
    valitud_allkiri = allkiri
    valik_aken.destroy()
    messagebox.showinfo("Informatsioon", f"Valitud allkiri:\n{valitud_allkiri}")

def vaheta_teema():
    """Vahetab tumeda ja heleda teema vahel."""
    global tume_režiim, text_color

    if tume_režiim:
        aken.configure(bg="#d5f5a7")
        email_label.configure(bg="#d5f5a7", fg="black")
        teema_label.configure(bg="#d5f5a7", fg="black")
        kiri_label.configure(bg="#d5f5a7", fg="black")
        allkiri_label.configure(bg="#d5f5a7", fg="black")
        text_color = "#000000"
    else:
        aken.configure(bg="#333333")
        email_label.configure(bg="#333333", fg="white")
        teema_label.configure(bg="#333333", fg="white")
        kiri_label.configure(bg="#333333", fg="white")
        allkiri_label.configure(bg="#333333", fg="white")
        text_color = "#FFFFFF"
    
    # Muudame tekstikastide värvi
    kiri_box.configure(fg=text_color)
    allkiri_box.configure(fg=text_color)

    tume_režiim = not tume_režiim

# Graafiline liides
aken = tk.Tk()
aken.title("E-kiri saatmine")
aken.geometry("400x550")
aken.configure(bg="#d5f5a7")

email_label = tk.Label(aken, text="EMAIL:", bg="#d5f5a7", font=("Arial", 12, "bold"))
email_label.pack()
email_box = tk.Entry(aken, width=50)
email_box.pack()

teema_label = tk.Label(aken, text="TEEMA:", bg="#d5f5a7", font=("Arial", 12, "bold"))
teema_label.pack()
teema_box = tk.Entry(aken, width=50)
teema_box.pack()

kiri_label = tk.Label(aken, text="SÕNUM:", bg="#d5f5a7", font=("Arial", 12, "bold"))
kiri_label.pack()
kiri_box = tk.Text(aken, height=5, width=50)
kiri_box.pack()

allkiri_label = tk.Label(aken, text="ALLKIRI:", bg="#d5f5a7", font=("Arial", 12, "bold"))
allkiri_label.pack()
allkiri_box = tk.Text(aken, height=2, width=50)
allkiri_box.pack()

lisa_pilt_nupp = tk.Button(aken, text="LISA PILT", command=vali_fail, bg="#7fbf4d", font=("Arial", 12))
lisa_pilt_nupp.pack()

saada_nupp = tk.Button(aken, text="SAADA", command=saada_kiri, bg="#4d9f38", font=("Arial", 12))
saada_nupp.pack()

puhasta_nupp = tk.Button(aken, text="PUHASTA", command=puhasta_vorm, bg="#bf4d4d", font=("Arial", 12))
puhasta_nupp.pack()

salvesta_allkiri_nupp = tk.Button(aken, text="SALVESTA ALLKIRI", command=salvesta_allkiri, bg="#4d7fbf", font=("Arial", 12))
salvesta_allkiri_nupp.pack()

vali_allkiri_nupp = tk.Button(aken, text="VALI ALLKIRI", command=vali_allkiri, bg="#4d7fbf", font=("Arial", 12))
vali_allkiri_nupp.pack()

teema_vahetus_nupp = tk.Button(aken, text="VAHETA TEEMA", command=vaheta_teema, bg="#9b59b6", font=("Arial", 12))
teema_vahetus_nupp.pack()

aken.mainloop()
