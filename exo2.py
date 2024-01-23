# TODO : Calculer les quantités de matériaux nécessaires pour fabriquer un nombre donné de baguettes magiques.

nombre_baguettes = input("Nombre de baguettes à fabriquer: ")
bois = 3 * nombre_baguettes
ccm = 1 * nombre_baguettes
vernis = 10 * nombre_baguettes
print(f"Voici les materiaux requis pour la fabrication de {nombre_baguettes} baguettes magiques:", bois "piece de bois", ccm "coeur de creatures magique", vernis "ml de vernis")