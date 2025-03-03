import math  # 1. Muutsin "import * from math" "import math"-iks, et kasutada "math.sqrt"

def ruudu_karakteristikud():
    a = float(input('Sisesta ruudu külje pikkus => '))
    if a <= 0:
        print("Pikkus peab olema suurem kui 0")
    else:
        S = a**2  # Arvutan ruudu pindala
        print("Ruudu pindala", S)
        P = 4 * a  # Arvutan ruudu ümbermõõdu
        print("Ruudu ümbermõõt", P)
        di = a * math.sqrt(2)  # 3. Muutsin "sqr" õigeks funktsiooniks "sqrt"
        print("Ruudu diagonaal", round(di, 2))
        print()

def ristkyliku_karakteristikud():
    b = float(input("Sisesta ristküliku 1. külje pikkus => "))
    c = float(input("Sisesta ristküliku 2. külje pikkus => "))
    if b <= 0 or c <= 0:
        print("Pikkus peab olema suurem kui 0")
    else:
        S = b * c  # Arvutan ristküliku pindala
        print('Ristküliku pindala', S)
        P = 2 * (b + c)  # 6. Kasutan õiget korrutamise süntaksit
        print("Ristküliku ümbermõõt", P)
        di = math.sqrt(b**2 + c**2)  # 7. Kasutan õiget valemit diagonaali jaoks
        print("Ristküliku diagonaal", round(di, 1))  # 8. Lisasin puuduoleva sulgu ja ümardasin ühe koma täpsusega
        print()

def ringi_karakteristikud():
    r = float(input("Sisesta ringi raadiusi pikkus => "))
    if r <= 0:
        print("Raadius peab olema suurem kui 0")
    else:
        d = 2 * r  # Arvutan ringi läbimõõdu
        print("Ringi läbimõõt", d)
        S = math.pi * r**2  # 12. Kasutan õiget valemit ringi pindala jaoks
        print("Ringi pindala", round(S, 2))  # 13. Ümardan pindala kahe komakoha täpsusega
        C = 2 * math.pi * r  # Arvutan ringi ümbermõõdu
        print("Ringjoone pikkus", round(C, 2))  # 14. Lisasin puuduoleva sulgu

ruudu_karakteristikud()
ristkyliku_karakteristikud()
ringi_karakteristikud()
