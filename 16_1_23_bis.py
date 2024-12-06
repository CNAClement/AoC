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
start=time.time()
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

class Rayon:
    def __init__(self,position:tuple,sens:tuple): #,etat:str ="non traité"):
        self.position = position
        self.sens = sens
        #self.etat = etat

    def __eq__(self, other):
        return isinstance(other, Rayon) and \
               self.position == other.position and \
               self.sens == other.sens

    def __ne__(self, other):
        return not self.__eq__(other)
    def deplacement_rayon(self):
        position=tuple(x + y for x, y in zip(self.position, self.sens))
        return position
def transformation_coordonnees(coordonnees,facteur):
    x,y=coordonnees
    nouvelles_coordonnees = (y*facteur, x*facteur)
    return nouvelles_coordonnees


def gestion_liste_rayons(liste_rayons_traites, liste_rayons) :
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
            for rayon_traite in liste_rayons_traites
        )
    ]
        # La nouvelle liste_non_traitee ne contiendra plus les éléments qui correspondent à la liste_traitee
    return rayons_non_traites

def trajet_rayon(rayon,liste_positions) :
    liste_rayons=[] #on mettra dans cette liste les rayons créés après un split contre "|" ou "-"
    etats_rayon=[] #contient tuple (position,sens) pour vérifier qu'on ne boucle pas (si un rayon tourne en rond et repasse dans le même état, il sera enlevé)
    if rayon.position not in liste_positions and tableau[rayon.position[1], rayon.position[0]] != "%":
            liste_positions.append(rayon.position) #On le met en haut de la fonction également pour être sûr d'ajouter les rayons qui rentrent ici (après split par exemple)
    while tableau[rayon.position[1],rayon.position[0]]!='%' and rayon not in etats_rayon :
        #print(f"on est dans le while, on traite le rayon de position {rayon.position} et de sens {rayon.sens}")
        if tableau[rayon.position[1],rayon.position[0]] == "/" :
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
            #print("if |")
            rayon.sens=(0,1) #le rayon part vers le bas, sa nouvelle position sera traitée à la fin de la fonction.
            liste_rayons.append(Rayon((rayon.position[0],rayon.position[1]-1),(0,-1))) #on créé un nouveau rayon à la même position mais qui part vers le haut
            # et on le décale d'un cran vers le haut (nécessaire pour ne pas boucler de manière infinie, sinon le rayon se situe sur le caractère "|" et au prochain passage, il sera de nouveau split
        elif tableau[rayon.position[1], rayon.position[0]] == "-" and rayon.sens[0] == 0 : # mouvement vertical
            rayon.sens = (1, 0)  # le rayon part vers la droite, sa nouvelle position sera traitée à la fin de la fonction.
            liste_rayons.append(Rayon((rayon.position[0]-1,rayon.position[1]), (-1, 0)))  # on créé un nouveau rayon à la même position mais qui part vers la gauche
            #et on le décale d'un vers la gauche
        #else : sens_mouvement = sens_mouvement : on est sur un "." , un "|" en mouvement vertical ou un "-" en mouvement horizontal
        etat_deep_save = copy.deepcopy(rayon)
        etats_rayon.append(etat_deep_save) #on stocke l'état avant de calculer la nouvelle position, au cas où on revient plus tard sur cet état
        rayon.position = rayon.deplacement_rayon()
        #print(f"rayon traité : position : {rayon.position} et sens : {rayon.sens}.")

        if rayon.position not in liste_positions and tableau[rayon.position[1],rayon.position[0]] != "%":
            liste_positions.append(rayon.position)
    #for _ in range(len(liste_rayons)):
        #print(f"liste des rayons à la fin du traitement : {liste_rayons[_].position}, de sens : {liste_rayons[_].sens}")
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
    #liste_rayons_complete = [Rayon((1, 1), (1, 0))]
    liste_rayons_traites = []
    liste_positions_par_entree = []
    rayons_non_traites = [rayon_entree]
    #print(f"on traite le rayon en entrée n° {numero_rayon_entree+1}, de position {rayon_entree.position} et de sens {rayon_entree.sens}")
    while rayons_non_traites != []:
        liste_rayons_produits_totaux = []
        for numero_rayon, rayon_non_traite in enumerate(rayons_non_traites):
            #print(f"on a {len(rayons_non_traites)} rayons non traités, on traite le n° {numero_rayon+1}, position : {rayon_non_traite.position}, sens : {rayon_non_traite.sens} ")
            rayon_deep_save = copy.deepcopy(rayon_non_traite) #on fige l'état de l'instance avant qu'il n'évolue au cours de son traitement
            liste_rayons_traites.append(rayon_deep_save)
            liste_rayons_produits_fonction, liste_positions = trajet_rayon(rayon_non_traite,liste_positions_par_entree)
            #on traite un rayon à la fois, cela renvoie une liste de plusieurs rayons produits entre temps. Cette liste est réinitialisée à chaque passage, on la conserve dans une autre liste
            liste_rayons_produits_totaux.extend(liste_rayons_produits_fonction)

            #for _ in range(len(liste_rayons_produits_totaux)):
                #print(f"rayons totaux : {liste_rayons_produits_totaux[_].position}, de sens : {liste_rayons_produits_totaux[_].sens}")

            #print(f"liste positions parcourues :\n{liste_positions}")

        rayons_non_traites = gestion_liste_rayons(liste_rayons_traites,liste_rayons_produits_totaux)

    print(f"le rayon n° {numero_rayon_entree + 1} a énergisé {len(liste_positions_par_entree)} positions : {liste_positions_par_entree}")
    liste_nombre_energisés.append(len(liste_positions_par_entree))


réponse_index,réponse=max(enumerate(liste_nombre_energisés),key=lambda x: x[1])
print(f"parcours le plus énergisé : {réponse}, obtenu pour le rayon en entrée n° {réponse_index+1} en {time.time()-start} secondes")








