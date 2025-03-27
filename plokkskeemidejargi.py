#v3

#1. Koostage programmi skeem, mille abil arvutatakse ainult positiivsete arvude summa antud Q arvust.

positive_sum = 0

while True:
    q = input("Sisestage arv (voi 'stopp', et lopetada): ")
    if q == "stopp":
        break
    q = int(q)
    if q > 0:
        positive_sum += q

print(f"Ainult positiivsete arvude summa: {positive_sum}")

#2. M‰‰rake H aasta jooksul pangas kogunenud rahasumma, kui Vlad'i esialgne sissemakse oli Y dollarit ja sissemakse tehti tingimustel Z% aastas.  

Y = float(input("Sisestage esialgne sissemakse (dollarit): "))
Z = float(input("Sisestage intressimaar (%): "))
H = int(input("Sisestage aastate arv: "))


final_sum = Y
years = 0

while years < H:
    final_sum += final_sum * (Z / 100)
    years += 1

print(f"Rahasumma parast {H} aastat: {final_sum} dollarit")

#3. Arvutage ja v‰ljastage naturaalse rea arvude summa, mis algab arvuga N ja lıpeb arvuga M (arvud N ja M ei ole ette teada, need on kasutaja poolt antud).

algusarv = int(input("Sisestage rea algusarv: "))
lıpparv = int(input("Sisestage rea lıpparv: "))


if algusarv > lıpparv:
    temp = algusarv
    algusarv = lıpparv
    lıpparv = temp


praegune = algusarv
rea_summa = 0

while praegune <= lıpparv:
    rea_summa += praegune
    praegune += 1

print(f"Naturaalse rea arvude summa vahemikus {algusarv} kuni {lıpparv}: {rea_summa}")
