import math  # 1. Muutsin "import * from math" "import math"-iks, et kasutada "math.sqrt"
print("Ruudu karakteristikud")
while True:
    a = input('Sisesta ruudu külje pikkus => ')
    try:
        a = float(a)  # Muudan sisendi arvuks
        if (a <= 0):  # Kontrollin, et pikkus oleks suurem kui 0
            print("Pikkus peab olema suurem kui 0")
            continue
        break
    except:
        print("Palun sisesta õige number")
S = a**2  # Arvutan ruudu pindala
print("Ruudu pindala", S)
P = 4 * a  # Arvutan ruudu ümbermõõdu
print("Ruudu ümbermõõt", P)
di = a * math.sqrt(2)  # 3. Muutsin "sqr" õigeks funktsiooniks "sqrt"
print("Ruudu diagonaal", round(di, 2))
print()

print("Ristküliku karakteristikud")
while True:
    b = input("Sisesta ristküliku 1. külje pikkus => ")
    c = input("Sisesta ristküliku 2. külje pikkus => ")
    try:
        b = float(b)  # Muudan esimese külje sisendi arvuks
        c = float(c)  # Muudan teise külje sisendi arvuks
        if (b <= 0 or c <= 0):  # Kontrollin, et mõlemad küljed oleksid positiivsed
            print("Pikkus peab olema suurem kui 0")
            continue
        break
    except:
        print("Palun sisesta õige number")
S = b * c  # Arvutan ristküliku pindala
print('Ristküliku pindala', S)
P = 2 * (b + c)  # 6. Kasutan õiget korrutamise süntaksit
print("Ristküliku ümbermõõt", P)
di = math.sqrt(b**2 + c**2)  # 7. Kasutan õiget valemit diagonaali jaoks
print("Ristküliku diagonaal", round(di, 1))  # 8. Lisasin puuduoleva sulgu ja ümardasin ühe koma täpsusega
print()

print("Ringi karakteristikud")
while True:
    r = input("Sisesta ringi raadiusi pikkus => ")
    try:
        if (r <= 0):  # Kontrollin, et raadius oleks suurem kui 0
            print("Raadius peab olema suurem kui 0")
            continue
        r = float(r)  # Muudan raadiuse sisendi arvuks
        break
    except:
        print("Palun sisesta õige number")
d = 2 * r  # Arvutan ringi läbimõõdu
print("Ringi läbimõõt", d)
S = math.pi * r**2  # 12. Kasutan õiget valemit ringi pindala jaoks
print("Ringi pindala", round(S, 2))  # 13. Ümardan pindala kahe komakoha täpsusega
C = 2 * math.pi * r  # Arvutan ringi ümbermõõdu
print("Ringjoone pikkus", round(C, 2))  # 14. Lisasin puuduoleva sulgu

