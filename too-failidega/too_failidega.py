import random

def loe_failist():
    sonastik = {}
    try:
        with open("sonastik.txt", 'r', encoding='utf-8-sig') as file:
            for line in file:
                est, rus = line.strip().split('-')
                sonastik[est] = rus
        print("Andmed on failist loetud!")
    except FileNotFoundError:
        print("Faili sonastik.txt ei leitud. Alustatakse tühja sõnastikuga.")
    return sonastik

def salvesta_faili(sonastik):
    with open("sonastik.txt", 'w', encoding='utf-8-sig') as file:
        for est, rus in sonastik.items():
            file.write(f"{est}-{rus}\n")
    print("Andmed on faili salvestatud!")

def tolgi_est_rus(sona, sonastik):
    return sonastik.get(sona, "Sõna ei leitud sõnastikus!")

def tolgi_rus_est(sona, sonastik):
    for est, rus in sonastik.items():
        if rus == sona:
            return est
    return "Sõna ei leitud sõnastikus!"

def lisa_sona(sonastik):
    est_sona = input("Sisesta uus sõna eesti keeles: ")
    rus_sona = input("Sisesta selle sõna vene tõlge: ")
    if est_sona and rus_sona:
        sonastik[est_sona] = rus_sona
        print("Sõna lisatud!")

def paranda_sona(sonastik):
    est_sona = input("Sisesta parandatav sõna eesti keeles: ")
    if est_sona in sonastik:
        rus_sona = input("Sisesta uus tõlge vene keeles: ")
        sonastik[est_sona] = rus_sona
        print("Sõna parandatud!")
    else:
        print("Sõna ei leitud sõnastikus!")

def testi_teadmisi(sonastik):
    sonad = list(sonastik.items())
    score = 0
    for est_sona, rus_sona in sonad:
        vastus = input(f"Sisesta vene tõlge sõnale '{est_sona}': ")
        if vastus == rus_sona:
            print("Õige!")
            score += 1
        else:
            print(f"Vale! Õige vastus: {rus_sona}")
    print(f"Test lõppenud! Sinu tulemus: {score / len(sonad) * 100:.2f}%")

def main():
    sonastik = loe_failist()

    while True:
        print("""\nTere tulemast eesti-vene sõnastikku!
Valikud:
1 - Tõlgi eesti -> vene
2 - Tõlgi vene -> eesti
3 - Lisa uus sõna
4 - Paranda sõna
5 - Testi teadmisi
6 - Näita sõnastikku
7 - Salvesta sõnastik faili
8 - Välju
""")
        valik = input("Tee oma valik: ")
        if valik == "1":
            est_sona = input("Sisesta sõna eesti keeles: ")
            print(f"Tõlge vene keelde: {tolgi_est_rus(est_sona, sonastik)}")
        elif valik == "2":
            rus_sona = input("Sisesta sõna vene keeles: ")
            print(f"Tõlge eesti keelde: {tolgi_rus_est(rus_sona, sonastik)}")
        elif valik == "3":
            lisa_sona(sonastik)
        elif valik == "4":
            paranda_sona(sonastik)
        elif valik == "5":
            testi_teadmisi(sonastik)
        elif valik == "6":
            for est, rus in sonastik.items():
                print(f"{est} - {rus}")
        elif valik == "7":
            salvesta_faili(sonastik)
        elif valik == "8":
            print("Nägemist!")
            salvesta_faili(sonastik)  
            break
        else:
            print("Vale valik, proovi uuesti.")

if __name__ == "__main__":
    main()
