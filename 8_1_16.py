#UPOJFLBCEZ
import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2016\8_1_ori.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")

pattern_rotate=r'(x|y)=(\d+)[^\d]+(\d+)'
pattern_rectangle=r'rect (\d+)x(\d+)'

param_hauteur_ecran = 6
param_largeur_ecran = 50
ecran = np.full((param_hauteur_ecran,param_largeur_ecran),".")
print(f"hauteur de l'écran (ie : nombre de lignes) : {ecran.shape[0]}")
def traiter_instruction(ligne):
    if ligne[1]=="e":
        match=re.search(pattern_rectangle,ligne)
        if match :
            largeur=int(match.group(1))
            hauteur=int(match.group(2))
            #print(f"le rectangle est de largeur {largeur} et de hauteur {hauteur}")
            for largeur_pixel in range(largeur):
                for hauteur_pixel in range(hauteur):
                    ecran[hauteur_pixel][largeur_pixel]='#'
        else : print(f"Aucune correspondance trouvée pour la ligne '{ligne}'")
    elif ligne[7]=="c": #on va déplacer une colonne (autrement dit : on fixe le numéro colonne et on va modifier les lignes de chaque pixel)
        match=re.search(pattern_rotate,ligne)
        if match:
            colonne_impactee=int(match.group(2))
            longueur_deplacement=int(match.group(3))
            #print(f"la colonne {colonne_impactee} va être déplacée de {longueur_deplacement} pixels vers le bas")
            ecran_temp=ecran.copy()
            #print(f"écran avant : \n{ecran}")
            #print(f"colonne qui va être déplacée : {ecran[:,colonne_impactee]} ")
            for index in range(ecran.shape[0]):
                #print(f"index vaut {index}, (index+longueur_deplacement)%ecran.shape[0] vaut {(index+longueur_deplacement)%ecran.shape[0]}, le pixel impacté est {ecran[(index+longueur_deplacement)%ecran.shape[0]][colonne_impactee]}, le pixel à mettre à la place vaut {ecran_temp[index][colonne_impactee]}")
                ecran[(index+longueur_deplacement)%ecran.shape[0]][colonne_impactee]=ecran_temp[index][colonne_impactee] #si index+longueur_deplacement > taille max écran, on retourne en haut
            #print(f"écran après : \n{ecran}")
        else: print(f"Aucune correspondance trouvée pour la ligne '{ligne}'")
    elif ligne[7]=="r": #on va déplacer une ligne (row) (autrement dit, on va fixer une ligne et on va modifier les colonnes de chaque pixel)
        match=re.search(pattern_rotate,ligne)
        if match:
            ligne_impactee=int(match.group(2))
            longueur_deplacement=int(match.group(3))
            ecran_temp=ecran.copy()
            #print(f"écran avant : \n{ecran}")
            #print(f"ligne qui va être déplacée : {ecran[ligne_impactee][:]} ")
            for index in range(ecran.shape[1]):
                #print(f"index vaut {index}, (index + longueur_deplacement) % ecran.shape[1] vaut {(index + longueur_deplacement) % ecran.shape[1]}, le pixel impacté est {ecran[ligne_impactee][(index + longueur_deplacement) % ecran.shape[1]]}, le pixel par lequel il sera remplacé est {ecran_temp[ligne_impactee][index]}")
                ecran[ligne_impactee][(index + longueur_deplacement) % ecran.shape[1]] = ecran_temp[ligne_impactee][index]  # si index+longueur_deplacement > taille max écran, on retourne à gauche
            #print(f"écran après : \n{ecran}")
        else : print(f"Aucune correspondance trouvée pour la ligne '{ligne}'")
    else : print("revoir instruction")
    return(ecran)

def compter_pixels_allumés(ecran):
    compteur_pixels=0
    for pixel in ecran:
        if pixel=="2":
            compteur+=1
    return compteur_pixels

for ligne in lignes:
    print(ligne)
    ecran=traiter_instruction(ligne)
    print(f"Le nombre de pixels allumés est : {np.count_nonzero(ecran=='#')}")
# Affichage avec matplotlib
#plt.imshow(ecran == '#', cmap='BrBG', interpolation='nearest')
#plt.show()


# Convertir les caractères en valeurs numériques (1 pour '#', 0 pour '.')
valeurs_numeriques = (ecran == '#').astype(int)

couleurs_personnalisees = ListedColormap(['black', 'orange'])


# Affichage avec matplotlib en utilisant la carte de couleurs personnalisée
plt.imshow(valeurs_numeriques, cmap=couleurs_personnalisees, interpolation='nearest', aspect='auto', extent=[0, valeurs_numeriques.shape[1], 0, valeurs_numeriques.shape[0]])
plt.title('Tableau')
plt.show()