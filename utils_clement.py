def lecture_fichier(chemin_fichier, mode = "lignes"):
    with open(chemin_fichier, 'r') as fichier:
        if mode == "complet" :
            return fichier.read()
        else :
            return fichier.read().splitlines()

def chargement_tableau(lignes):
    import numpy as np
    # A partir du fichier lu (et converti sous une forme de listes de ligne), on charge un tableau numpy
    parametre_nombre_colonnes_tableau = len(lignes[0])
    liste_caracteres = []
    for ligne in lignes:
        for caractere in ligne :
            liste_caracteres.append(caractere) #Chaque colonne du futur tableau ne doit contenir qu'un seul caractère

    array_prep =np.asarray(liste_caracteres)

    tableau=array_prep.reshape(int(len(liste_caracteres)/parametre_nombre_colonnes_tableau), parametre_nombre_colonnes_tableau)
    return tableau

def reperage_position_caractere(tableau , caractere_cherche):
    # Cette fonction permet de parcourir les données du tableau jusqu'à trouver le caractère cherché
    # et noter ses coordonnées.
    liste_coordonnees = []
    for num_ligne in range(tableau.shape[0]):
        for num_colonne in range(tableau.shape[1]):
            if tableau[num_ligne][num_colonne]==caractere_cherche:
                liste_coordonnees.append((num_colonne, num_ligne))
    return liste_coordonnees


def tableau_coordonnees(tableau, coordonnees):
    return tableau[coordonnees[1]][coordonnees[0]]

def maj_tableau(tableau, coordonnees , caractere) :
    tableau[coordonnees[1]][coordonnees[0]] = caractere
    # Pour mémoire : il y a une subtilité qui fait que ça ne marche pas d'utiliser l'autre fonction "tableau_coordonnees"
    # pour faire : tableau_coordonnees(tableau, coordonnees) = 'caractere'
    # L'idée c'est que tableau_coordonnees(tableau, coordonnees) ne fait que renvoyer une valeur. Ca dit juste "la valeur de ce tableau à cet endroit est 4"
    return tableau

def maj_coordonnees(coordonnees_depart, deplacement):
    return(coordonnees_depart[0]+deplacement[0],coordonnees_depart[1]+deplacement[1])

def recherche_valeurs(tableau , valeur_cherchee):
    import numpy as np
    """np.where renvoie deux tableaux numpy, un qui donne la position des indices sur l'axe horizontal et un qui
     donne la position des indices sur l'axe vertical."""

    #Pour des tableaux très grands, on peut utiliser np.column_stack pour éviter la transposition implicite avec zip :
    #return np.column_stack(np.where(tableau == valeur_cherchee)).tolist()

    return [(int(i), int(j)) for i, j in zip(*np.where(tableau == valeur_cherchee))]
