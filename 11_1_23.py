import re
import sys
import time
import numpy as np
with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\11_1.txt', 'r') as fichier:
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

pas_expansion = 19999
def expansion_univers(tableau):
    index = 0  # obligé de créer un index séparé pour gérer les lignes en double, que l'on ne veut traiter qu'une fois
    for ligne in range(tableau.shape[1]):
        #tableau = np.insert(tableau, nouvelle_ligne , axis=0 )
        if np.all(tableau[index] == '.'):
            lignes_a_inserer = np.repeat(np.full((1, tableau.shape[1]), '.', dtype=str),pas_expansion,axis=0)
            tableau = np.insert(tableau,index, lignes_a_inserer,axis=0)
            #on insère au niveau ligne-1 pour éviter que la nouvelle ligne créée soit de nouveau traitée
            #print(tableau)
            index+=pas_expansion #on saute des lignes pour ne pas retraiter plusieurs fois la ligne dupliquée
        index+=1

    index = 0  # obligé de créer un index séparé pour gérer les lignes en double, que l'on ne veut traiter qu'une fois
    for colonne in range(tableau.shape[1]) :
        # tableau = np.insert(tableau, colonne)
        if np.all(tableau[:,index] == '.'):
            #print(f"coucou colonne {colonne}, {index}")
            colonnes_a_inserer = np.repeat(np.full((1, tableau.shape[0]), '.', dtype=str),pas_expansion,axis=0)
            tableau = np.insert(tableau, index, colonnes_a_inserer,axis=1)
            #print(tableau)
            index+=pas_expansion #on saute des lignes pour ne pas retraiter plusieurs fois la ligne dupliquée
        index+=1
    return tableau

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
            # le nombre de lignes vides entre galaxies 1 et galaxies 2 : nombres d'éléments dans [lignes_vides] >                                                                                        c'dont galaxie1[1])
            distance = abs(galaxie2[1]-galaxie1[1]) + abs(galaxie2[0]-galaxie1[0])
            #print(f"({galaxie2[1]}-{galaxie1[1]}) + ({galaxie2[0]}-{galaxie1[0]})")
            print(f"galaxie2 : {galaxie2} et galaxie1 : {galaxie1}")
            print(f"distance : {distance}")
            somme_distances+=distance
    somme_distances/=2
    print(somme_distances)


print(f"Taille de l'univers avant expansion : {tableau.shape[0]}, nombre de colonnes : {tableau.shape[1]} ")
print(tableau)
#étaient utiles pour approche partie 1, en réalité on peut faire autrement :
tableau=expansion_univers(tableau)
print(f"Taille de l'univers après expansion : {tableau.shape[0]}, nombre de colonnes : {tableau.shape[1]} ")
print(tableau)
coordonnées_galaxies = coordonnées_galaxies(tableau)
chemins_galaxies(coordonnées_galaxies)