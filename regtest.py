import MyModule
while True:
        print("\nRegtest menüü:")
        print("1. Registreerimine")  
        print("2. Autoriseerimine")  
        print("3. Välju")  

        choice = input("Valige toiming (1/2/3): ").strip()

        if choice == "1":
            register_user(logins, passwords)
        elif choice == "2":
            authorize_user(logins, passwords)
        elif choice == "3":
            print("Nägemist!")
            break
        else:
            print("Vale valik, proovi uuesti.")


