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





def kas_nimi_kehtib(nimi):
    return nimi.isalpha()


nimi1 = input("sisesta esimene nimi: ")
nimi2 = input("sisesta teine nimi: ")


if kas_nimi_kehtib(nimi1) and kas_nimi_kehtib(nimi2):
  
    if (nimi1 == "igor" and nimi2 == "nikita") or (nimi1 == "igor" and nimi2 == "nikita"):
        print("nikita ja igor on tana pinginaabrid")
    else:
        print("Need inimesed ei ole tana pinginaabrid")
else:
    print("Palun sisesta nimed, mis sisaldavad ainult tahti")
