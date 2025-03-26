#v3

def linnad():
    """
    Funktsioon linnad() võimaldab kasutajal lisada linnu ja nende elanike arvu loenditesse
    ning seejärel valida tegevusi: saada teavet elanike arvu kohta, sorteerida linnu,
    leida vähemate elanikega linnad või leida lähim elanike arv.
    """

    
    linnad_list = []  
    elanikud_list = []  

    
    while True:
        linn = input("Sisestage linna nimi või 'lopp' et lõpetada: ") 
        if linn.lower() == "lopp":  
            break
        elanikud = int(input(f"Kui palju elanikke elab linnas {linn}: "))  
        linnad_list.append(linn)  
        elanikud_list.append(elanikud)  


    while True:
        print("\nValige tegevus:")  
        print("1. Uuri elanike arvu linna järgi")  
        print("2. Kuvage linnade tähestikulist nimekirja")  
        print("3. Leidke linnad, kus elab vähem kui n inimest")  
        print("4. Leidke linn elanike arvuga, mis on määratud numbrile kõige lähemal") 
        print("5. Väljuge programmist")  
        valik = input("Sinu valik: ")  
        
        if valik == "1":
            """
            Võimaldab saada teavet konkreetse linna elanike arvu kohta
            """
            linn = input("Sisestage linna nimi: ") 
            if linn in linnad_list:
                index = linnad_list.index(linn)  
                print(f"Linnas {linn} elab {elanikud_list[index]} inimest.")  
            else:
                print("Linna ei leitud.")  
        
        elif valik == "2":
            """
            Kuvab linnade tähestikulise nimekirja
            """
            for i in range(len(linnad_list)):
                for j in range(i + 1, len(linnad_list)):
                     if linnad_list[i] > linnad_list[j]: 
                              elanikud_list[i], elanikud_list[j] = elanikud_list[j], elanikud_list[i] #меняет местами элементы в списке численности населения, для синхронизации с городами в списке.
                              print("Linnad tähestikulises järjekorras:")
            for i in range(len(linnad_list)):
                print(f"{linnad_list[i]}: {elanikud_list[i]} inimest")
            
        
        elif valik == "3":
            """
            Võimaldab leida linnad, kus elanikke on vähem kui antud arv.
            """
            n = int(input("Sisestage number n: ")) 
            print(f"Linnad, kus on vähem kui {n} inimest:")
            for i in range(len(linnad_list)):
                if elanikud_list[i] < n: 
                    print(f"{linnad_list[i]}: {elanikud_list[i]} inimest")  
        
        elif valik == "4":
            """
            Находит город с числом жителей, наиболее близким к заданному числу.
            Leiab linna, mille elanike arv on kõige lähemal antud arvule.
            """
            siht_elanikud = int(input("Sisestage elanike arv: "))  
            lähim_linn = linnad_list[0] 
            if minimaalne_vahe < 0:
                minimaalne_vahe = -minimaalne_vahe  # Если разница отрицательная, превращаем её в положительную
            for i in range(1, len(elanikud_list)):
                vahe = elanikud_list[i] - siht_elanikud  # Вычисляем разницу 
                if vahe < 0:
                    vahe = -vahe
                    if vahe < minimaalne_vahe:  # Если нашли город с меньшей разницей
                        minimaalne_vahe = vahe  # Обновляем минимальную разницу
                        lähim_linn = linnad_list[i]
            print(f"Linn, mille elanike arv on kõige lähem: {lähim_linn}")
        
        elif valik == "5":
            """
            Lõpetab programmi.
            """
            print("Programmist väljumine.")  
            break
        
        else:
            print("Vale valik, proovige uuesti.")  


linnad()
