import re
import sys
import time
import numpy as np
with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\10_1_ori.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")

liste_droite_possible = ["-" , "J" , "7"]
liste_bas_possible = [ "|" , "L" , "J" ]
liste_gauche_possible = ["-" , "L" , "F"]
liste_haut_possible = [ "|" , "7", "F" ]

new_list=[]
for ligne in lignes:
    for caractere in ligne :
        new_list.append(caractere)
array=np.asarray(new_list)
#print(f" array : {array} , nombre de lignes : {int(len(lignes))}, taille d'une ligne : {int(len(lignes[0]))}")
tableau=array.reshape(int(len(lignes)), int(len(lignes[0])))
tableau = np.pad(tableau, pad_width=1, constant_values='.')

print(f"tableau : {tableau}")
#print(f"types : type de la ligne : {type(lignes)}, type de l'array : {type(array)}, type du tableau : {type(tableau)}")
#print(f"3 premières lignes du tableau 2d obtenu : \n {tableau[0:3]}")
#print(f"nombre de dimensions du tableau : {tableau.ndim}")
#print(f"1ere ligne 2eme colonne du tableau : {tableau[0][1]}")
#print(f"2eme ligne 3eme colonne du tableau : {tableau[1][2]}")
#print(f"3eme ligne du tableau : {tableau[2]}")
print(f"lignes (ordonnées) 73 à 77, colonnes (abscisses) 51 à 63 :  {tableau[73:78,51:64]}")



#print(f"3eme colonne du tableau : {tableau[:,2]}")
print(f"nombre de lignes du tableau: {tableau.shape[0]}, nombre de colonnes : {tableau.shape[1]} ")

position_depart = np.where(tableau == 'S')
position_depart = list(zip(position_depart[1], position_depart[0]))
#methode 2 : position_depart = [(i, j) for i, ligne in enumerate(tableau) for j, element in enumerate(ligne) if element == 'F']
print(f"position de départ : {position_depart}")
print(tableau[76,54])


def premier_deplacement(position_depart):
    current_positions=[[0,0,0],[0,0,0]]
    numero_coordonnee=0
    abscisse_depart = position_depart[0][0]
    ordonnee_depart = position_depart[0][1]
    if tableau[ordonnee_depart][abscisse_depart+1] in liste_droite_possible:
        current_positions[numero_coordonnee]=abscisse_depart+1,ordonnee_depart,1  #le ,1 peremt d'initialiser un compteur montrant à combien de tuyaux on est du départ
        numero_coordonnee+=1 #on cherche maintenant la 2eme et dernière coordonnée possible
    if tableau[ordonnee_depart+1][abscisse_depart] in liste_bas_possible:
        current_positions[numero_coordonnee]=abscisse_depart, ordonnee_depart+1,1
        numero_coordonnee+=1
    if tableau[ordonnee_depart][abscisse_depart-1] in liste_gauche_possible:
        current_positions[numero_coordonnee]=abscisse_depart-1,ordonnee_depart,1
        numero_coordonnee+=1
    if tableau[ordonnee_depart-1][abscisse_depart] in liste_haut_possible:
        current_positions[numero_coordonnee]=abscisse_depart,ordonnee_depart-1,1
        numero_coordonnee+=1

    return current_positions

def deplacement(current_positions, liste_positions_visitees):
    liste_positions_visitees.append(current_positions[0][0:2])
    liste_positions_visitees.append(current_positions[1][0:2])
    print(f"current positions : {current_positions}")
    for indice in range(len(current_positions)) :
        abscisse_position = current_positions[indice][0]
        ordonnee_position = current_positions[indice][1]
        if tableau[ordonnee_position][abscisse_position + 1] in liste_droite_possible and (abscisse_position + 1,ordonnee_position) not in liste_positions_visitees:
            current_positions[indice]=abscisse_position+1,ordonnee_position,current_positions[indice][2]+1
        elif tableau[ordonnee_position+1][abscisse_position] in liste_bas_possible and (abscisse_position, ordonnee_position +1) not in liste_positions_visitees:
            current_positions[indice]=abscisse_position,ordonnee_position+1,current_positions[indice][2]+1
        elif tableau[ordonnee_position][abscisse_position - 1] in liste_gauche_possible and (abscisse_position - 1 , ordonnee_position) not in liste_positions_visitees:
            current_positions[indice]=abscisse_position-1,ordonnee_position,current_positions[indice][2]+1
        elif tableau[ordonnee_position-1][abscisse_position] in liste_haut_possible and (abscisse_position, ordonnee_position-1) not in liste_positions_visitees:
            current_positions[indice]=abscisse_position,ordonnee_position-1,current_positions[indice][2]+1
    #print(f"current positions après déplacement : {current_positions}")

liste_positions_visitees = position_depart
current_positions=premier_deplacement(position_depart)
#while current_positions[0][0:2]!=current_positions[1][0:2]:
for i in range(52):
    deplacement(current_positions,liste_positions_visitees)

reponse = max(current_positions[0][2],current_positions[1][2])
print(f"la réponse à la partie 1 est : {reponse}")