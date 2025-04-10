import random

sonastik = {
    'koer': 'собака',
    'kass': 'кошка',
    'maja': 'дом',
    'auto': 'машина',
    'päike': 'солнце'
}

def tolgi_est_rus(sona):
    return sonastik.get(sona, "Sõna ei leitud sõnastikus!")

def tolgi_rus_est(sona):
    for est, rus in sonastik.items():
        if rus == sona:
            return est
    return "Sõna ei leitud sõnastikus!"

def lisa_sona():
    est_sona = input("Sisesta uus sõna eesti keeles: ")
    rus_sona = input("Sisesta selle sõna vene tõlge: ")
    if est_sona and rus_sona:
        sonastik[est_sona] = rus_sona
        print("Sõna lisatud!")

def paranda_sona():
    est_sona = input("Sisesta parandatav sõna eesti keeles: ")
    if est_sona in sonastik:
        rus_sona = input("Sisesta uus tõlge vene keeles: ")
        print("Sõna parandatud!")
    else:
        print("Sõna ei leitud sõnastikus!")

def testi_teadmisi():
    sonad = list(sonastik.items())
    random.choice   (sonad)
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
    while True:
        print("\nTere tulemast eesti-vene sõnastikku!")
        print("Valikud:")
        print("1 - Tõlgi eesti -> vene")
        print("2 - Tõlgi vene -> eesti")
        print("3 - Lisa uus sõna")
        print("4 - Paranda sõna")
        print("5 - Testi teadmisi")
        print("6 - Välju")
        
        valik = input("Tee oma valik: ")
        if valik == "1":
            est_sona = input("Sisesta sõna eesti keeles: ")
            print(f"Tõlge vene keelde: {tolgi_est_rus(est_sona)}")
        elif valik == "2":
            rus_sona = input("Sisesta sõna vene keeles: ")
            print(f"Tõlge eesti keelde: {tolgi_rus_est(rus_sona)}")
        elif valik == "3":
            lisa_sona()
        elif valik == "4":
            paranda_sona()
        elif valik == "5":
            testi_teadmisi()
        elif valik == "6":
            print("Nägemist!")
            break
        else:
            print("Vale valik, proovi uuesti.")

if __name__ == "__main__":
    main()

