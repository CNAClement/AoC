import numpy as np

def execution_jour4_partie2(chemin_fichier):
    lignes = lecture_fichier(chemin_fichier)
    parametre_nombre_colonnes_tableau=len(lignes[0])
    print(f"le tableau devrait avoir {len(lignes)} lignes et {parametre_nombre_colonnes_tableau} colonnes.")
    liste_caracteres = []
    for ligne in lignes:
        for caractere in ligne :
            liste_caracteres.append(caractere)

    array=np.asarray(liste_caracteres)

    tableau=array.reshape(int(len(liste_caracteres)/parametre_nombre_colonnes_tableau), parametre_nombre_colonnes_tableau)
    liste_coordonnees_a=reperage_a(tableau)
    nombre_mas_croix_trouves=recherche_mot(tableau, liste_coordonnees_a)
    print(f"On a trouvé : {nombre_mas_croix_trouves} X-MAS.")






def lecture_fichier(chemin_fichier):
    with open(chemin_fichier, 'r') as fichier:
        contenu = fichier.read()
        lignes = contenu.splitlines()
        return lignes

def reperage_a(tableau):
    # Cette fonction permet de parcourir les données du tableau jusqu'à trouver un A et noter ses coordonnées.
    # Ce A constituera le point de départ de nos recherches de mot "MAS" en double-diagonale.
    liste_coordonnees_a = []
    for num_ligne in range(tableau.shape[0]):
        for num_colonne in range(tableau.shape[1]):
            if tableau[num_ligne][num_colonne]=='A':
                liste_coordonnees_a.append((num_colonne, num_ligne))
    return liste_coordonnees_a

def recherche_mot(tableau, liste_coordonnees_a):
    nombre_mas_trouves = 0
    # A partir de chacun des A trouvés, on fait quelques tests de bordure puis on appelle une fonction qui
    # cherche le mot 'MAS' dans les diagonales.
    for coordonnee in liste_coordonnees_a :
        deplacable_droite = coordonnee[0]<tableau.shape[1]-1 #On vérifie qu'il y a suffisamment d'espace sur la droite.
        deplacable_gauche = coordonnee[0]>0
        deplacable_bas = coordonnee[1]<tableau.shape[0]-1  # Suffisamment d'espace vers le bas.
        deplacable_haut = coordonnee[1]>0  # On vérifie que le "X" est au moins sur la 4eme ligne (3eme indice en notation Python) pour qu'il y ait la place d'écrire 'SAMX' vers la gauche.

        if deplacable_gauche and deplacable_haut and deplacable_droite and deplacable_bas :
            nombre_mas_trouves += recherche_mas(tableau, coordonnee)

    return nombre_mas_trouves


def recherche_mas(tableau, coordonnee_depart):

    # Diagonale d'en haut à gauche jusqu'en bas à droite avec "MAS" :
    diagonale_sens1_possibilite1 = (tableau_coordonnees(tableau , somme_coordonnees(coordonnee_depart , "haut-gauche")) =="M"
            and tableau_coordonnees(tableau , somme_coordonnees(coordonnee_depart , "bas-droite")) =="S")

    # Diagonale d'en haut à gauche jusqu'en bas à droite avec "SAM" :
    diagonale_sens1_possibilite2 = (
                tableau_coordonnees(tableau, somme_coordonnees(coordonnee_depart, "haut-gauche")) == "S"
                and tableau_coordonnees(tableau, somme_coordonnees(coordonnee_depart, "bas-droite")) == "M")

    # Diagonale d'en bas à gauche jusqu'en haut à droite avec "MAS" :
    diagonale_sens2_possibilite1 = (tableau_coordonnees(tableau , somme_coordonnees(coordonnee_depart , "bas-gauche")) =="M"
            and tableau_coordonnees(tableau , somme_coordonnees(coordonnee_depart , "haut-droite")) =="S")

    # Diagonale d'en bas à gauche jusqu'en haut à droite avec "MAS" :
    diagonale_sens2_possibilite2 = (tableau_coordonnees(tableau , somme_coordonnees(coordonnee_depart , "bas-gauche")) =="S"
            and tableau_coordonnees(tableau , somme_coordonnees(coordonnee_depart , "haut-droite")) =="M")

    if (diagonale_sens1_possibilite1 or diagonale_sens1_possibilite2 )  \
        and (diagonale_sens2_possibilite1 or diagonale_sens2_possibilite2) :
        return 1
    else :
        return 0

def somme_coordonnees(coordonnees_depart, sens ):
    dic_coordonnees_sens =  {"haut-gauche" : (-1,-1) , "haut-droite" : (1,-1) , "bas-gauche" : (-1,1) , "bas-droite" : (1,1)}
    # Rappel : (x,y) avec x = abscisse = n° colonne du tableau  et y = ordonnée = n° ligne du tableau.
    nouvelles_coordonnees = coordonnees_depart[0]+ dic_coordonnees_sens[sens][0], coordonnees_depart[1]+ dic_coordonnees_sens[sens][1]

    return nouvelles_coordonnees

def tableau_coordonnees(tableau, coordonnees):
    return tableau[coordonnees[1],coordonnees[0]]