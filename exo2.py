# TODO : Calculer les quantités de matériaux nécessaires pour fabriquer un nombre donné de baguettes magiques.

nombre_baguettes = int(input("Nombre de baguettes à fabriquer: "))
bois = nombre_baguettes * 3
ccm = nombre_baguettes
vernis = nombre_baguettes * 10
print(f"Voici les materiaux requis pour la fabrication de {nombre_baguettes} baguettes magiques:")
print(f"- {bois} piece(s) de bois.")
print(f"- {ccm} coeur(s) de creatures magiques.")
print(f"- {vernis} ml de vernis.")