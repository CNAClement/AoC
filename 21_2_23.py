import re
import sys
import time
import numpy as np
#321 too low
with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\21_1.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")

start=time.time()

new_list=[]
for ligne in lignes:
    for caractere in ligne :
        new_list.append(caractere)
array=np.asarray(new_list)
#print(f" array : {array} , nombre de lignes : {int(len(lignes))}, taille d'une ligne : {int(len(lignes[0]))}")
tableau=array.reshape(int(len(lignes)), int(len(lignes[0])))
tableau = np.pad(tableau, pad_width=1, constant_values='%')

print(f"longueur tableau : {tableau.shape[0]} lignes, {tableau.shape[1]} colonnes")

class Jardinier:
    def __init__(self,position,univers):  #univers est un élément de dictionnaire_univers, qui à une clé (0,1) associe un tableau
        self.position=position
        self.univers=univers

    def changement_univers(self,direction):
        coordonnées_univers = next(iter(self.univers))
        if direction == "droite" :
            coordonnées_univers = (coordonnées_univers[0] +1 , coordonnées_univers[1])
        elif direction == "bas":
            coordonnées_univers = (coordonnées_univers[0] , coordonnées_univers[1] +1 )
        elif direction == "gauche":
            coordonnées_univers = (coordonnées_univers[0] -1 , coordonnées_univers[1])
        elif direction == "haut":
            coordonnées_univers = (coordonnées_univers[0] , coordonnées_univers[1] -1 )

        if coordonnées_univers not in dictionnaire_univers:
            dictionnaire_univers[coordonnées_univers]=tableau.copy()
        self.univers=(coordonnées_univers,dictionnaire_univers[coordonnées_univers])
        return self.univers


def créer_jardinier(liste_jardiniers) : #on rentre avec l'instance jardinier et son univers associé, et pour chaque déplacement possible, on
    #créé une nouvelle instance de jardinier, puis on delete l'instance initiale
    longueur_liste_entrée = len(liste_jardiniers)
    #print(f"longueur liste jardiniers : {longueur_liste_entrée}")

    #print(liste_jardiniers[0].univers[0])
    for numéro_jardinier in range(longueur_liste_entrée) :
        jardinier = liste_jardiniers[numéro_jardinier]
        tableau_univers = dictionnaire_univers[jardinier.univers[0]]
        #print(f"tableau de l'univers : {tableau_univers}")
        #print(f"jardinier traité : {jardinier.position , jardinier.univers[1] }")
        if tableau_univers[jardinier.position[1]][jardinier.position[0] +1 ] == ".":  #on regarde si l'emplacement à droite est disponible
            liste_jardiniers.append(Jardinier((jardinier.position[0] +1 , jardinier.position[1]) , jardinier.univers ))
            tableau_univers[jardinier.position[1]][jardinier.position[0] + 1] = 0

        if tableau_univers[jardinier.position[1] +1 ][jardinier.position[0]] == ".": #on regarde si l'emplacement en bas  est disponible
            liste_jardiniers.append(Jardinier((jardinier.position[0], jardinier.position[1] +1 ) , jardinier.univers ))
            tableau_univers[jardinier.position[1] +1 ][jardinier.position[0]] = 0

        if tableau_univers[jardinier.position[1]][jardinier.position[0] -1 ] == ".": #on regarde si l'emplacement à gauche est disponible
            liste_jardiniers.append(Jardinier((jardinier.position[0] -1 , jardinier.position[1]) , jardinier.univers ))
            tableau_univers[jardinier.position[1]][jardinier.position[0] - 1] = 0

        if tableau_univers[jardinier.position[1] -1 ][jardinier.position[0]] == ".": #on regarde si l'emplacement en haut est disponible
            liste_jardiniers.append(Jardinier((jardinier.position[0] , jardinier.position[1] - 1) , jardinier.univers ))
            tableau_univers[jardinier.position[1] -1 ][jardinier.position[0]] = 0

        if tableau_univers[jardinier.position[1]][jardinier.position[0] +1 ] == "%":  # si on a atteint le bord droit, on recommence au bord gauche (qui sera toujours un "." ) sur un nouvel univers "à droite"
            liste_jardiniers.append(Jardinier((1, jardinier.position[1]), jardinier.changement_univers("droite")))
            coordonnées_nouvel_univers = liste_jardiniers[-1].univers[0]
            tableau_nouvel_univers = dictionnaire_univers[coordonnées_nouvel_univers]
            tableau_nouvel_univers[liste_jardiniers[-1].position[1]][liste_jardiniers[-1].position[0]] = 0
            #on prend la dernière instance créée, avec son propre univers et son propre tableau, et on met in "0" à l'endroit où l'instance est créée

        if tableau_univers[jardinier.position[1] +1 ][jardinier.position[0]] == "%":  # si on atteint le bas, on recommence en haut sur un nouvel univers "en bas"
            liste_jardiniers.append(Jardinier((jardinier.position[0], 1), jardinier.changement_univers("haut")))
            coordonnées_nouvel_univers = liste_jardiniers[-1].univers[0]
            tableau_nouvel_univers = dictionnaire_univers[coordonnées_nouvel_univers]
            tableau_nouvel_univers[liste_jardiniers[-1].position[1]][liste_jardiniers[-1].position[0]] = 0

        if tableau_univers[jardinier.position[1]][jardinier.position[0] - 1] == "%":  #on recommence à droite d'un univers situé "sur la gauche"
            liste_jardiniers.append(Jardinier((tableau.shape[1] -2 , jardinier.position[1]), jardinier.changement_univers("gauche")))
            #print(f"jardinier créé : {liste_jardiniers[-1].position}, {liste_jardiniers[-1].univers[1]}")
            coordonnées_nouvel_univers = liste_jardiniers[-1].univers[0]
            tableau_nouvel_univers = dictionnaire_univers[coordonnées_nouvel_univers]
            tableau_nouvel_univers[liste_jardiniers[-1].position[1]][liste_jardiniers[-1].position[0]] = 0

        if tableau_univers[jardinier.position[1] - 1][jardinier.position[0]] == "%":  # on regarde si l'emplacement en haut est disponible
            liste_jardiniers.append(Jardinier((jardinier.position[0], tableau.shape[0] -2 ), jardinier.changement_univers("haut")))
            coordonnées_nouvel_univers = liste_jardiniers[-1].univers[0]
            tableau_nouvel_univers = dictionnaire_univers[coordonnées_nouvel_univers]
            tableau_nouvel_univers[liste_jardiniers[-1].position[1]][liste_jardiniers[-1].position[0]] = 0

    #suppression des jardiniers traités (rip) et remise à "." de l'emplacement libéré :
    for numéro_jardinier in range(longueur_liste_entrée):
        jardinier = liste_jardiniers[numéro_jardinier]
        #print(f"on va supprimer le jardinier : {jardinier.position} de l'univers {jardinier.univers[1]}")
        tableau_univers[jardinier.position[1]][jardinier.position[0]]="."
    del liste_jardiniers[0:longueur_liste_entrée]

    return liste_jardiniers

coordonnées_jardinier = np.where(tableau == 'S')
coordonnées_jardinier = list(zip(coordonnées_jardinier[1], coordonnées_jardinier[0]))

dictionnaire_univers = {(0,0) : tableau.copy()} #le 0,0 indique la localisation du tableau par rapport au tableau initial, exemple (2,1) ==> +2 à droite et +1 en bas
jardinier=Jardinier(coordonnées_jardinier[0],((0,0),dictionnaire_univers[0,0]))
print(f"position départ : {coordonnées_jardinier}")
coordonnées_univers_jardinier = jardinier.univers[0]
tableau_univers = dictionnaire_univers[coordonnées_univers_jardinier]
# puisque jardinier.univers est un dictionnaire, le tableau est la valeur associée à la clé.
print(f"tableau de l'univers : {tableau_univers}")
print(f"vérification position de départ du jardinier : {tableau_univers[jardinier.position[1]][jardinier.position[0]]}")
liste_jardiniers = [jardinier]


for numero_pas in range(80):
    liste_jardiniers =créer_jardinier(liste_jardiniers)
    #print(f"longueur après : {len(liste_jardiniers)}")


#for _ in range(len(liste_jardiniers)):
  #  print(f"{liste_jardiniers[_].position}, {liste_jardiniers[_].univers[1]}")




réponse=len(liste_jardiniers)
print(f"réponse : {réponse} en {time.time() - start} secondes")


#petite remarque :
#la coordonnée (6,2) renvoyée correspond à tableau[2][6], c'est-à-dire à 3eme colonne, 7eme ligne du tableau.
# Cependant, puisque le tableau est paddé, la coordonnée (6,2) correspond à la 2eme colonne, 6eme ligne du tableau "initial" (avant padding).
# De cette façon, cela facilite notre lecture humaine, et permet également d'utiliser directement ces coordonnées avec tableau (sans avoir besoin de faire des conversions +1 / -1 )
# (6,2) correspond à la coordonnée que l'on attend en tant qu'humain, mais est directement utilisable avec tableau[2][6] (sur le tableau paddé).
