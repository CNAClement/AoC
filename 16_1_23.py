import re
import sys
import time
import copy
#1071 too low
import numpy as np
from dataclasses import dataclass


with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\16_1_ori.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")
partie="partie2"
new_list=[]
for ligne in lignes:
    for caractere in ligne :
        new_list.append(caractere)
array=np.asarray(new_list)
tableau=array.reshape(int(len(lignes)), int(len(lignes[0])))
tableau = np.pad(tableau, pad_width=1, constant_values='%')
print(f"nombres de ligne du tableau : {tableau.shape[0]}, nombre de colonnes : {tableau.shape[1]}, dimensions : {tableau.ndim}")
#tableau = [['0' if element == '.' else element for element in row] for row in tableau] utile dans le cas d'un tableau NON-numpy
#tableau[tableau == '.'] = '0'
print(tableau)

@dataclass()
class Rayon:
    def __init__(self,position:tuple,sens:tuple,etat:str ="non traité"):
        self.position = position
        self.sens = sens
        self.etat = etat

    def deplacement_rayon(self):
        position=tuple(x + y for x, y in zip(self.position, self.sens))
        return position
def transformation_coordonnees(coordonnees,facteur):
    x,y=coordonnees
    nouvelles_coordonnees = (y*facteur, x*facteur)
    return nouvelles_coordonnees


def gestion_liste_rayons(liste_rayons_complete, liste_rayons) :
    # Créer une nouvelle liste non traitée sans les éléments qui correspondent à la liste traitée
    rayons_non_traites = [
        rayon for rayon in liste_rayons
        if not any(
            (
                    rayon.position[0] == rayon_traite.position[0]
                    and rayon.position[1] == rayon_traite.position[1]
                    and rayon.sens[0] == rayon_traite.sens[0]
                    and rayon.sens[1] == rayon_traite.sens[1]
            )
            for rayon_traite in liste_rayons_complete
        )
    ]
        # La nouvelle liste_non_traitee ne contiendra plus les éléments qui correspondent à la liste_traitee
    return rayons_non_traites

def trajet_rayon(rayon,liste_positions) :
    liste_rayons=[rayon]
    etat_rayon=[] #contient tuple (position,sens) pour vérifier qu'on ne boucle pas
    if rayon.position not in liste_positions and tableau[rayon.position[1], rayon.position[0]] != "%":
            liste_positions.append(rayon.position) #On le met en haut de la fonction également pour être sûr d'ajouter les rayons qui rentrent ici (après split par exemple)
    while tableau[rayon.position[1],rayon.position[0]]!='%' and (rayon.position,rayon.sens) not in etat_rayon :
            #print(f"on est en position et sens : {(rayon.position,rayon.sens)}, état rayon : {etat_rayon}")
            #print(f"coordonnées du rayon : {rayon.position}, valeur tableau : {tableau[rayon.position[1], rayon.position[0]]} , sens : {rayon.sens}")
            if tableau[rayon.position[1],rayon.position[0]] == "/" :
                #print("if /")
                #sens_mouvement = tuple(map(lambda x: x * -1, sens_mouvement))
                #rappel : map(fonction,liste) ; applique une fonction à tous les éléments de la liste, tuple ou tout autre itérable
                # fonction lambda : une fonction définie localement (ici : f(x) = -x )
                rayon.sens=transformation_coordonnees(rayon.sens,-1)
                """(1,0) ==> (0,-1)
                 (0,-1) ==> (1,0)
                 (-1,0]) ==> (0,1)
                 (0,1) ==> (-1,0)"""
            elif tableau[rayon.position[1],rayon.position[0]] == "\\" :
                #print("if \\ ")
                rayon.sens=transformation_coordonnees(rayon.sens,1)
                """(1,0) ==> (0,1)
                  (0,-1) ==> (-1,0)
                  (-1,0]) ==> (0,1)
                  (0,1) ==> (-1,0)"""
            elif tableau[rayon.position[1],rayon.position[0]] == "|" and rayon.sens[1]==0  : #mouvement horizontal
                #print(f"on est dans le cas '|', sur la position : {rayon.position}, dans le sens {rayon.sens}, rayon.sens[1] = {rayon.sens[1]}")
                rayon.sens=(0,1) #le rayon part vers le haut, sa nouvelle position sera traitée plus bas.
                liste_rayons.append(Rayon((rayon.position[0],rayon.position[1]-1),(0,-1))) #on créé un nouveau rayon à la même position mais qui part vers le bas
                # et on le décale d'un cran vers le bas (nécessaire pour ne pas boucler de manière infinie, sinon le rayon se situe sur le caractère "|" et au prochain passage, il sera de nouveau split
            elif tableau[rayon.position[1], rayon.position[0]] == "-" and rayon.sens[0] == 0 : # mouvement vertical
                #print(f"on est dans le cas '-', sur la position : {rayon.position}, dans le sens {rayon.sens}, rayon.sens[0] = {rayon.sens[0]}")
                rayon.sens = (1, 0)  # le rayon part vers la droite
                liste_rayons.append(Rayon((rayon.position[0]-1,rayon.position[1]), (-1, 0)))  # on créé un nouveau rayon à la même position mais qui part vers la gauche
                #et on le décale d'un vers la gauche
            #else : sens_mouvement = sens_mouvement : on est sur un "." , un "|" en mouvement vertical ou un "-" en mouvement horizontal
            etat_rayon.append((rayon.position,rayon.sens))
            rayon.position = rayon.deplacement_rayon()
            if rayon.position not in liste_positions and tableau[rayon.position[1],rayon.position[0]] != "%":
                liste_positions.append(rayon.position)
            #print(f"position : {rayon.position}, liste des positions : {liste_positions}")
    return liste_rayons, liste_positions


if partie == "partie1" :
    liste_positions_depart = [Rayon((1, 1), (1, 0))]
if partie == "partie2" :
    liste_positions_depart = []
    for numero_ligne in range(1,tableau.shape[0]-2):
        liste_positions_depart.append(Rayon((1,numero_ligne),(1,0))) #toutes les entrées par le côté gauche et allant vers la droite, sauf les bordures
        liste_positions_depart.append(Rayon((tableau.shape[1]-2,numero_ligne),(-1,0))) #toutes les entrées par le côté droit et allant vers la gauche, sauf les bordures

    for numero_colonne in range(1,tableau.shape[1]-2):
        liste_positions_depart.append(Rayon((numero_colonne, 1), (0, 1)))  # toutes les entrées par le haut et allant vers le bas, sauf les bordures
        liste_positions_depart.append(Rayon((numero_colonne, tableau.shape[0]-2), (0, -1))) # toutes les entrées par le bas et allant vers le haut, sauf les bordures

    print(f"nombre de positions de départ différentes : {len(liste_positions_depart)}")

liste_nombre_energisés=[]
for numero_rayon_entree, rayon_entree in enumerate(liste_positions_depart) :
    liste_rayons_complete = [Rayon((1, 1), (1, 0))]
    liste_positions_par_entree = []
    rayons_non_traites = [rayon_entree]
    print(f"on traite le rayon en entrée n° {numero_rayon_entree+1}, de position {rayon_entree.position} et de sens {rayon_entree.sens}")
    while rayons_non_traites != []:
        for numero_rayon, rayon in enumerate(rayons_non_traites):
            print(f"on a {len(rayons_non_traites)} rayons non traités, on traite le n° {numero_rayon+1}, position : {rayon.position}, sens : {rayon.sens} ")

            liste_rayons, liste_positions = trajet_rayon(rayon,liste_positions_par_entree)
            print(f"liste positions parcourues par le rayon non traité n° {numero_rayon+1} du rayon en entrée n° {numero_rayon_entree+1} :\n{liste_positions}")

        rayons_non_traites = gestion_liste_rayons(liste_rayons_complete,liste_rayons)
        for _ in range(len(rayons_non_traites)):
            print(f"liste rayons non traités, de longueur {len(rayons_non_traites)} : {rayons_non_traites[_].position} de sens {rayons_non_traites[_].sens}")

        liste_rayons_complete.extend(rayons_non_traites)
        liste_rayons_complete=copy.deepcopy(liste_rayons_complete)
    print(f"le rayon n° {numero_rayon_entree + 1} a énergisé {len(liste_positions_par_entree)} positions : {liste_positions_par_entree}")
    liste_nombre_energisés.append(len(liste_positions_par_entree))
    #print(f"liste des positions en entrée : {liste_positions_par_entree}")


réponse_index,réponse=max(enumerate(liste_nombre_energisés),key=lambda x: x[1])
print(f"parcours le plus énergisé : {réponse}, obtenu pour le rayon en entrée n° {réponse_index+1}")








