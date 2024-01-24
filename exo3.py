# TODO : Calculer la distance que chaque rocher lancé par les catapultes peut atteindre en utilisant la formule de la portée d'un projectile.
import math
vitesse_initiale =float(input("Entrez la vitesse initiale (en m/s) :"))
angle_lancement = float(input("Entrez l'angle de lancement (en degres) :"))
angle_converti= angle_lancement* math.pi / 180
D= (vitesse_initiale)**2 * math.sin(2*angle_converti) / 9.81
print(f"La distance parcourue par le projectile est de {D}")