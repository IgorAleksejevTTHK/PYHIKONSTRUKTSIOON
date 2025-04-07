from module1 import *

palgad = [1200, 2500, 750, 395, 1200]
inimesed = ["A", "B", "C", "D", "E"]

def menu():
    while True:
        print("\n--- Menü ---")
        print("1. Andmete lisamine")
        print("2. Andmete kustutamine")
        print("3. Suurima palga otsimine")
        print("4. Vaiksema palka otsimine")
        print("5. Palka sorteerimine")
        print("6. Võrdsed palgad")
        print("7. Otsi palka nimist")
        print("8. Otsib kes saavad rohkem/vähem kui määratud summa.")
        print("9. Otsib  vaeseimad ja rikkamad inimesed")
        print("10. Keskmine palk")
        print("11. Välju")
        
        valik = input("Vali tegevus (1-11): ")
        
        if valik == "1":
            lisa_andmed(palgad, inimesed)
        elif valik == "2":
            kustuta_andmed(palgad, inimesed)
        elif valik == "3":
            print(suurem_palk(palgad, inimesed))
        elif valik == "4":
            print(vaiksem_palk(palgad, inimesed))
        elif valik == "5":
            print(sorteeri_palgad(inimesed, palgad))
        elif valik == "6":
            print(võrdsed_palgad(palgad, inimesed))
        elif valik == "7":
            print(otsi_palk(inimesed, palgad))
        elif valik == "8":
            print(filtreeri_palgad(inimesed, palgad))
        elif valik == "9":
            print(top1(inimesed,palgad))
        elif valik == "10":
            print(keskmine_palk(inimesed, palgad))
        elif valik == "11":
            break
        else:
            print("Vale valik, proovi uuesti.")

menu()
