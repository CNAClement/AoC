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

new_list=[]
for ligne in lignes:
    for caractere in ligne :
        new_list.append(caractere)
array=np.asarray(new_list)
#print(f" array : {array} , nombre de lignes : {int(len(lignes))}, taille d'une ligne : {int(len(lignes[0]))}")
tableau=array.reshape(int(len(lignes)), int(len(lignes[0])))
tableau = np.pad(tableau, pad_width=1, constant_values='%')

print(f"longueur tableau : {tableau.shape[0]} lignes, {tableau.shape[1]} colonnes")

def déplacer_jardinier(tableau, liste_coordonnées) :
    print(liste_coordonnées)
    for coordonnées in liste_coordonnées :
        if tableau[coordonnées[1]][coordonnées[0] +1 ] == ".": #on regarde si l'emplacement à droite est disponible
            tableau[coordonnées[1]][coordonnées[0] +1 ] = "0"
        if tableau[coordonnées[1] +1 ][coordonnées[0]] == ".": #on regarde si l'emplacement en bas  est disponible
            #print(coordonnées)
            #print(tableau[11][11])
            tableau[coordonnées[1] +1 ][coordonnées[0]] = "0"
        if tableau[coordonnées[1]][coordonnées[0] -1 ] == ".": #on regarde si l'emplacement à gauche est disponible
            tableau[coordonnées[1]][coordonnées[0] -1 ] = "0"
        if tableau[coordonnées[1] -1 ][coordonnées[0]] == ".": #on regarde si l'emplacement en haut est disponible
            tableau[coordonnées[1] -1 ][coordonnées[0]] = "0"

        if tableau[coordonnées[1]][coordonnées[0] +1 ] == "%": #si on a atteint le bord droit, on recommence au bord gauche (qui sera toujours un "." )
            tableau[coordonnées[1]][1] = "0"
        if tableau[coordonnées[1] +1 ][coordonnées[0]] == "%": #si on atteint le bas, on recommence en haut
            tableau[coordonnées[1]][coordonnées[0]] = "0"
        if tableau[coordonnées[1]][coordonnées[0] -1 ] == ".":
            tableau[coordonnées[1]][tableau.shape[1] -1 ] = "0"
        if tableau[coordonnées[1] -1 ][coordonnées[0]] == ".":
            tableau[coordonnées[tableau.shape[0] - 1 ]][coordonnées[0]] = "0"

        tableau[coordonnées[1]][coordonnées[0]] = "."  #lorsque tous les déplacements ont été testés et effectués, la position initiale redevient un "."
    return tableau

coordonnées_jardinier = np.where(tableau == '#')
coordonnées_jardinier = list(zip(coordonnées_jardinier[1], coordonnées_jardinier[0]))
print(coordonnées_jardinier)


coordonnées_jardinier = np.where(tableau == 'S')

coordonnées_jardinier = list(zip(coordonnées_jardinier[1], coordonnées_jardinier[0]))
print(f"position départ : {coordonnées_jardinier}")

for numero_pas in range(100):
    tableau=déplacer_jardinier(tableau,coordonnées_jardinier)
    coordonnées_jardinier=np.where(tableau=="0")
    coordonnées_jardinier = list(zip(coordonnées_jardinier[1], coordonnées_jardinier[0]))

réponse=np.count_nonzero(tableau=="0")
print(réponse)


#petite remarque :
#la coordonnée (6,2) renvoyée correspond à tableau[2][6], c'est-à-dire à 3eme colonne, 7eme ligne du tableau.
# Cependant, puisque le tableau est paddé, la coordonnée (6,2) correspond à la 2eme colonne, 6eme ligne du tableau "initial" (avant padding).
# De cette façon, cela facilite notre lecture humaine, et permet également d'utiliser directement ces coordonnées avec tableau (sans avoir besoin de faire des conversions +1 / -1 )
# (6,2) correspond à la coordonnée que l'on attend en tant qu'humain, mais est directement utilisable avec tableau[2][6] (sur le tableau paddé).
