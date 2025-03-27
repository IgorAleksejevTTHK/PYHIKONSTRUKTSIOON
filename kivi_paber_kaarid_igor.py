import random

while True:
    print("1. Alustada mangu")
    print("2. Lopetada mangu")

    choice = input("Sisesta 1-2: ")

    
    kivi = 1
    kaarid = 2
    paber = 3

    
    if choice == "1":  
        print("Kivi - 1")
        print("Kaarid - 2")
        print("Paber - 3")
        move1 = input("Sisestage Arv 1-3: ")
        
        if move1 == "1":  
            move1 = kivi
        elif move1 == "2":
            move1 = kaarid
        elif move1 == "3":
            move1 = paber
        else:
            print("Vale valik. Palun sisestage arv 1-3.")
            continue  
        
        move2 = random.choice([kivi, kaarid, paber])  
        print(f"Teie valik: {move1}, Arvuti valik: {move2}")

        if move1 == kivi:
            if move2 == kaarid:
                print("Te voitsite")
            elif move2 == paber:
                print("Arvuti voitis")
            else:
                print("Viik")
        
        elif move1 == kaarid:
            if move2 == paber:
                print("Te voitsite")
            elif move2 == kivi:
                print("Arvuti voitis")
            else:
                print("Viik")
        
        elif move1 == paber:
            if move2 == kivi:
                print("Te voitsite")
            elif move2 == kaarid:
                print("Arvuti voitis")
            else:
                print("Viik")
    elif choice == "2":  
        print("Mang lopetatud.")
        break
    else:
        print("Vale valik. Proovi uuesti.")
