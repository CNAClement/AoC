import re
import sys
import time
import numpy as np
#321 too low
with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\10_1_ori.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")

liste_compatibilites_est = ["-" , "J" , "7"] #Le caractère peut être trouvé à l'Est de la position, ie : il est compatible avec le caractère à son Ouest, ou encore autrement dit : ce caractère peut faire une jonction vers l'Ouest
liste_compatibilites_sud = ["|" , "J" , "L"] #Le caractère peut être trouvé au Sud, ie : il est compatible avec le caractère à son Nord, ou encore autrement dit : ce caractère peut faire une jonction vers le Nord
liste_compatibilites_ouest = ["-" , "F" , "L"] #Le caractère peut être trouvé à l'Ouest, ie : il est compatible avec le caractère à son Est
liste_compatibilites_nord = ["|" , "F" , "7"] #Le caractère peut être trouvé au Nord

liste_compatibilites_vers_est = ["-" , "F" , "L"] #Le caractère est autorisé à aller vers l'Est, il est possible de se retrouver à l'Est de ce caractère
liste_compatibilites_vers_sud = ["|" , "7" , "F"] #le caractère est autorisé à aller vers le Sud, il est possible de se retrouver au Sud de se caractère
liste_compatibilites_vers_ouest = ["-" , "J" , "7"] #vers l'Ouest
liste_compatibilites_vers_nord = ["|" , "L" , "J"]  #vers le Nord

barrage_horizontal = ["-","F","L","S"]
new_list=[]
for ligne in lignes:
    for caractere in ligne :
        new_list.append(caractere)
array=np.asarray(new_list)
#print(f" array : {array} , nombre de lignes : {int(len(lignes))}, taille d'une ligne : {int(len(lignes[0]))}")
tableau=array.reshape(int(len(lignes)), int(len(lignes[0])))
tableau = np.pad(tableau, pad_width=1, constant_values='#')

print(f"tableau : {tableau}")
#print(f"types : type de la ligne : {type(lignes)}, type de l'array : {type(array)}, type du tableau : {type(tableau)}")
#print(f"3 premières lignes du tableau 2d obtenu : \n {tableau[0:3]}")
#print(f"nombre de dimensions du tableau : {tableau.ndim}")
#print(f"1ere ligne 2eme colonne du tableau : {tableau[0][1]}")
#print(f"2eme ligne 3eme colonne du tableau : {tableau[1][2]}")
#print(f"3eme ligne du tableau : {tableau[2]}")
#print(f"lignes (ordonnées) 73 à 77, colonnes (abscisses) 51 à 63 :  {tableau[73:78,51:64]}")



#print(f"3eme colonne du tableau : {tableau[:,2]}")
print(f"nombre de lignes du tableau: {tableau.shape[0]}, nombre de colonnes : {tableau.shape[1]} ")

position_depart = np.where(tableau == 'S')
position_depart = list(zip(position_depart[1], position_depart[0]))
#methode 2 : position_depart = [(i, j) for i, ligne in enumerate(tableau) for j, element in enumerate(ligne) if element == 'F']
print(f"position de départ : {position_depart}")

def premier_deplacement(position_depart):
    current_positions=[[0,0,0],[0,0,0]]
    numero_coordonnee=0
    abscisse_depart = position_depart[0][0]
    ordonnee_depart = position_depart[0][1]
    if tableau[ordonnee_depart][abscisse_depart+1] in liste_compatibilites_est:
        current_positions[numero_coordonnee]=abscisse_depart+1,ordonnee_depart,1  #le ,1 peremt d'initialiser un compteur montrant à combien de tuyaux on est du départ
        numero_coordonnee+=1 #on cherche maintenant la 2eme et dernière coordonnée possible
    if tableau[ordonnee_depart+1][abscisse_depart] in liste_compatibilites_sud:
        current_positions[numero_coordonnee]=abscisse_depart, ordonnee_depart+1,1
        numero_coordonnee+=1
    if tableau[ordonnee_depart][abscisse_depart-1] in liste_compatibilites_ouest:
        current_positions[numero_coordonnee]=abscisse_depart-1,ordonnee_depart,1
        numero_coordonnee+=1
    if tableau[ordonnee_depart-1][abscisse_depart] in liste_compatibilites_nord:
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
        #tentative de déplacement vers l'Est : il faut que le tuyau de départ et le tuyau d'arrivée aient tous les deux une comptabilité Est
        if tableau[ordonnee_position][abscisse_position] in liste_compatibilites_vers_est and tableau[ordonnee_position][abscisse_position + 1] in liste_compatibilites_est and (abscisse_position + 1,ordonnee_position) not in liste_positions_visitees:
            current_positions[indice]=abscisse_position+1,ordonnee_position,current_positions[indice][2]+1
        #tentative de déplacement vers le Sud
        elif tableau[ordonnee_position][abscisse_position] in liste_compatibilites_vers_sud and tableau[ordonnee_position+1][abscisse_position] in liste_compatibilites_sud and (abscisse_position, ordonnee_position +1) not in liste_positions_visitees:
            current_positions[indice]=abscisse_position,ordonnee_position+1,current_positions[indice][2]+1
        #tentative de déplacement vers l'Ouest
        elif tableau[ordonnee_position][abscisse_position] in liste_compatibilites_vers_ouest and tableau[ordonnee_position][abscisse_position - 1] in liste_compatibilites_ouest and (abscisse_position - 1 , ordonnee_position) not in liste_positions_visitees:
            current_positions[indice]=abscisse_position-1,ordonnee_position,current_positions[indice][2]+1
        #tentative de déplacement vers le Nord
        elif tableau[ordonnee_position][abscisse_position] in liste_compatibilites_vers_nord and tableau[ordonnee_position-1][abscisse_position] in liste_compatibilites_nord and (abscisse_position, ordonnee_position-1) not in liste_positions_visitees:
            current_positions[indice]=abscisse_position,ordonnee_position-1,current_positions[indice][2]+1
    #print(f"current positions après déplacement : {current_positions}")


liste_positions_visitees = position_depart
current_positions=premier_deplacement(position_depart)
while current_positions[0][0:2]!=current_positions[1][0:2]:
#for i in range(52):
    deplacement(current_positions,liste_positions_visitees)
liste_positions_visitees.append(current_positions[0][0:2]) #on ajoute la dernière position à la liste
reponse = max(current_positions[0][2],current_positions[1][2])
print(f"la réponse à la partie 1 est : {reponse}")

print(f"liste positions visitées : {liste_positions_visitees}")

for i in range(1,len(tableau[0])-1): #on n'itère pas sur la bordure
    for j in range(1,len(tableau)-1):
        if (i, j) not in liste_positions_visitees:
            tableau[j][i] = '.'  # toutes les cases n'appartenant pas à la boucle de tuyaux principale deviennent des espaces vides, même les tuyaux isolés

positions_vides = np.where(tableau == '.')
positions_vides = list(zip(positions_vides[1], positions_vides[0]))
print(f"positions vides : {positions_vides}")

for indice in range(len(positions_vides)) :
    abscisse_vide = positions_vides[indice][0]
    ordonnee_vide = positions_vides[indice][1]
    traversee_tuyau = 0
    while tableau[ordonnee_vide+1][abscisse_vide]!="#" :
        if tableau[ordonnee_vide+1][abscisse_vide] in barrage_horizontal:
            traversee_tuyau+=1
        ordonnee_vide += 1

    if traversee_tuyau%2!=0 : #le nombre est impair ==> on n'est pas dans l'enclos
        tableau[positions_vides[indice][1]][positions_vides[indice][0]] = "%"
        print(f"On a traversé un nombre impair de tuyaux : {traversee_tuyau} pour la position {positions_vides[indice]}")

print(tableau)
# On compte le nombre de I :
resultat2 =np.count_nonzero(tableau == '%')
print(f"le résultat de la partie 2 est : {resultat2}")
