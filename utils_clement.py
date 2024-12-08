def lecture_fichier(chemin_fichier, mode = "lignes"):
    with open(chemin_fichier, 'r') as fichier:
        if mode == "complet" :
            return fichier.read()
        else : return fichier.read().splitlines()

def chargement_tableau(lignes):
    import numpy as np
    # A partir du fichier lu (et converti sous une forme de listes de ligne), on charge un tableau numpy
    parametre_nombre_colonnes_tableau = len(lignes[0])
    liste_caracteres = []
    for ligne in lignes:
        for caractere in ligne :
            liste_caracteres.append(caractere) #Chaque colonne du futur tableau ne doit contenir qu'un seul caractère

    array=np.asarray(liste_caracteres)

    tableau=array.reshape(int(len(liste_caracteres)/parametre_nombre_colonnes_tableau), parametre_nombre_colonnes_tableau)
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