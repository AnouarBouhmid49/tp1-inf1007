# TODO : Analyser le message crypté de l'Empire, compter le nombre d'occurrences des voyelles "a", "e", "i", "o", "u" et "y", puis assembler les résultats en une coordonnée galactique.
message = input("Entrez le message de l'Empire")
v1 = message.count("a")+ message.count("A")
v2 = message.count("e")+ message.count("E")
v3 = message.count("i")+ message.count("I")
v4 = message.count("o")+ message.count("O")
v5 = message.count("u")+ message.count("U")
v6 = message.count("y")+ message.count("Y")

print(f"Les coordonnees galactiques sont : {v1}.{v2}.{v3}.{v4}.{v5}.{v6}")