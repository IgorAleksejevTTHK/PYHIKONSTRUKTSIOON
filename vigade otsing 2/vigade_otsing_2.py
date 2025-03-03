print("*** SASAL? ***")  
print()

#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while True:
    try:
        a = abs(int(input("Sisesta täisarv => ")))  
        break  
    except ValueError:
        print("See ei ole täisarv")  
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

if a == 0:
    print("Nulliga pole mõtet midagi teha")  
else:
    #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrame, mitu paaris ja mitu paaritu numbrit on arvus")  
    print()
    c = b = a  
    paaris = 0  
    paaritu = 0  

    while b > 0:  
        if b % 2 == 0:  
            paaris += 1  
        else:
            paaritu += 1
        b = b // 10 
    print("Paaris numbreid:", paaris)  
    print("Paaritu numbreid:", paaritu) 
    print()

    #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Pöörame sisestatud numbrit ümber") 
    print()
    b = 0  

    while a > 0:  
        number = a % 10 
        a = a // 10  
        b = b * 10 
        b += number  

    print("Ümberpööratud number:", b) 
    print()

    #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Kontrollime Syracuse hüpoteesi")  
    print()

    if c % 2 == 0: 
        print("c on paarisarv. Jagame 2-ga.")  
    else:
        print("c on paaritu arv. Korrutame 3-ga, liidame 1 ja jagame 2-ga.")  

    while c != 1: 
        sleep(1) # 1 sek
        if c % 2 == 0: 
            print('{:>4}'.format(round(c)),"- paaris arv, jagame 2." )
            c = c // 2 
        else:
              print('{:>4}'.format(round(c)),"- paaritu arv. korrutame 3, liidame 1 ja jagame 2." )
              c = (3 * c + 1) // 2  
        print(c, end=" ") 
    print()
    print("Hüpotees kehtib")  