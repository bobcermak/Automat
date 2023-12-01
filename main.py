
import time
 
 
while True:
    print("Vyber si produkt: ")
    time.sleep(1)
 
    print("Kola - 1 - 30kc",        "Jahoda. juice -2 - 40kc",      "Pomeranc.Juice - 3 - 30kc",        "Fanta - 4 - 50kc")
    produkt = input("Zvol si produkt: ")
 
    time.sleep(1)
 
    if produkt == "":
        print("Produkt nebyl vybrán")
        time.sleep(1)
 
    elif produkt in ["a", "b" , "c" , "d"]:
        print("Zadal jste špatný prvek")
       
 
    elif type(produkt) == str:
        if produkt == "1":
            print("Váš produkt je Kola, poprosim vas o 30kc")
 
        if produkt == "2":
            print("Váš produkt je Jahoda Juice, poprosim vas o 40kc")
 
        if produkt == "3":
            print("Váš produkt je pomeranc.Juice, poprosim vas o 30kc")
 
        if produkt == "4":
            print("Váš produkt je fanta, poprosim vas o 500kc")
       
        print("Poprosím vhoďte peníze")
        break
       
     
   