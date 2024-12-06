import numpy as np
#540324 too low
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

def reperage_nombre(numero_ligne):
    print(f"on traite la ligne n°{numero_ligne+1} du tableau.") # : {tableau[numero_ligne]}")
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
            #print(f"abscisse traitée : {colonne}, flag début de nombre = {flag_debut_de_nombre}")
            if flag_debut_de_nombre==True:
                flag_debut_de_nombre=0
                abscisse_debut = colonne
            if colonne==(tableau.shape[1]-1): #gestion du cas où le dernier caractère traité est un chiffre et que l'on n'aura donc pas l'occasion de passer dans le else
                liste_nombres.append(nombre)
                abscisse_fin = colonne - 1
                range_abscisse_nombre = (abscisse_debut, abscisse_fin)
                # print(f"range abscisse du nombre : {range_abscisse_nombre}")
                range_abscisses.append(range_abscisse_nombre)
        else :
            flag_fin_de_nombre=1
            if nombre!="":
                flag_debut_de_nombre=1
                flag_debut_de_nombre = 1
                liste_nombres.append(nombre)
                abscisse_fin=colonne-1
                range_abscisse_nombre=(abscisse_debut,abscisse_fin)
                #print(f"range abscisse du nombre : {range_abscisse_nombre}")
                range_abscisses.append(range_abscisse_nombre)
    return(liste_nombres,range_abscisses)

def reperage_symbole(range_abscisses,numero_ligne,sum_engine,liste_nombres):
    index=0
    for element in range_abscisses:
        index+=1
        flag_symbole=0
        #print(f"on traite l'ensemble  : {element}")
        for coordonnees in range(element[0],element[1]+1):
                if ((element[0]!=0 and (tableau[numero_ligne][coordonnees - 1].isdigit() == False and tableau[numero_ligne][coordonnees - 1] != "."))
                    #dans ce qui va suivre, element[-1]!= tableau.shape[1]-1 permet de vérifier que l'abscisse la plus élevée n'est pas sur le bord du tableau
                    #de même, numero_ligne!=tableau.shape[0]-1 permet de vérifier que la ligne traitée n'est pas la dernière du tableau
                        # si la valeur à gauche du nombre est un symbole
                        or (element[-1]!=tableau.shape[1]-1 and (tableau[numero_ligne][coordonnees + 1].isdigit() == False and tableau[numero_ligne][coordonnees + 1] != "."))
                        # si la valeur à droite du nombre est un symbole
                        or (numero_ligne!=0 and (tableau[numero_ligne - 1][coordonnees].isdigit() == False and tableau[numero_ligne - 1][coordonnees] != "."))
                        # si la valeur au-dessus du nombre est un symbole
                        or (numero_ligne!=tableau.shape[0]-1 and (tableau[numero_ligne + 1][coordonnees].isdigit() == False and tableau[numero_ligne + 1][coordonnees] != "."))
                        # si la coordonnée au-dessous de la fin du nombre est un symbole
                        or (element[0]!=0 and numero_ligne!=0 and (tableau[numero_ligne - 1][coordonnees - 1].isdigit() == False and tableau[numero_ligne - 1][coordonnees - 1] != "."))
                        # gestion diagonale haut gauche
                        or (element[-1]!=tableau.shape[1]-1 and numero_ligne!=0 and (tableau[numero_ligne - 1][coordonnees + 1].isdigit() == False and tableau[numero_ligne - 1][coordonnees + 1] != "."))
                        # gestion diagonale haut droite
                        or (element[0]!=0  and numero_ligne!=tableau.shape[0]-1 and (tableau[numero_ligne + 1][coordonnees - 1].isdigit() == False and tableau[numero_ligne + 1][coordonnees - 1] != "."))
                        # gestion diagonale bas gauche
                        or (element[-1]!=tableau.shape[1]-1 and numero_ligne!=tableau.shape[0]-1 and (tableau[numero_ligne + 1][coordonnees+ 1].isdigit() == False and tableau[numero_ligne + 1][coordonnees+ 1] != "."))):
                        # gestion diagonale bas droite:
                    #print(f"symbole trouvé autour de la coordonnée {coordonnees}")
                    flag_symbole=1
        if flag_symbole==1:
            #print(f"symbole trouvé autour du nombre {liste_nombres[index - 1]} dans la range d'abscisses {element}")
            sum_engine += int(liste_nombres[index - 1])
        else : print(f"aucun symbole trouvé pour le nombre {int(liste_nombres[index - 1])} ligne {numero_ligne+1} ")
    flag_symbole=0
    return sum_engine

sum_engine=0
for numero_ligne in range(len(lignes)):
    liste_nombres, range_abscisses=reperage_nombre(numero_ligne)
    print(f"liste nombres : {liste_nombres}")
    print(f"range des abscisses : {range_abscisses}")

    sum_engine = reperage_symbole(range_abscisses,numero_ligne,sum_engine, liste_nombres)
    print(f"sum_engine= {sum_engine}")

print(f"la réponse à l'exercice est {sum_engine}")