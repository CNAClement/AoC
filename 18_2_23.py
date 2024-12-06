import re
import sys
import time
import copy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from dataclasses import dataclass
from scipy.ndimage import binary_fill_holes


#98293274587848 too high


with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\18_1_ori.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")
start=time.time()
partie="partie2"

class Pelleteur:
    def __init__(self,position:tuple,direction:tuple):
        self.position = position
        self.direction = direction

    def __eq__(self, other):
        return isinstance(other, Pelleteur) and \
               self.position == other.position and \
               self.direction == other.direction

    def __ne__(self, other):
        return not self.__eq__(other)

    def deplacement_horizontal(self,longueur):
        self.position = (self.position[0]+longueur,self.position[1])
        return self.position

    def deplacement_vertical(self,longueur):
        self.position = (self.position[0],self.position[1]+longueur)
        return self.position


def traitement_instruction( pelleteur_en_chef, longueur ):
    if pelleteur_en_chef.direction in ("U","D"):
        état_debut=copy.deepcopy(pelleteur_en_chef)
        pelleteur_en_chef.deplacement_vertical(dico_correspondance[pelleteur_en_chef.direction]*longueur)
        for numero_ligne in range(état_debut.position[1],
                                  pelleteur_en_chef.position[1]+dico_correspondance[pelleteur_en_chef.direction], #permet de fixer la fin de la borne, +1 si on est de haut en bas et -1 si on est de bas en haut (c'est à dire range(9,7,-1)
                                  dico_correspondance[pelleteur_en_chef.direction]):
            if numero_ligne in dico_ordonnées:
                if pelleteur_en_chef.position[0] < dico_ordonnées[numero_ligne][0]:
                    dico_ordonnées[numero_ligne][0]=pelleteur_en_chef.position[0]
                if pelleteur_en_chef.position[0] > dico_ordonnées[numero_ligne][1]:
                    print(f"on met à jour le maximum pendant la descente sur la position : {pelleteur_en_chef.position[0]} (ancienne position : {dico_ordonnées[numero_ligne][1]}")
                    dico_ordonnées[numero_ligne][1]=pelleteur_en_chef.position[0]
            else :
                dico_ordonnées[numero_ligne]=[pelleteur_en_chef.position[0],pelleteur_en_chef.position[0]] #si la ligne n'a jamais été croisée,
                # alors on initialise le début et la fin avec la valeur par laquelle on passe dans ce mouvement vertical

    if pelleteur_en_chef.direction in ("R","L"):
        état_debut=copy.deepcopy(pelleteur_en_chef)
        pelleteur_en_chef.deplacement_horizontal(dico_correspondance[pelleteur_en_chef.direction]*longueur)
        if pelleteur_en_chef.position[1] in dico_ordonnées:
            if min(état_debut.position[0],pelleteur_en_chef.position[0]) < dico_ordonnées[pelleteur_en_chef.position[1]][0]:
                dico_ordonnées[pelleteur_en_chef.position[1]][0]=min(état_debut.position[0],pelleteur_en_chef.position[0])
                #si pour la ligne considérée (donc position[1], la première valeur renvoyée par le dico (donc [O] est supérieure au min : on met à jour
                #exemple : {4:[3,9]} : pour la ligne 4, le min est 3 et le max est 9. dico[4] = [3,9]. dico[4][0]=3 Donc si abscisse position < dico[4][O] ==> on met à jour
            if max(état_debut.position[0],pelleteur_en_chef.position[0]) > dico_ordonnées[pelleteur_en_chef.position[1]][1]:
                dico_ordonnées[pelleteur_en_chef.position[1]][1]=max(état_debut.position[0],pelleteur_en_chef.position[0])

        else :
            dico_ordonnées[pelleteur_en_chef.position[1]]=[min(état_debut.position[0],pelleteur_en_chef.position[0]),max(état_debut.position[0],pelleteur_en_chef.position[0])]
    print(f"déplacement dans le sens : {pelleteur_en_chef.direction} de longueur {longueur}, position initiale : {état_debut.position}, position d'arrivée : {pelleteur_en_chef.position}")
92966329726
92966441736

pattern_instruction = re.compile("(R|L|U|D)[ ]+(\d+)[ ]+(\(#[A-Za-z0-9]+\))")
dico_correspondance = {"U":-1,"D":1,"R":1,"L":-1}  #ça change avec la partie 2
dico_ordonnées = {}
pelleteur_en_chef = Pelleteur((0,0),"R") #définie arbitrairement


for numero_instruction, instruction in enumerate(lignes) :
    match=re.search(pattern_instruction,instruction)
    if match:
        if partie=="partie1" :
            pelleteur_en_chef.direction = match.group(1)
            longueur_deplacement = int(match.group(2))
        elif partie=="partie2":
            infos_partie2 = match.group(3)
            longueur_deplacement=int(infos_partie2[2:7], 16) #convertit les caractères 2 à 6 de la chaine en entier (le "16" signifie que la base initiale est hexadécimale)
            direction_hexa = (
                "R" if infos_partie2[7:8] == "0" else
                "D" if infos_partie2[7:8] == "1" else
                "L" if infos_partie2[7:8] == "2" else
                "U" if infos_partie2[7:8] == "3" else
                "autre_valeur"
            )
            pelleteur_en_chef.direction=direction_hexa
    else :
        print(f"pattern non reconnu pour l'instruction {instruction}")
        sys.exit("Instruction non reconnue. Arrêt du programme")

    traitement_instruction(pelleteur_en_chef, longueur_deplacement)
#print(dico_ordonnées[-829975])
#   print(dico_ordonnées[0])
#print(dico_ordonnées)

réponse = 0
for indice in dico_ordonnées:
    réponse+=dico_ordonnées[indice][1]-dico_ordonnées[indice][0]+1

print(f"résultat : {réponse} en {time.time()-start} secondes")

#plot_table(tableau)
