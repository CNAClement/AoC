import re
import sys
import time
import numpy as np
with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\14_1_ori.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")
start=time.time()

partie="partie2"
dict_sens = dict([(0,"nord"),(1,"ouest"),(2,"sud"),(3,"est")])

new_list=[]
for ligne in lignes:
    for caractere in ligne :
        new_list.append(caractere)
array=np.asarray(new_list)
#print(f" array : {array} , nombre de lignes : {int(len(lignes))}, taille d'une ligne : {int(len(lignes[0]))}")
tableau=array.reshape(int(len(lignes)), int(len(lignes[0])))

pierres_rondes = ['O','0','0','0']

def remonter_pierres(tableau) :
    for numero_colonne in range(tableau.shape[1]):
        for numero_ligne in range (tableau.shape[0]-1,0,-1) :
            #print(f"ligne, colonne : {numero_ligne} , {numero_colonne}, caractère : {tableau[numero_ligne][numero_colonne]} , caractère du dessus : {tableau[numero_ligne-1][numero_colonne]}")
            if tableau[numero_ligne][numero_colonne] in pierres_rondes :
                if tableau[numero_ligne-1][numero_colonne] == '.':
                    #print(f"caractère {tableau[numero_ligne][numero_colonne]} trouvé ligne : {numero_ligne + 1} et colonne {numero_colonne + 1}, le caractère du dessus est : {tableau[numero_ligne - 1][numero_colonne]}")
                    #objet_rond = tableau[numero_ligne][numero_colonne]
                    tableau[numero_ligne - 1][numero_colonne] = '0' #objet_rond si besoin de gérer la différence
                    tableau[numero_ligne][numero_colonne] = '.'
                    #print(f"sortie de if : caractère {tableau[numero_ligne][numero_colonne]} désormais ligne {numero_ligne + 1} et colonne {numero_colonne + 1}, le caractère du dessus est désormais {tableau[numero_ligne - 1][numero_colonne]}")

        #print(f"tableau sortie de boucle : \n \n \n {tableau}")

    return tableau

def rotation_tableau(tableau):
    #tableau = [[row[i] for row in tableau] for i in range(len(tableau[0]) - 1, -1, -1)]
    tableau = np.transpose(tableau, axes=(1, 0))[:, ::-1] #transposition puis inversion du sens des colonnes
    return tableau

def calculer_poids(tableau):
    poids_total = 0
    for numero_colonne in range(tableau.shape[1]):
        for numero_ligne in range (tableau.shape[0]-1,-1,-1) :
            if tableau[numero_ligne][numero_colonne] in pierres_rondes :
                poids_total+=tableau.shape[0]-numero_ligne
                #print(f"ligne : {numero_ligne + 1} et colonne {numero_colonne + 1} : poids total = {poids_total} ")
    return poids_total

def remonter_pierres_complet(tableau):
    tableau_save = tableau.copy()
    tableau = remonter_pierres(tableau)

    while np.array_equal(tableau , tableau_save) == False :
        tableau_save=tableau.copy()
        tableau = remonter_pierres(tableau)
    return tableau

if partie=="partie1":
    tableau = remonter_pierres_complet(tableau)
    poids_total = calculer_poids(tableau)
    print(f"la réponse à la partie 1 : {poids_total} ")



elif partie=="partie2":
    nombre_cycles_souhaites = 1000000000
    liste_tableaux=[]
    liste_poids_calculés = []
    boucle_finie = False
    cycle=0
    #for cycle in range(104):
    while 1==1 :
        #print(f"cycle : {cycle + 1}")
        if boucle_finie == 0 :
            for sens in range(4):
                tableau = remonter_pierres_complet(tableau)
                #print(f"fin du sens : {dict_sens[sens]} : \n {tableau}")
                tableau = rotation_tableau(tableau)
            #print(f"fin du cycle {cycle+1} \n {tableau} \n \n")
            #print(f"liste tableaux : \n {liste_tableaux}")
            for numero_element, element in enumerate(liste_tableaux) :
                #print( f"élément\n{element} \n  tableau\n{tableau} \n")
                if np.array_equal(tableau , element) == True :
                    debut_boucle = numero_element
                    taille_boucle = cycle-numero_element #on a une boucle de longueur cycle-numero_element, atteinte après le nombre "cycle+1" de cycles, et qui commence à l'itération n° élément+1
                    print(f"on a fait une boucle, itération n° {cycle+1}, on a trouvé pour la première fois un tableau qui était déjà en position {numero_element+1} de la liste des tableaux déjà obtenus, longueur du cycle : {taille_boucle}")
                    boucle_finie = 1
                    break
            if boucle_finie == True :
                break

            poids_total = calculer_poids(tableau)
            liste_poids_calculés.append(poids_total)
            tableau_temp = tableau.copy()
            liste_tableaux.append(tableau_temp)
            cycle+=1
    print(f"la réponse à la partie 2 : {liste_poids_calculés[(nombre_cycles_souhaites-debut_boucle)%taille_boucle+debut_boucle-1]}, trouvée en {time.time()-start} secondes ")
    #Si la boucle commence pour la 1ere fois au rang 122, il y a donc 1000000000-122 (= 999999878) éléments à considérer dans ces boucles, c'est-à-dire pour une boucle de longueur 26, le nombre de boucles est partie entière de 1000000000/26  (= 38461533)
    #999999878 = 1000000000//26 + 1000000000%26 . Autrement dit, le nombre 999999878 est le même que le nombre 1000000000%26 (c'est-à-dire 20), donc le 20eme élément de la boucle, mais 38461533 boucles plus tard.
    #En prenant en compte tous les éléments, même les 122 premiers qui ne sont pas dans la boucle, le nombre 122+20 est le même que le nombre 122+999999878
print(liste_poids_calculés)

#La méthode ne marche pas (je ne comprends pas pourquoi). A noter que par chance, elle marche pour n = 1000 (je ne sais pas non plus pourquoi mais une étoile est une étoile)




