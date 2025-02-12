from random import *
#näidis 1
arv=randint(0,10)
print(arv)
if arv>5:
    print("***********************")
    print(f"arv {arv} suurem kui 5")
    print("***********************")
if arv>5: print("arv {arv} suurem kui 5")

#Näidis 2
arv=randint(-10,10)
if arv>0:
    print("Positiivne")
else:
    print("Negatiivne")

if arv>0:
    print("Positiivne")
elif arv==0:
    print("0")
else:
    print("negatiivne")

 # nimi kontrollimine
nimi = input("Sisesta eesnimi: ")

if nimi.upper() == "JUKU":
    print("Lahme Jukuga kinno.")
else:
    print("Oi, mul vaja minna.")

# vanuse kontroll
vanus_input = input("kui vana sa oled: ")

if vanus_input.isdigit():
    vanus = int(vanus_input)
    
    if vanus < 6:
        print(" tasuta.")
    elif 6 <= vanus <= 14:
        print(" lastepilet.")
    elif 15 <= vanus <= 65:
        print(" taispilet.")
    elif vanus > 65:
        print(" sooduspilet.")
    else:
        print("vanus ei saa olla negatiivne ega rohkem kui 100.")
else:
    print("sisesta palun kehtiv taisarv.")
