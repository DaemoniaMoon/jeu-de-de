import random

# Nom du jeux

print()
print("Roll The Dice !")
print("----------")
print()

# Règles du jeu

print("Les joueurs lancent chacun des dés (vous avez le choix entre plusieurs dés:)")
print("Un dé à 4, 6, 8, 10, 12, 20 ou 100 faces ")
print("Le joueur qui obtient le plus haut score est déclaré gagnant.")
print("En cas de scores égaux, ils sont déclarés ex aequo.")

# choix du nombre de joueurs



# choix du type de dé

print()
print("Choisissez le nombre de face de vos dés")
nbFaces = int(input("Choisissez entre 4, 6, 8, 10, 12, 20 ou 100 faces :"))
deDisponible = [4, 6, 8, 10, 12, 20, 100]
while nbFaces not in deDisponible:
    print()
    nbFace = int(input("Choisissez entre 4, 6, 8, 10, 12, 20 ou 100 faces :"))

# Les joueurs entrent leur noms :

print()
NomJoueur1 = input("Joueur 1, quel est ton nom ? ")
NomJoueur2 = input("Joueur 2, quel est ton nom ? ")


Tirage1 = random.randint(1, 6) + random.randint(1, 6)
Tirage2 = random.randint(1, 6) + random.randint(1, 6)

print()
print(NomJoueur1 + " a un score de " + str(Tirage1))
print(NomJoueur2 + " a un score de " + str(Tirage2))

print()
if Tirage1 > Tirage2:
    print(NomJoueur1 + " a gagné !")
elif Tirage2 > Tirage1:
    print(NomJoueur2 + " a gagné !")
else:
    print(NomJoueur1 + " et " + NomJoueur2 + " sont ex aequo.")
 
print()
print("Au revoir.")