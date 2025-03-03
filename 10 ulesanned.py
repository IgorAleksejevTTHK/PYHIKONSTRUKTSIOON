#1 Вводят 15 чисел. Определить, сколько среди них целых.
taisarvud=0        
for i in range(3): 
    while True:
        try:
           arv=float(input(f"Sisesta {i+1}. arv"))
           break
        except:
             print("kirjuta ainult numbrid")
        if arv==int(arv):
            taisarvud+=1
print(f"Taisarvude kogus: {taisarvud}")

#2 Запросите у пользователя число А и найдите сумму всех натуральных чисел от 1 до А.
A = int(input("sisesta arv: "))
if A>0:
    summa = sum(range(1, A + 1))
    print("summa 1. kuni", A, "on", summa)
else:
    print("Число должно быть натуральным (больше 0).")

#14 Составьте программу, которая вычисляет произведение чисел от 1 до N. Значение N создается случайным образом.
import random

N=random.randint(1, 100)
if N > 0:
        summa = sum(range(1, N + 1))
        print("summa 1. kuni", N, "on", summa)
else:
    print("midagi läks valesti")

#3 Вводят 8 чисел. Найти их произведение (только положительных).
arv = 1
for _ in range(8):
    num = float(input("sisestage arv: "))
    if num > 0:
        arv *= num
print("Произведение положительных чисел:", arv)
 
#5.    Составьте программу, которая вычисляет сумму только отрицательных из N чисел. Значение N вводится с клавиатуры

summa = 0
while True:
    try:
        N = int(input("Sisesta N: "))
        if N>=1:
            for i in range(1,N+1):
                arv=float(input(f"Sisesta {i}. arv"))
                if arv<0:
                    summa+=arv
            print(f"summa vordub {summa}")
            break
        else:
            print("N peab olema suurem kui 1")
    except:
            print("vale formaat")

#9.    В банк на трехпроцентный вклад положили S евро. Какой станет сумма вклада через N лет?

S = float(input("Sisestage deposiiti: "))
N = int(input("Sisestage aastad: "))

vklad = 0.03
fin_summa = S * (1 + vklad) ** N

print("Будущий депозит через", N, "лет будет", fin_summa, "евро")


#17.Напишите программу, печатающую столбик таблицу умножения такого вида:
#2*1=2
#2*2=4
#2*3=6


for i in range(1, 10):
    print(f"2*{i}={2*i}")

    #15 Написать программу, выводящую в столбик десять строк, в каждой печатая цифры от 0 до 9, то есть в таком виде:
    for j in range(10):
        for i in range(10):
            print(i, end=" ")
        print()
print()

# 11.Найти произведение двузначных нечетных чисел, кратных случайно сгенерированному числу.
import random

N = random.randint(10, 99)
arv = 1

for i in range(10, 100, 2):
    if i % N == 0:
        arv *= i

print("произведение двузначных нечетных чисел, кратных", N, "равно", arv)


numbers = [num for num in range(100, 1001) if num % 7 == 0]


count = len(numbers)


total_sum = sum(numbers)


print("количество чисел, кратных 7:", count)
print("сумма чисел, кратных 7:", total_sum)
