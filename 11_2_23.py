import re
import sys
import time
import numpy as np
#82000210 too low
with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\11_1_ori.txt', 'r') as fichier:
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
#tableau = np.pad(tableau, pad_width=1, constant_values='#')
#print(f"nombre de lignes du tableau: {tableau.shape[0]}, nombre de colonnes : {tableau.shape[1]} ")
#print(tableau)

new_ligne = np.full((1, tableau.shape[1]), '.', dtype=str)
pas_expansion = 1000000 #en réalité, plutôt un coefficient qu'un pas. 10 signifie qu'une ligne devient 10 lignes (on ajoute 9 lignes)


def expansion_univers2(tableau) :
    lignes_vides = []
    colonnes_vides = []
    for ligne in range(tableau.shape[1]):
        #tableau = np.insert(tableau, nouvelle_ligne , axis=0 )
        if np.all(tableau[ligne] == '.'):
            lignes_vides.append(ligne+1)
    for colonne in range(tableau.shape[1]) :
        if np.all(tableau[:,colonne] == '.'):
            colonnes_vides.append(colonne+1)
    print(f"numéros lignes vides, numéros colonnes vides : {lignes_vides}, {colonnes_vides}")
    return lignes_vides, colonnes_vides

def coordonnées_galaxies(tableau) :
    coordonnées_galaxies = np.where(tableau == '#')
    coordonnées_galaxies = list(zip(coordonnées_galaxies[1]+1,coordonnées_galaxies[0]+1))
    print(f"coordonnées des galaxies : {coordonnées_galaxies}")
    return coordonnées_galaxies

def chemins_galaxies(coordonnées_galaxies):
    somme_distances = 0
    for galaxie1 in coordonnées_galaxies:
        for galaxie2 in coordonnées_galaxies:
            #on compte le nombre de lignes et de colonnes vides qui séparent galaxie1 et galaxie2, (c'est à dire : '
            # le nombre de lignes vides entre galaxies 1 et galaxies 2 : nombre d'éléments dans [lignes_vides] > galaxie1[1] et < galaxie2[1]
            # et idem, nombre de colonnes vides : nombre d'éléments dans [colonnes_vides] > galaxie1[0] et < galaxie2[0]
            nombre_lignes_vides = 0
            nombre_colonnes_vides = 0
            for ligne_vide in lignes_vides:
                if galaxie1[1]<ligne_vide and galaxie2[1]>ligne_vide :
                    nombre_lignes_vides+=1
                if galaxie1[1]>ligne_vide and galaxie2[1]<ligne_vide :
                    nombre_lignes_vides+=1
            for colonne_vide in colonnes_vides:
                if galaxie1[0]<colonne_vide and galaxie2[0]>colonne_vide :
                    nombre_colonnes_vides+=1
                if galaxie1[0] > colonne_vide and galaxie2[0] < colonne_vide:
                    nombre_colonnes_vides += 1
            distance = ( abs(galaxie2[1]-galaxie1[1]) + nombre_lignes_vides * (pas_expansion-1) )  + (abs(galaxie2[0]-galaxie1[0]) + nombre_colonnes_vides * (pas_expansion-1) )
            #print(f"({galaxie2[1]}-{galaxie1[1]}) + ({galaxie2[0]}-{galaxie1[0]})")
            print(f"galaxie2 : {galaxie2} et galaxie1 : {galaxie1}, distance de base : {abs(galaxie2[1]-galaxie1[1]) + abs(galaxie2[0]-galaxie1[0])}, nombre de lignes vides : {nombre_lignes_vides} et nombre colonnes vides = {nombre_colonnes_vides}")
            print(f"distance : {distance}")
            somme_distances+=distance
    somme_distances/=2
    print(somme_distances)


print(f"Taille de l'univers avant expansion : {tableau.shape[0]}, nombre de colonnes : {tableau.shape[1]} ")
print(tableau)
#étaient utiles pour approche partie 1, en réalité on peut faire autrement :
#tableau=expansion_univers(tableau)
#print(f"Taille de l'univers après expansion : {tableau.shape[0]}, nombre de colonnes : {tableau.shape[1]} ")
#print(tableau)
lignes_vides, colonnes_vides = expansion_univers2(tableau)
coordonnées_galaxies = coordonnées_galaxies(tableau)
chemins_galaxies(coordonnées_galaxies)