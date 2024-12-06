import re
import sys
import time
import numpy as np
#48402 too high
with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\13_1.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")


def symetrie_verticale(tableau) :
    reponse_colonne_tableau = 0
    flag_symetrie_verticale=0
    #print(f"type tableau : {type(tableau)}, nombre de dimensions du tableau : {tableau.ndim}")
    for numero_colonne in range(tableau.shape[1]):
        for index in range(min(numero_colonne+1,(tableau.shape[1]-numero_colonne-1))): #pourquoi colonne+1 ? Si on traite colonne 0, il faut avoir range(1) pour traiter le cas index=0
            if np.all(tableau[:, numero_colonne - index] == tableau[:, numero_colonne + 1 + index]): #symétrie entre les colonnes n° numero_colonne et numero_colonne+1
                flag_symetrie_verticale=1
            else :
                print(f"smudge ? : {tableau[:, numero_colonne - index]}")
                break
        if flag_symetrie_verticale == 1 :
            #symétrie totale pour cette colonne
            #print(f"symétrie entre les colonnes {numero_colonne+1} et {numero_colonne+2}: {tableau[:,numero_colonne]} et {tableau[:,numero_colonne+1]}")
            reponse_colonne_tableau+=int(numero_colonne+1)
            flag_symetrie_verticale=0
    return reponse_colonne_tableau

def symetrie_horizontale(tableau) :
    reponse_ligne_tableau = 0
    flag_symetrie_horizontale = 0
    for numero_ligne in range(tableau.shape[0]):
        print(f"numero ligne : {numero_ligne}, shape : {tableau.shape[0]}")
        for index in range(min(numero_ligne+1,(tableau.shape[0]-numero_ligne-1))): # si shape[0]=7 et numero_ligne = 4 (cad ligne n°5 ) ==>
            #on compare d'abord lignes 5 et 6 , puis lignes 4 et 7 ==> deux tours de comparaison, index vaut 0 puis 1 (jamais 2)
            if np.all(tableau[numero_ligne-index]==tableau[numero_ligne+1+index]): #symétrie entre les lignes n° numero_ligne et numero_ligne+1
                #print(f"symétrie pour la ligne n° {numero_ligne} vraie à l'index : {index} :\n{tableau[numero_ligne-index]} et {tableau[numero_ligne+1+index]}" )
                flag_symetrie_horizontale =1
            else :
                flag_symetrie_horizontale = 0
                break
        if flag_symetrie_horizontale == 1 :
            #symétrie totale pour cette ligne
            #print(f"symétrie entre les lignes {numero_ligne+1} et {numero_ligne+2}: {tableau[numero_ligne]} et {tableau[numero_ligne+1]}")
            reponse_ligne_tableau+=numero_ligne+1
            flag_symetrie_horizontale=0
    return reponse_ligne_tableau


reponse_colonne = 0
reponse_ligne = 0

pattern_separation = re.compile(r"(\n\s*\n)")

liste_tableaux_plats = re.split(pattern_separation, contenu)

# Supprimer les éléments vides de la liste
liste_tableaux_plats = [tableau.strip() for tableau in liste_tableaux_plats if tableau.strip()]

for numero_tableau_traite, tableau_plat in enumerate(liste_tableaux_plats) :
    lignes = tableau_plat.splitlines()
    #print(f"on traite le tableau n° {numero_tableau_traite+1}, nombre de lignes : {tableau.shape[0]}, nombre de colonnes : {tableau.shape[1]}")
    new_list = []
    for ligne in lignes:
        for caractere in ligne:
            new_list.append(caractere)
    array = np.asarray(new_list)
        # print(f" array : {array} , nombre de lignes : {int(len(lignes))}, taille d'une ligne : {int(len(lignes[0]))}")
    tableau = array.reshape(int(len(lignes)), int(len(lignes[0])))
    print(f"on traite le tableau n° {numero_tableau_traite+1}, nombre de lignes : {tableau.shape[0]}, nombre de colonnes : {tableau.shape[1]}")
    #print(f"tableau : {tableau}")
    reponse_colonne_tableau = symetrie_verticale(tableau)
    reponse_colonne += reponse_colonne_tableau
    reponse_ligne_tableau = symetrie_horizontale(tableau)
    reponse_ligne += reponse_ligne_tableau
    print(f"symétrie ligne : {reponse_ligne_tableau}, symétrie colonne : {reponse_colonne_tableau}")

#print(f"réponse colonne : {reponse_colonne}, réponse ligne : {reponse_ligne}")
print(f"réponse partie 1 : {reponse_colonne+100*reponse_ligne}")