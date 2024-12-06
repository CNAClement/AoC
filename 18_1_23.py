import re
import sys
import time
import copy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from dataclasses import dataclass
from scipy.ndimage import binary_fill_holes


#49282 too high


with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\18_1_ori.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")
start=time.time()
partie="partie1"

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


def plot_table(table):
    cmap = plt.cm.get_cmap('tab10', len(np.unique(table)))  # Choix d'une colormap (tab10 pour 10 couleurs distinctes)

    fig, ax = plt.subplots()
    ax.axis('off')

    # Création d'un tableau coloré
    ax.table(cellText=[[' ' if cell == '.' else cell for cell in row] for row in table],
             loc='center',
             cellLoc='center',
             edges='open',
             cellColours=[[cmap(0) if cell == '#' else 'white' for cell in row] for row in table])

    plt.show()

def traitement_instruction(tableau, pelleteur_en_chef, longueur, numero_instruction):
    if pelleteur_en_chef.direction in ("U","D"):
        for numero_ligne in range(pelleteur_en_chef.position[1],
                                  pelleteur_en_chef.position[1]+longueur*dico_correspondance[pelleteur_en_chef.direction],
                                  dico_correspondance[pelleteur_en_chef.direction]):
            #si "U" , on multiplie par -1 (dico["U" ] ) et on parcourt donc en sens inverse les lignes du tableau.
            pelleteur_en_chef.deplacement_vertical(dico_correspondance[pelleteur_en_chef.direction])
            #si vers le bas, on ajoute 1 à la ligne, si vers le haut, on enlève 1
            #if pelleteur_en_chef.position[1] == 1:
                #print("on doit agrandir le tableau vers le haut")
                #tableau = np.pad(tableau, ((1, 0), (0, 0)), constant_values='.')
            if pelleteur_en_chef.position[1] == 1 or pelleteur_en_chef.position[1] == tableau.shape[0] :
                print(f"limite verticale atteinte : {pelleteur_en_chef.position} pour l'instruction n° {numero_instruction +1}, déplacement dans le sens : {pelleteur_en_chef.direction}")
            tableau[pelleteur_en_chef.position[1]-1][pelleteur_en_chef.position[0]-1]="#"  #le -1 permet de traduire les coordonnées "françaises" en "python" (1 ==> 0)

    if pelleteur_en_chef.direction in ("R","L"):
        for numero_colonne in range(pelleteur_en_chef.position[0],
                                    pelleteur_en_chef.position[0]+longueur*dico_correspondance[pelleteur_en_chef.direction],
                                    dico_correspondance[pelleteur_en_chef.direction]):
            #si "L" , on multiplie par -1 (dico["L" ] ) et on parcourt donc en sens inverse les colonnes du tableau.
            pelleteur_en_chef.deplacement_horizontal(dico_correspondance[pelleteur_en_chef.direction])
            if pelleteur_en_chef.position[0] == 1 or pelleteur_en_chef.position[0] == tableau.shape[1] :
                print(f"limite horizontale atteinte : {pelleteur_en_chef.position} pour l'instruction n° {numero_instruction +1}")
            #si vers la droite, on ajoute 1 à la ligne, si vers la gauche, on enlève 1
            tableau[pelleteur_en_chef.position[1]-1][pelleteur_en_chef.position[0]-1]="#"  #le -1 permet de traduire les coordonnées "françaises" en "python" (1 ==> 0)



    return tableau

def remplissage_pas_opti(tableau):
    #le but est de valoriser les points qui ont un # à leur gauche et un # à leur droite
    for numero_ligne in range(tableau.shape[0]):
        for numero_colonne in range(tableau.shape[1]):
            flag_gauche = any(tableau[numero_ligne, :numero_colonne] == "#")
            flag_droite = any(tableau[numero_ligne, numero_colonne + 1:] == "#")
            if  flag_gauche == True and flag_droite == True :
                tableau[numero_ligne][numero_colonne] = "#"
    return tableau

def remplissage(tableau):
    tableau_binaire = (tableau == '#').astype(int)
    contours_remplis = binary_fill_holes(tableau_binaire)
    tableau = np.where(contours_remplis, '#', tableau)
    return tableau



tableau=np.full((500,420),".")
print(f"nombres de ligne du tableau : {tableau.shape[0]}, nombre de colonnes : {tableau.shape[1]}, dimensions : {tableau.ndim}")
#print(tableau)
pattern_instruction = re.compile("(R|L|U|D)[ ]+(\d+)[ ]+(\(#[A-Za-z0-9]+\))")
dico_correspondance = {"U":-1,"D":1,"R":1,"L":-1}
pelleteur_en_chef = Pelleteur((10,250),"R") #définie arbitrairement


for numero_instruction, instruction in enumerate(lignes) :
    match=re.search(pattern_instruction,instruction)
    if match:
        pelleteur_en_chef.direction = match.group(1)
        longueur_deplacement = int(match.group(2))
        couleur = match.group(3)
    else :
        print(f"pattern non reconnu pour l'instruction {instruction}")
        sys.exit("Instruction non reconnue. Arrêt du programme")
    tableau=traitement_instruction(tableau,pelleteur_en_chef, longueur_deplacement, numero_instruction)
print(f"Première partie du code en {time.time()-start} secondes")
tableau=remplissage(tableau)
tableau=remplissage_pas_opti(tableau)
print(f"résultat : {np.count_nonzero(tableau == '#')} en {time.time()-start} secondes")

#plot_table(tableau)
