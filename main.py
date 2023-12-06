


import time


badPrize = "5"
kola = "30"
jahoda = "40"
pomeranc = "30"
fanta = "50"
            



            
 
while True:
    print("Vyber si produkt: ")
    time.sleep(1)
 
    print("Kola - 1 - 30 Kč",        "Jahoda.juice - 2 - 40 Kč",      "Pomeranc.juice - 3 - 30 Kč",        "Fanta - 4 - 50 Kč")
    produkt = input("Zvol si produkt: ")
 
    time.sleep(1)
 

    if type(produkt) == str:
        if produkt == "1":
            print("Váš produkt je Kola, poprosim vas o 30 Kč")  #vzdy pojmenovavat INPUT
            time.sleep(1)
            ikola = str(input("Prosím vhoďte "+kola+" Kč: "))
            print("Vhodil jste " + ikola +" Kč")
            while (int(ikola) < int(kola)):
                kola = int(kola) - int(ikola)
                ikola = input("Chybí vám ještě " + str(kola) + "Kč: ")

            while (int(ikola) > int(kola)):
                kola = int(ikola) - int(kola)
                print("Zde je vaše vrácená částka " + str(kola) + " Kč, přeji hezký zbytek dne :) ")
                time.sleep(1)
                break

            if (int(ikola) == int(kola)):
                print("Vaše objednávka je potvrzena, přeji hezký zbytek dne :)")
                time.sleep(1)


 
        elif produkt == "2":
            print("Váš produkt je Jahoda.juice, poprosim vas o 40 Kč")
            time.sleep(1)
            ijahod = str(input("Prosím vhoďte "+jahoda+" Kč: "))
            print("Vhodil jste " + ijahod +" Kč")
            while (int(ijahod) < int(jahoda)):
                jahoda = int(jahoda) - int(ijahod)
                ijahod = input("Chybí vám ještě " + str(jahoda) + "Kč: ")

            while (int(ijahod) > int(jahoda)):
                jahoda = int(ijahod) - int(jahoda)
                print("Zde je vaše vrácená částka " + str(jahoda) + " Kč, přeji hezký zbytek dne :) ")
                time.sleep(1)
                break

            if (int(ijahod) == int(jahoda)):
                print("Vaše objednávka je potvrzena, přeji hezký zbytek dne :)")
                time.sleep(1)
 



 
        elif produkt == "3":
            print("Váš produkt je Pomeranc.juice, poprosim vas o 30 Kč")
            time.sleep(1)
            ipomeranc = str(input("Prosím vhoďte "+pomeranc+" Kč: "))
            print("Vhodil jste " + ipomeranc +" Kč")

            while (int(ipomeranc) < int(pomeranc)):
                pomeranc = int(pomeranc) - int(ipomeranc)
                ipomeranc = input("Chybí vám ještě " + str(pomeranc) + "Kč: ")

            while (int(ipomeranc) > int(pomeranc)):
                pomeranc = int(ipomeranc) - int(pomeranc)
                print("Zde je vaše vrácená částka " + str(pomeranc) + " Kč, přeji hezký zbytek dne :) ")
                time.sleep(1)
                break

            if (int(ipomeranc) == int(pomeranc)):
                print("Vaše objednávka je potvrzena, přeji hezký zbytek dne :)")
                time.sleep(1)
                    
            
 


        elif produkt == "4":
            print("Váš produkt je Fanta, poprosím vás o 50Kč")
            time.sleep(1)
            ifanta = str(input("Prosím vhoďte "+fanta+" Kč: "))
            print("Vhodil jste " + ifanta +" Kč")
            while (int(ifanta) < int(fanta)):
                fanta = int(fanta) - int(ifanta)
                ifanta = input("Chybí vám ještě " + str(fanta) + "Kč: ")
        
            while (int(ifanta) > int(fanta)):
                fanta = int(ifanta) - int(fanta)
                print("Zde je vaše vrácená částka " + str(fanta) + " Kč, přeji hezký zbytek dne :) ")
                time.sleep(1)
                break
                

            if (int(ifanta) == int(fanta)):
                print("Vaše objednávka je potvrzena, přeji hezký zbytek dne :)")
                time.sleep(1)
                
            



        elif produkt == "":
            print("Produkt nebyl vybrán")
            time.sleep(1) 
    



        elif produkt != ("1","2","3","4"):
            print("Zadal jste špatný prvek")
            time.sleep(1)



while False:
    print("Automat mimo provoz!!!")

            
    

    


    
    

    

        
       
     
   