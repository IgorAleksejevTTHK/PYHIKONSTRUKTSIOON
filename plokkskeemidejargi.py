#v3

#1. Koostage programmi skeem, mille abil arvutatakse ainult positiivsete arvude summa antud Q arvust.

positive_sum = 0

while True:
    q = input("Sisestage arv (voi 'stopp', et lopetada): ")
    if q == "stopp":
        break
    try:
        q = int(q)
        if q > 0:
            positive_sum += q
    except ValueError:
        print("Vale sisend! Palun sisestage kehtiv arv.")

print(f"Ainult positiivsete arvude summa: {positive_sum}")



#2. Määrake H aasta jooksul pangas kogunenud rahasumma, kui Vlad'i esialgne sissemakse oli Y dollarit ja sissemakse tehti tingimustel Z% aastas.  

while True:
    try:
        Y = float(input("Sisestage esialgne sissemakse (dollarit): "))
        Z = float(input("Sisestage intressimaar (%): "))
        H = int(input("Sisestage aastate arv: "))
        break
    except ValueError:
        print("Vale sisend! Palun sisestage arvud korrektselt.")

final_sum = Y
years = 0

while years < H:
    final_sum += final_sum * (Z / 100)
    years += 1

print(f"Rahasumma parast {H} aastat: {final_sum} dollarit")

#3. Arvutage ja väljastage naturaalse rea arvude summa, mis algab arvuga N ja lõpeb arvuga M (arvud N ja M ei ole ette teada, need on kasutaja poolt antud).

while True:
    try:
        algusarv = int(input("Sisestage rea algusarv: "))
        lopparv = int(input("Sisestage rea lopparv: "))
        break
    except ValueError:
        print("Vale sisend! Palun sisestage taisarvud.")

if algusarv > lopparv:
    algusarv, lopparv = lopparv, algusarv

rea_summa = 0
praegune = algusarv

while praegune <= lopparv:
    rea_summa += praegune
    praegune += 1

print(f"Naturaalse rea arvude summa vahemikus {algusarv} kuni {lopparv}: {rea_summa}")
