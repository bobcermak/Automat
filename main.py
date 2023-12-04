


import time


badPrize = "5"
kola = "30"
jahoda = "40"
pomeranc = "30"
fanta = "50"

timer = 0

            
 
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
            if ikola > kola:
                negrk = int(ikola) - int(kola)
                print("Zde je vaše vrácená částka " + str(negrk) + " Kč")
                print("Vaše objednávka je potvrzena, přeji hezký zbytek dne :)")
                break
            elif ikola < kola:
                negrko = int(kola) - int(ikola)
                innegrko = input("Chybí vám ještě " + str(negrko) + " Kč: ")
                if str(negrko) == str(innegrko):
                    print("Vaše částka je dostačující")
                    print("Vaše objednávka je potvrzena, přeji hezký zbytek dne :)")
                    break
                elif str(innegrko) != str(negrko):
                    aut = int(negrko) - int(innegrko)
                    najme = input("Vaše částka je nedostatečná, ještě přidejte " + str(aut) + " Kč: ")
                    if str(aut) != str(najme):                                                          #pokud nfunguje if/elif/else = zkusit dat do sebe
                        print("Váš nákup proběhl neúspěšně")
                        print("Zde máte vámi vhozené peníze, přeji hezký zbytek dne :)")
                        break
                    elif str(aut) == str(najme):
                        print("Vaše objednávka je potvrzena, přeji hezký zbytek dne :)")
                        break
                    
                    
                
            elif ikola == kola:
                print("Vaše objednávka je potvrzena, přeji hezký zbytek dne :)")  #VZDY DAVAT IF do sebe (nesmí přečahovat)
                break


 
        elif produkt == "2":
            print("Váš produkt je Jahoda.juice, poprosim vas o 40 Kč")
            time.sleep(1)
            ijahod = str(input("Prosím vhoďte "+jahoda+" Kč: "))
            print("Vhodil jste " + ijahod +" Kč")
            if ijahod > jahoda:
                negrke = int(ijahod) - int(jahoda)
                print("Zde je vaše vrácená částka " + str(negrke) + " Kč")
                print("Vaše objednávka je potvrzena, přeji hezký zbytek dne :)")
                break
            elif ijahod < jahoda:
                negrkeo = int(jahoda) - int(ijahod)
                innegrkeo = input("Chybí vám ještě " + str(negrkeo) + " Kč: ")
                if str(negrkeo) == str(innegrkeo):
                    print("Vaše částka je dostačující")
                    print("Vaše objednávka je potvrzena, přeji hezký zbytek dne :)")
                    break
                elif str(innegrkeo) != str(negrkeo):
                    auto = int(negrkeo) - int(innegrkeo)
                    najmen = input("Vaše částka je nedostatečná, ještě přidejte " + str(auto) + " Kč: ")
                    if str(auto) != str(najmen):                                                          #pokud nfunguje if/elif/else = zkusit dat do sebe
                        print("Váš nákup proběhl neúspěšně")
                        print("Zde máte vámi vhozené peníze, přeji hezký zbytek dne :)")
                        break
                    elif str(auto) == str(najmen):
                        print("Vaše objednávka je potvrzena, přeji hezký zbytek dne :)")
                        break
                    
                    
                
            elif ijahod == jahoda:
                print("Vaše objednávka je potvrzena, přeji hezký zbytek dne :)")  #VZDY DAVAT IF do sebe (nesmí přečahovat)
                break
 



 
        elif produkt == "3":
            print("Váš produkt je Pomeranc.juice, poprosim vas o 30 Kč")
            time.sleep(1)
            ipomeranc = str(input("Prosím vhoďte "+pomeranc+" Kč: "))
            print("Vhodil jste " + ipomeranc +" Kč")
            if ipomeranc > pomeranc:
                negrkp = int(ipomeranc) - int(pomeranc)
                print("Zde je vaše vrácená částka " + str(negrkp) + " Kč")
                print("Vaše objednávka je potvrzena, přeji hezký zbytek dne :)")
                break
            elif ipomeranc < pomeranc:
                negrkpo = int(pomeranc) - int(ipomeranc)
                innegrkpo = input("Chybí vám ještě " + str(negrkpo) + " Kč: ")
                if str(negrkpo) == str(innegrkpo):
                    print("Vaše částka je dostačující")
                    print("Vaše objednávka je potvrzena, přeji hezký zbytek dne :)")
                    break
                elif str(innegrkpo) != str(negrkpo):
                    autos = int(negrkpo) - int(innegrkpo)
                    najmeno = input("Vaše částka je nedostatečná, ještě přidejte " + str(autos) + " Kč: ")
                    if str(autos) != str(najmeno):                                                          #pokud nfunguje if/elif/else = zkusit dat do sebe
                        print("Váš nákup proběhl neúspěšně")
                        print("Zde máte vámi vhozené peníze, přeji hezký zbytek dne :)")
                        break
                    elif str(autos) == str(najmeno):
                        print("Vaše objednávka je potvrzena, přeji hezký zbytek dne :)")
                        break
                    
                    
                
            elif ipomeranc == pomeranc:
                print("Vaše objednávka je potvrzena, přeji hezký zbytek dne :)")  #VZDY DAVAT IF do sebe (nesmí přečahovat)
                break
            
 


        elif produkt == "4":
            print("Váš produkt je Fanta, poprosím vás o 50Kč")
            time.sleep(1)
            ifanta = str(input("Prosím vhoďte "+fanta+" Kč: "))
            print("Vhodil jste " + ifanta +" Kč")
            if ifanta > fanta:
                negrf = int(ifanta) - int(fanta)
                print("Zde je vaše vrácená částka " + str(negrf) + " Kč")
                print("Vaše objednávka je potvrzena, přeji hezký zbytek dne :)")
                break
            elif ifanta < fanta:
                negrkfo = int(fanta) - int(ifanta)
                innegrfo = input("Chybí vám ještě " + str(negrkfo) + " Kč: ")
                if str(negrkfo) == str(innegrfo):
                    print("Vaše částka je dostačující")
                    print("Vaše objednávka je potvrzena, přeji hezký zbytek dne :)")
                    break
                elif str(innegrfo) != str(negrkfo):
                    autosi = int(negrkfo) - int(innegrfo)
                    najmenos = input("Vaše částka je nedostatečná, ještě přidejte " + str(autosi) + " Kč: ")
                    if str(autosi) != str(najmenos):                                                          #pokud nfunguje if/elif/else = zkusit dat do sebe
                        print("Váš nákup proběhl neúspěšně")
                        print("Zde máte vámi vhozené peníze, přeji hezký zbytek dne :)")
                        break
                    elif str(autosi) == str(najmenos):
                        print("Vaše objednávka je potvrzena, přeji hezký zbytek dne :)")
                        break
                    
                    
                
            elif ifanta == fanta:
                print("Vaše objednávka je potvrzena, přeji hezký zbytek dne :)")  #VZDY DAVAT IF do sebe (nesmí přečahovat)
                break
            



        elif produkt == "":
            print("Produkt nebyl vybrán")
            time.sleep(1) 
    



        elif produkt != ("1","2","3","4"):
            print("Zadal jste špatný prvek")
            time.sleep(1)
            


while False:
    print("Automat mimo provoz!!!")

            
    

    


    
    

    

        
       
     
   