
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

#---------------------------------------
# ulesanne 3
def remont():
    pikkus = float(input("Sisesta toa pikkus meetrites: "))
    laius = float(input("Sisesta toa laius meetrites: "))
    pindala = pikkus * laius
    print(f"Toa pindala on {pindala} ruutmeetrit.")
    
    soov = input("Kas soovite remonti teha? (jah/ei): ")
    if soov.lower() == 'jah':
        hind = float(input("Sisesta ruutmeetri hind: "))
        koguhind = hind * pindala
        print(f"Põranda vahetamise hind on {koguhind} eurot.")
       
#---------------------------------------
# ulesanne 4
def allahindus():
    alg_hind = float(input("Sisesta alghind: "))
    if alg_hind > 700:
        soodus_hind = alg_hind * 0.7
        print(f"30% soodushind on {soodus_hind} eurot.")
    else:
        print("Alghind ei ole suurem kui 700.")

#---------------------------------------
# ulesanne 5
def temperatuur():
    temp = float(input("Sisesta temperatuur: "))
    if temp > 18:
        print("Temperatuur on üle 18 kraadi (soovitav toasoojus talvel).")
    else:
        print("Temperatuur ei ole üle 18 kraadi.")


#---------------------------------------
# ulesanne 6
def pikkus():
    height = float(input("Sisesta oma pikkus sentimeetrites: "))
    if height < 160:
        print("Sa oled lühike.")
    elif 160 <= height <= 180:
        print("Sa oled keskmine.")
    else:
        print("Sa oled pikk.")

#---------------------------------------
# ulesanne 7
def pikkus_ja_sugu():
    height = float(input("Sisesta oma pikkus sentimeetrites: "))
    gender = input("Sisesta oma sugu (mees/naine): ").lower()
    
    if gender == "mees":
        if height < 165:
            print("Sa oled lühike mees.")
        elif 165 <= height <= 185:
            print("Sa oled keskmine mees.")
        else:
            print("Sa oled pikk mees.")
    elif gender == "naine":
        if height < 155:
            print("Sa oled lühike naine.")
        elif 155 <= height <= 175:
            print("Sa oled keskmine naine.")
        else:
            print("Sa oled pikk naine.")
    else:
        print("Tundmatu sugu.")

#---------------------------------------
# ulesanne 8
def poes():
    items = {"piim": random.randint(50, 100) / 10, "sai": random.randint(50, 100) / 10, "leib": random.randint(50, 100) / 10}
    total = 0
    print("Poe tooted ja hinnad (eurodes):")
    for item, price in items.items():
        print(f"{item.capitalize()}: {price}€")
        quantity = int(input(f"Kui palju {item} soovid osta? "))
        total += price * quantity
    
    print(f"Kokku maksad: {total}€")

#---------------------------------------
# ulesanne 9

def ruut():
    side1 = float(input("Sisesta esimene külg: "))
    side2 = float(input("Sisesta teine külg: "))
    if side1 == side2:
        print("Need küljed moodustavad ruudu.")
    else:
        print("Need küljed ei moodusta ruudu.")

    #--------------------------------------- 
    # ulesanne 10

def matemaatika():
    number1 = float(input("Sisesta esimene arv: "))
    number2 = float(input("Sisesta teine arv: "))
    operation = input("Sisesta tehe (+, -, *, /): ")
    
    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2
    elif operation == '/':
        if number2 != 0:
            result = number1 / number2
        else:
            print("Nulliga jagamine on voimatu.")
            return
    else:
        print("Tundmatu tehe.")
        return
    
    print(f"Tulemus: {result}")

    #--------------------------------------- 
    # ulesanne 11

    
def juubel():
   birth_year = int(input("Sisesta oma sunniaasta: "))
   current_year = 2025  # Current year
   age = current_year - birth_year
    
if age % 5 == 0:
        print(f"Tegemist on juubeliga, vanus on {age} aastat.")
else:
        print(f"Ei ole juubel, vanus on {age} aastat.")

     #---------------------------------------
     # ulesanne 12

def muuk():
         price = float(input("Sisesta toote hind: "))
    
if price <= 10:
        final_price = price * 0.9
else:
        final_price = price * 0.8
    
print(f"Toote loplik hind on {final_price} eurot.")

     #---------------------------------------
     # ulesanne 13

def jalgpalli_meeskond():
    gender = input("Sisesta oma sugu (mees/naine): ").lower()
    
    if gender == "mees":
        age = int(input("Sisesta oma vanus: "))
        if 16 <= age <= 18:
            print("Sobid meeskonda.")
        else:
            print("Ei sobi meeskonda.")
    elif gender == "naine":
        print("Naissoost kandidaate ei küsita vanust.")
    else:
        print("Tundmatu sugu.")

     #---------------------------------------
     # ulesanne 14

def busside_logistika():
    people = int(input("Sisesta inimeste arv: "))
    bus_capacity = int(input("Sisesta bussi kohtade arv: "))
    
    buses_needed = (people + bus_capacity - 1) // bus_capacity
    last_bus_passengers = people % bus_capacity or bus_capacity
    
    print(f"Vaja on {buses_needed} bussi.")
    print(f"Viimases bussis on {last_bus_passengers} inimest.")
