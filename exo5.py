# TODO : Créer un système d'alerte qui demande le niveau de charge de la batterie, affiche une représentation graphique si la charge est entre 0 et 100%, et affiche un message d'erreur en cas de charge en dehors de la plage normale.

niveau_charge = int(input("Entrez le niveau de charge actuel de la batterie :"))
a= '❚'
if (0<= niveau_charge< 5) :
    print([     ])
    print(niveau_charge,"%")

elif (5<= niveau_charge < 15) :
    print(f"[{a}]")
    print(niveau_charge, "%")

elif (15<= niveau_charge<25):
    print(f"[{a*2}]")
    print(niveau_charge, "%")

elif (25<= niveau_charge<35):
    print(f"[{a*3}]")
    print(niveau_charge, "%")

elif (35<= niveau_charge<45):
    print(f"[{a*4}]")
    print(niveau_charge, "%")

elif (45<= niveau_charge<55):
    print(f"[{a*5}]")
    print(niveau_charge, "%")

elif (55<= niveau_charge<65):
    print(f"[{a*6}]")
    print(niveau_charge, "%")

elif (65<= niveau_charge<75):
    print(f"[{a*7}]")
    print(niveau_charge, "%")

elif (75<= niveau_charge<85):
    print(f"[{a*8}]")
    print(niveau_charge, "%")

elif (85<= niveau_charge<95):
    print(f"[{a*9}]")
    print(niveau_charge, "%")

elif (95<= niveau_charge<=100):
    print(f"[{a*10}]")
    print(niveau_charge, "%")
else:
    print("Erreur : niveau de charge invalide.")
    


    




