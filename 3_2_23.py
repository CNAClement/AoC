import numpy as np
#59205383 too low
with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\3_1_ori.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")

parametre_nombre_colonnes_tableau=len(lignes[0])
print(f"le tableau devrait avoir {len(lignes)} lignes et {parametre_nombre_colonnes_tableau} colonnes")
#print(f"lignes : {lignes}")

new_list=[]
for element in lignes:
    for caractere in element :
        new_list.append(caractere)

#print(f"la nouvelle liste de longueur {len(new_list)} vaut {new_list}")
array=np.asarray(new_list)

#tableau=array.reshape(parametre_colonnes_tableau,int(len(new_list)/parametre_colonnes_tableau))
tableau=array.reshape(int(len(new_list)/parametre_nombre_colonnes_tableau), parametre_nombre_colonnes_tableau)
#print(f"types : type de la ligne : {type(lignes)}, type de l'array : {type(array)}, type du tableau : {type(tableau)}")
#print(f"3 premières lignes du tableau 2d obtenu : \n {tableau[0:3]}")
#print(f"nombre de dimensions du tableau : {tableau.ndim}")
print(f"1ere ligne 2eme colonne du tableau : {tableau[0][1]}")
print(f"2eme ligne 1ere colonne du tableau : {tableau[1][0]}")
print(f"3eme ligne du tableau : {tableau[2]}")
print(f"3eme colonne du tableau : {tableau[:,2]}")
print(f"nombre de lignes du tableau: {tableau.shape[0]}, nombre de colonnes : {tableau.shape[1]} ")

def reperage_gears(numero_ligne,liste_coordonnees_gears):
    range_abscisses=[]
    for colonne in range(tableau.shape[1]):
        if tableau[numero_ligne][colonne]=="*":
            liste_coordonnees_gears.append((colonne+1,numero_ligne+1))
    return(liste_coordonnees_gears)

def reperage_nombres(numero_ligne,liste_coordonnees_nombres,association_nombre_coordonnees):
    liste_nombres=[]
    range_abscisses=[]
    flag_fin_de_nombre=1
    flag_debut_de_nombre=1 #ça peut sembler contre-intuitif, mais grâce à ces deux flags True, on va pouvoir rentrer dans la boucle comme après une fin de nombre (donc réinitialiser la variable nombre etc), et grâce au flag debut_de_nombre, on va pouvoir stocker la première coordonnée dès qu'on rencontrera un chiffre
    for colonne in range(tableau.shape[1]):
        if flag_fin_de_nombre==1:
            nombre=""
        if tableau[numero_ligne][colonne].isdigit()==True:
            flag_fin_de_nombre=0
            nombre+=tableau[numero_ligne][colonne]
            if flag_debut_de_nombre==True:
                flag_debut_de_nombre=0
                abscisse_debut = colonne +1
            if colonne==(tableau.shape[1]-1): #gestion du cas où le dernier caractère traité est un chiffre et que l'on n'aura donc pas l'occasion de passer dans le else
                liste_nombres.append(nombre)
                abscisse_fin = colonne
                range_abscisse_nombre = (abscisse_debut, abscisse_fin)
                # print(f"range abscisse du nombre : {range_abscisse_nombre}")
                range_abscisses.append(range_abscisse_nombre)
                for abscisse in range(abscisse_debut, abscisse_fin + 1):
                    liste_coordonnees_nombres.append((abscisse, numero_ligne + 1))
                    association_nombre_coordonnees.append([(abscisse, numero_ligne + 1), nombre])
        else :
            flag_fin_de_nombre=1
            if nombre!="":
                flag_debut_de_nombre=1
                flag_debut_de_nombre = 1
                liste_nombres.append(nombre)
                abscisse_fin=colonne
                range_abscisse_nombre=(abscisse_debut,abscisse_fin)
                #print(f"range abscisse du nombre : {range_abscisse_nombre}")
                range_abscisses.append(range_abscisse_nombre)
                for abscisse in range (abscisse_debut,abscisse_fin+1):
                    liste_coordonnees_nombres.append((abscisse, numero_ligne + 1))
                    association_nombre_coordonnees.append([(abscisse,numero_ligne+1),nombre])

    return(liste_nombres,liste_coordonnees_nombres,association_nombre_coordonnees)

def comparaison_coordonnees(liste_coordonnees_gears,liste_coordonnees_nombres,dico_association_nombre_coordonnees):
    somme_gear_ratio=0
    for coordonnees_gear in liste_coordonnees_gears:
        #print(f"coordonnees du gear en cours de test : {coordonnees_gear}")
        nombres_pour_gear_ratio = []
        compteur_nombres_adjacents = 0
        #recherche nombre sur la gauche (même ligne mais colonne-1 (ie : même ordonnée mais abscisse -1 )):
        if coordonnees_gear[0]!=1 and (coordonnees_gear[0]-1,coordonnees_gear[1]) in liste_coordonnees_nombres:
            #print(f"nombre trouvé à gauche du gear de coordonnees {coordonnees_gear}")
            compteur_nombres_adjacents+=1
            nombres_pour_gear_ratio.append(dico_association_nombre_coordonnees[(coordonnees_gear[0]-1,coordonnees_gear[1])])
        #recherche nombre sur la droite (même ligne mais colonne+1 (ie : même ordonnée mais abscisse + 1 )):
        if coordonnees_gear[0]!=tableau.shape[1] and (coordonnees_gear[0]+1,coordonnees_gear[1]) in liste_coordonnees_nombres:
            #print(f"nombre trouvé à droite du gear de coordonnees {coordonnees_gear}")
            compteur_nombres_adjacents+=1
            nombres_pour_gear_ratio.append(dico_association_nombre_coordonnees[(coordonnees_gear[0]+1,coordonnees_gear[1])])
        #recherche nombre sur le haut (même colonne mais ligne -1 (ie : même abscisse mais ordonnée -1 ) ):
        if coordonnees_gear[1]!=1 and (coordonnees_gear[0],coordonnees_gear[1]-1) in liste_coordonnees_nombres:
            #print(f"nombre trouvé en haut du gear de coordonnees {coordonnees_gear}")
            compteur_nombres_adjacents+=1
            nombres_pour_gear_ratio.append(dico_association_nombre_coordonnees[(coordonnees_gear[0],coordonnees_gear[1]-1)])
        else :#pas de nombre trouvé sur le haut, on vérifie les diagonales
        #recherche nombre sur la diagonale haut gauche (ligne-1 et colonne -1):
            if coordonnees_gear[0]!=1 and coordonnees_gear[1]!=1 and (coordonnees_gear[0]-1,coordonnees_gear[1]-1) in liste_coordonnees_nombres:
                #print(f"nombre trouvé en diagonale haut-gauche du gear de coordonnees {coordonnees_gear}")
                compteur_nombres_adjacents+=1
                nombres_pour_gear_ratio.append(dico_association_nombre_coordonnees[(coordonnees_gear[0]-1,coordonnees_gear[1]-1)])
        #recherche nombre sur la diagonale haut droite (ligne-1 et colonne +1):
            if coordonnees_gear[0]!=tableau.shape[1] and coordonnees_gear[1]!=1 and (coordonnees_gear[0]+1,coordonnees_gear[1]-1) in liste_coordonnees_nombres:
                #print(f"nombre trouvé en diagonale haut-droite du gear de coordonnees {coordonnees_gear}")
                compteur_nombres_adjacents+=1
                nombres_pour_gear_ratio.append(dico_association_nombre_coordonnees[(coordonnees_gear[0]+1,coordonnees_gear[1]-1)])
        #recherche nombre sur le bas (même colonne mais ligne+1 (ie : même abscisse mais ordonnee +1 ) ):
        if coordonnees_gear[1]!=tableau.shape[0] and (coordonnees_gear[0],coordonnees_gear[1]+1) in liste_coordonnees_nombres:
            #print(f"nombre trouvé en bas du gear de coordonnees {coordonnees_gear}")
            compteur_nombres_adjacents+=1
            nombres_pour_gear_ratio.append(dico_association_nombre_coordonnees[(coordonnees_gear[0],coordonnees_gear[1]+1)])
        else:  # pas de nombre trouvé sur le bas, on vérifie les diagonales
            # recherche nombre sur la diagonale bas gauche (ligne+1 et colonne -1):
            print(f"on recherche sur la coordonnée {(coordonnees_gear[0],coordonnees_gear[1]+1)} ")
            if coordonnees_gear[0] != 1 and coordonnees_gear[1] != tableau.shape[0] and (coordonnees_gear[0] - 1, coordonnees_gear[1] + 1) in liste_coordonnees_nombres:
                #print(f"nombre trouvé en diagonale bas-gauche du gear de coordonnees {coordonnees_gear}")
                compteur_nombres_adjacents += 1
                nombres_pour_gear_ratio.append(dico_association_nombre_coordonnees[(coordonnees_gear[0] - 1, coordonnees_gear[1] + 1)])
            # recherche nombre sur la diagonale bas droite (ligne+1 et colonne +1):
            if coordonnees_gear[0] != tableau.shape[1] and coordonnees_gear[1] != tableau.shape[0] and (coordonnees_gear[0] + 1, coordonnees_gear[1] + 1) in liste_coordonnees_nombres:
                #print(f"nombre trouvé en diagonale bas-droite du gear de coordonnees {coordonnees_gear}")
                compteur_nombres_adjacents += 1
                nombres_pour_gear_ratio.append(dico_association_nombre_coordonnees[(coordonnees_gear[0] + 1, coordonnees_gear[1] + 1)])
        if compteur_nombres_adjacents==2:
            gear_ratio=int(nombres_pour_gear_ratio[0])*int(nombres_pour_gear_ratio[1])
            somme_gear_ratio+=gear_ratio
            #print(f"Il y a exactement deux nombres adjacents au gear de coordonnées {coordonnees_gear}.\nLes nombres sont {nombres_pour_gear_ratio}")

        elif compteur_nombres_adjacents>2:
            print(f"ce gear a plus de deux nombres adjacents : {coordonnees_gear}.\nLes nombres sont {nombres_pour_gear_ratio}")

    return somme_gear_ratio


liste_coordonnees_gears=[]
liste_coordonnees_nombres=[]
association_nombre_coordonnees=[]
somme_gear_ratio=0


for numero_ligne in range(len(lignes)):
    #print(f"on traite la ligne n°{numero_ligne+1} du tableau.") # : {tableau[numero_ligne]}")
    liste_coordonnees_gears=reperage_gears(numero_ligne,liste_coordonnees_gears)
    liste_nombres, liste_coordonnees_nombres, association_nombre_coordonnees = reperage_nombres(numero_ligne,liste_coordonnees_nombres,association_nombre_coordonnees)


print(f"Il y a {len(liste_coordonnees_gears)} gears (liste des coordonnées : {liste_coordonnees_gears})")
print(f"liste des coordonnées des nombres : {liste_coordonnees_nombres}") #abscisse début, abscisse fin, ordonnée
dico_association_nombre_coordonnees=dict(association_nombre_coordonnees) #on fait un dictionnaire avant le dernier appel de fonction, plus pratique pour retrouver le nombre à partir de coordonnées
somme_gear_ratio=comparaison_coordonnees(liste_coordonnees_gears,liste_coordonnees_nombres,dico_association_nombre_coordonnees)

print(f"association nombres et coordonnees : {association_nombre_coordonnees}")
print(f"somme gear ratio (réponse à la partie 2) = {somme_gear_ratio}")

