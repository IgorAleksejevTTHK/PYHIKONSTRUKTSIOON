from time import *
#v5 3.
for o in range(20):
    print(f"Soritab eksamit {o+1}. opilane")
    for e in range(3):
        print(f"{e+1}. eksam")

#v4 2.
vastus=0
P=int(input("mitu korda kordame"))
while True:
    arv=float(input("sisesta arv: "))
    if arv<0: vastus+=arv
    p-=1
    if P==0: break
print("Suma on: ", vastus)

#v1 4.
kokku=int(input("kokku kotlete: "))
panni_maht=int(input("panni maht: "))
aeg=1
lahenemine=kokku//panni_maht
jaak=kokku%panni_maht
if jaak>0: lahenemine+=1
print(f"praeme. tuleb {lahenemine} lahenemist")

for l in range(lahenemine):
    print(f"{l+1}. lahemine. praeme esimene pool")
    sleep(aeg)
    print("umberpooramine")
    print(f"{l+1}. lahemine. praeme teine pool")
    sleep(aeg)
    print(f"valmis")
print("koik kotletid on praetud")

#v2 2.