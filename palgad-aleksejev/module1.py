  
p=[]
i=[]

def lisa_andmed(p:list,i:list):
    """
    lisame palka ja inimesi
    """
    while True:
        try:
            nimi=input("Nimi: ")
            if nimi.isalpha():
                try:
                    palk=float(input("Palk: "))
                except:
                       print("Palk on arv")
                break
        except:
            print("Kirjuta ainult tahtede kasutades")

    p.append(palk)
    i.append(nimi)

def kustuta_andmed(p:list,i:list):
    """
    kustutame palka ja inimesi
    """
    while True:
        nimi = input("Nimi: ")
        if nimi.isalpha():
            break
        else:
            print("Kirjuta ainult tähti kasutades.")

    if nimi in i:
        indeks = i.index(nimi)  
        i.pop(indeks)  
        p.pop(indeks)  
        print("Andmed on kustutatud.")
    else:
        print("Andmed ei leitud.")


def suurem_palk(p:list,i:list):
    """
    leiab kõige suurem palk
    """ 
    suurim_palk = max(p)
    indeks = p.index(suurim_palk)
    suurim_nimi = i[indeks]
    
    return f"Kõige suurem palk {suurim_palk} saab {suurim_nimi}"

def vaiksem_palk(p:list,i:list):
    """
    leiab kõige väiksem palk
    """ 
    väikseim_palk = min(p)
    indeks = p.index(väikseim_palk)
    väikseim_nimi = i[indeks]
    
    return f"Kõige väiksem palk {väikseim_palk} saab {väikseim_nimi}"

def sorteeri_palgad(i: list, p: list):
    """
    Järjestab palgad kasvavas ja kahanevas järjekorras 
    """
    while True:
        v = input("Vali märk: > (kasvav) või < (kahanev): ")
        if v in [">", "<"]:
            break
        else:
            print("Vale märk! Palun sisesta '>' või '<'.")

    for n in range(len(i)): 
        for m in range(len(i)):
            if v == ">":
                if p[n] > p[m]:
                    i[n], i[m] = i[m], i[n]
                    p[n], p[m] = p[m], p[n]
            elif v == "<":
                if p[n] < p[m]:
                    i[n], i[m] = i[m], i[n]
                    p[n], p[m] = p[m], p[n]

def võrdsed_palgad(p:list,i:list):
    """
    leiab võrdsed palgad
    """
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] == p[j]:
                print(f"{i} ja {j} on võrdsed palgad")

    hulk = set(p)
    for palk in hulk:
        k = p.count(palk)
        if k > 1:
            print(f"Palk {palk}")
            ind = p.index(palk)
            for j in range(k):
                ind = p.index(palk, ind)
                print(f"Saab kätte {p[ind]}")

def otsi_palk(i: list, p: list):
    """
    Leiab palka nimist
    """
    nimi = input("Sisesta nimi, kelle palka otsida: ")  

    if not i or not p or len(i) != len(p):
        return "Vale andmed."

    tulemused = []  

    for indeks, nimi_i in enumerate(i):
        if nimi_i == nimi:
            tulemused.append(p[indeks])

    if tulemused:
        return f"{nimi} saab palka: {tulemused}"
    else:
        return f"{nimi} ei leitud nimekirjas."

def filtreeri_palgad(i: list, p: list):
    """
    Küsib kasutajalt summa ja filtreerib inimesed vastavalt palgale.
    """
    while True:
        try:
            summa = float(input("Sisesta summa filtreerimiseks: "))
            break
        except ValueError:
            print("Viga! Palun sisesta arvuline väärtus.")

    while True:
        tingimus = input("Vali tingimus '>' (suurem) või '<' (väiksem): ")
        if tingimus in [">", "<"]:
            break
        else:
            print("Viga! Palun sisesta ainult '>' või '<'.")

    tulemused = []  

    for indeks, palk in enumerate(p):
        if tingimus == ">" and palk > summa:
            tulemused.append((i[indeks], palk))
        elif tingimus == "<" and palk < summa:
            tulemused.append((i[indeks], palk))

    if tulemused:
        print(f"\nInimesed, kelle palk on {tingimus} {summa}:")
        for nimi, palk in tulemused:
            print(f"{nimi}: {palk}")
    else:
        print(f"\nÜhtegi inimest palgaga {tingimus} {summa} ei leitud.")


def top1(i: list, p: list, t: int):
    """
    leiab  T vaeseimad ja rikkamad inimesed/
    """
    if not i or not p or len(i) != len(p):
        return "Vale andmed."

    andmed = list(zip(i, p))

    for n in range(len(andmed) - 1):
        for m in range(len(andmed) - 1 - n):
            if andmed[m][1] > andmed[m + 1][1]:
                andmed[m], andmed[m + 1] = andmed[m + 1], andmed[m]

    vaeseimad = andmed[:t]
    rikkamad = andmed[-t:]

    return vaeseimad, rikkamad


 


    