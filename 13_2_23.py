import re
import sys
import time
import numpy as np
#48402 too high
with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\13_1_ori.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")


def symetrie_verticale(tableau) :
    reponse_colonne_tableau = 0
    flag_symetrie_verticale=0
    #print(f"type tableau : {type(tableau)}, nombre de dimensions du tableau : {tableau.ndim}")
    smudge_corrige = 0
    for numero_colonne in range(tableau.shape[1]):
        print(f"On traite la colonne {numero_colonne+1} du tableau : ")
        nombre_ecarts_axe = 0
        for index in range(min(numero_colonne + 1, (tableau.shape[1] - numero_colonne - 1))):  # si shape[1]=7 et numero_colonne = 4 (cad colonne n°5 ) ==>
            print(f"on est sur l'index {index} donc on compare les colonnes {numero_colonne-index+1} et {numero_colonne+1+index+1}, nombre d'écarts : {nombre_ecarts_axe}")
            ligne_en_ecart_temp = np.where(tableau[:, numero_colonne - index] != tableau[:, numero_colonne + 1 + index])[0]  # on ajoute les coordonnées en écart
            print(f"indices en écart : {ligne_en_ecart_temp}, longueur : {len(ligne_en_ecart_temp)}")
            if len(ligne_en_ecart_temp) == 1:  # un seul écart sur la ligne en cours de traitement :
                nombre_ecarts_axe += 1
                colonne_en_ecart = numero_colonne - index
                ligne_en_ecart = ligne_en_ecart_temp.copy() #colonne_en_ecart_temp risque d'être réinitialisée dans la suite de la boucle
                print(f"ligne en écart : {ligne_en_ecart+1}, colonne_en_ecart : {colonne_en_ecart+1}, longueur : {len(ligne_en_ecart)}, nombre d'écarts : {nombre_ecarts_axe}, smudge corrigé : {smudge_corrige}")
            elif len(ligne_en_ecart_temp) > 1:
                nombre_ecarts_axe += 2 #on rajoute au moins 2 pour ne pas tomber dans le if suivant
                print("coucou")
                break
        if nombre_ecarts_axe == 1 and smudge_corrige == 0:  # un seul écart sur l'ensemble des colonnes traitées
            ligne_en_ecart=ligne_en_ecart[0]
            print(f"liste diff : {ligne_en_ecart}, valeur avant : {tableau[ligne_en_ecart][colonne_en_ecart]} : {tableau[5][0]}  pour ligne {ligne_en_ecart+1} et colonne {colonne_en_ecart+1} ")
            tableau[ligne_en_ecart][colonne_en_ecart] = correction_smudge(tableau[ligne_en_ecart][colonne_en_ecart])
            flag_symetrie_verticale = 1
            smudge_corrige = 1
        else:
            flag_symetrie_verticale = 0

        if flag_symetrie_verticale == 1 :
            #symétrie totale pour cette colonne
            #print(f"symétrie entre les colonnes {numero_colonne+1} et {numero_colonne+2}: {tableau[:,numero_colonne]} et {tableau[:,numero_colonne+1]}")
            reponse_colonne_tableau+=int(numero_colonne+1)
            flag_symetrie_verticale=0
    return reponse_colonne_tableau

def symetrie_horizontale(tableau) :
    reponse_ligne_tableau = 0
    flag_symetrie_horizontale = 0
    smudge_corrige = 0
    for numero_ligne in range(tableau.shape[0]):
        #print(f"On traite la ligne {numero_ligne+1} du tableau : ")
        nombre_ecarts_axe=0
        for index in range(min(numero_ligne+1,(tableau.shape[0]-numero_ligne-1))): # si shape[0]=7 et numero_ligne = 4 (cad ligne n°5 ) ==>
            #on compare d'abord lignes 5 et 6 , puis lignes 4 et 7 ==> deux tours de comparaison, index vaut 0 puis 1 (jamais 2)
            #print(f"on est sur l'index {index} donc on compare les lignes {numero_ligne-index+1} et {numero_ligne+1+index+1}")
            #print(f"on compare les lignes {tableau[numero_ligne-index]} et {tableau[numero_ligne+1+index]}")
            colonne_en_ecart_temp = np.where(tableau[numero_ligne-index]!=tableau[numero_ligne+1+index])[0] #on ajoute les coordonnées en écart
            #print(f"indices en écart : {colonne_en_ecart_temp}, longueur : {len(colonne_en_ecart_temp)}")
            if len(colonne_en_ecart_temp) ==1 : #un seul écart sur la ligne en cours de traitement :
                nombre_ecarts_axe += 1
                ligne_en_ecart=numero_ligne-index
                colonne_en_ecart = colonne_en_ecart_temp.copy() #colonne_en_ecart_temp risque d'être réinitialisée dans la suite de la boucle
                #print(f"ligne en écart : {ligne_en_ecart+1}, colonne_en_ecart : {colonne_en_ecart+1}, longueur : {len(colonne_en_ecart)}, nombre d'écarts : {nombre_ecarts_axe}, smudge corrigé : {smudge_corrige}")
            elif len(colonne_en_ecart_temp) > 1 :
                nombre_ecarts_axe += 2 #on rajoute au moins 2 pour ne pas tomber dans le if suivant
                break
        if nombre_ecarts_axe==1 and smudge_corrige==0: #un seul écart sur l'ensemble des lignes traitées
            #print(f"liste diff : {colonne_en_ecart}, valeur avant : {tableau[ligne_en_ecart][colonne_en_ecart]} pour ligne {ligne_en_ecart+1} et colonne {colonne_en_ecart+1} ")
            tableau[ligne_en_ecart][colonne_en_ecart] = correction_smudge(tableau[ligne_en_ecart][colonne_en_ecart])
            flag_symetrie_horizontale=1
            smudge_corrige=1
        else :
            flag_symetrie_horizontale=0

        if flag_symetrie_horizontale == 1 :
            #symétrie totale pour cette ligne
            #print(f"symétrie entre les lignes {numero_ligne+1} et {numero_ligne+2}: {tableau[numero_ligne]} et {tableau[numero_ligne+1]}")
            reponse_ligne_tableau+=numero_ligne+1
            flag_symetrie_horizontale=0
    return reponse_ligne_tableau, tableau

def correction_smudge(smudge):
    if smudge == "#":
        smudge = "."
    elif smudge == ".":
        smudge = "#"
    else :
        print(f"problème avec le tableau, la valeur n'est ni # ni . : {smudge}")
        sys.exit("Valeur incorrecte")
    return smudge


reponse_colonne = 0
reponse_ligne = 0

pattern_separation = re.compile(r"(\n\s*\n)")

liste_tableaux_plats = re.split(pattern_separation, contenu)

# Supprimer les éléments vides de la liste
liste_tableaux_plats = [tableau.strip() for tableau in liste_tableaux_plats if tableau.strip()]

for numero_tableau_traite, tableau_plat in enumerate(liste_tableaux_plats) :
    lignes = tableau_plat.splitlines()
    new_list = []
    for ligne in lignes:
        for caractere in ligne:
            new_list.append(caractere)
    array = np.asarray(new_list)
    tableau = array.reshape(int(len(lignes)), int(len(lignes[0])))
    print(f"on traite le tableau n° {numero_tableau_traite+1}, nombre de lignes : {tableau.shape[0]}, nombre de colonnes : {tableau.shape[1]}")
    print(f"tableau : {tableau}")

    reponse_ligne_tableau, tableau = symetrie_horizontale(tableau)
    reponse_ligne += reponse_ligne_tableau
    if reponse_ligne_tableau == 0 :
        reponse_colonne_tableau = symetrie_verticale(tableau)
        reponse_colonne += reponse_colonne_tableau
        #print(f"symétrie colonne : {reponse_colonne_tableau}")
    #print(f"symétrie ligne : {reponse_ligne_tableau}, symétrie colonne : {reponse_colonne_tableau}")
    #print(f"symétrie ligne : {reponse_ligne_tableau}")
    print(f"réponse : {reponse_colonne + 100 * reponse_ligne}")

print(f"réponse colonne : {reponse_colonne}, réponse ligne : {reponse_ligne}")
print(f"réponse : {reponse_colonne+100*reponse_ligne}")
