import numpy as np

def execution_jour4_partie1(chemin_fichier):
    lignes = lecture_fichier(chemin_fichier)
    parametre_nombre_colonnes_tableau=len(lignes[0])
    print(f"le tableau devrait avoir {len(lignes)} lignes et {parametre_nombre_colonnes_tableau} colonnes.")
    liste_caracteres = []
    for ligne in lignes:
        for caractere in ligne :
            liste_caracteres.append(caractere)

    array=np.asarray(liste_caracteres)

    tableau=array.reshape(int(len(liste_caracteres)/parametre_nombre_colonnes_tableau), parametre_nombre_colonnes_tableau)
    liste_coordonnees_x=reperage_x(tableau)
    nombre_xmas_trouves=recherche_mot(tableau, liste_coordonnees_x)
    print(f"On a trouvé : {nombre_xmas_trouves} xmas.")






def lecture_fichier(chemin_fichier):
    with open(chemin_fichier, 'r') as fichier:
        contenu = fichier.read()
        lignes = contenu.splitlines()
        return lignes

def reperage_x(tableau):
    # Cette fonction permet de parcourir les données du tableau jusqu'à trouver un X et noter ses coordonnées.
    # Ce X constituera le point de départ de nos recherches de mot "XMAS".
    liste_coordonnees_x = []
    for num_ligne in range(tableau.shape[0]):
        for num_colonne in range(tableau.shape[1]):
            if tableau[num_ligne][num_colonne]=='X':
                liste_coordonnees_x.append((num_colonne, num_ligne))
    return liste_coordonnees_x

def recherche_mot(tableau, liste_coordonnees_x):
    nombre_xmas_trouves = 0
    # A partir de chacun des x trouvés, on fait quelques tests de bordure puis on appelle une fonction qui
    # cherche le mot 'XMAS' dans la direction souhaitée.
    for coordonnee in liste_coordonnees_x :
        # recherche vers la droite :
        deplacable_droite = coordonnee[0]<tableau.shape[1]-3 #On vérifie qu'il y a suffisamment d'espace pour M + A +S jusqu'à la fin du tableau.
        # Pour un tableau de longueur 10, il faut que l'abscisse du S soit au plus 9 (version Python), donc au plus 6 pour le X
        deplacable_gauche = coordonnee[0]>2  # On vérifie que le "X" est au moins sur la 4eme colonne (3eme indice en notation Python) pour qu'il y ait la place d'écrire 'SAMX' vers la gauche.
        deplacable_bas = coordonnee[1]<tableau.shape[0]-3  # Suffisamment d'espace pour M + A + S jusqu'à la fin du tableau (vers le bas).
        deplacable_haut = coordonnee[1]>2  # On vérifie que le "X" est au moins sur la 4eme ligne (3eme indice en notation Python) pour qu'il y ait la place d'écrire 'SAMX' vers la gauche.

        if deplacable_droite :
            nombre_xmas_trouves += recherche_xmas(tableau, coordonnee, ["droite"])  # Cette fonction renvoie 1 si on a trouvé un 'XMAS' et 0 sinon.
        if deplacable_gauche :
            nombre_xmas_trouves += recherche_xmas(tableau, coordonnee, ["gauche"])  # Cette fonction renvoie 1 si on a trouvé un 'XMAS' et 0 sinon.
        if deplacable_bas :
            nombre_xmas_trouves += recherche_xmas(tableau, coordonnee, ["bas"])  # Cette fonction renvoie 1 si on a trouvé un 'XMAS' et 0 sinon.
        if deplacable_haut :
            nombre_xmas_trouves += recherche_xmas(tableau, coordonnee, ["haut"]) # Cette fonction renvoie 1 si on a trouvé un 'XMAS' et 0 sinon.
        if deplacable_gauche and deplacable_haut :
            nombre_xmas_trouves += recherche_xmas(tableau, coordonnee, ["haut" , 'gauche'])
        if deplacable_gauche and deplacable_bas :
            nombre_xmas_trouves += recherche_xmas(tableau, coordonnee, ["bas", 'gauche'])
        if deplacable_droite and deplacable_haut :
            nombre_xmas_trouves += recherche_xmas(tableau, coordonnee, ["haut", 'droite'])
        if deplacable_droite and deplacable_bas :
            nombre_xmas_trouves += recherche_xmas(tableau, coordonnee, ["bas" , 'droite'])

    return nombre_xmas_trouves


def recherche_xmas(tableau, coordonnee_depart, sens):
    deplacement = (0,0)
    if "droite" in sens :
        deplacement = somme_coordonnees(deplacement,(1,0),1)
    if "gauche" in sens :
        deplacement = somme_coordonnees(deplacement,(-1,0),1)
    if "haut" in sens :
        deplacement = somme_coordonnees(deplacement,(0,-1),1)
    if "bas" in sens :
        deplacement = somme_coordonnees(deplacement,(0,1),1)

    # print(f"coordonnees départ : {coordonnee_depart}, déplacement : {deplacement}")

    # print(tableau_coordonnees(tableau , somme_coordonnees(coordonnee_depart, deplacement, 1)))
    # print(tableau_coordonnees(tableau , somme_coordonnees(coordonnee_depart, deplacement, 2)))
    # print(tableau_coordonnees(tableau , somme_coordonnees(coordonnee_depart, deplacement, 3)))
    if (tableau_coordonnees(tableau , somme_coordonnees(coordonnee_depart , deplacement, 1 )) =="M"
            and tableau_coordonnees(tableau , somme_coordonnees(coordonnee_depart , deplacement, 2 ))  =="A"
            and tableau_coordonnees(tableau , somme_coordonnees(coordonnee_depart , deplacement, 3 ))  =="S") :
        print(f"On a trouvé un XMAS dans le sens {deplacement} qui commence aux coordonnées {coordonnee_depart}")
        return 1
    else :
        return 0

def somme_coordonnees(coordonnees_depart, deplacement, nombre_deplacement):
    # A partir des coordonnées de départ (exemple : (2,3) ), du déplacement (exemple : (1,0) ) et du nombre
    # de déplacements (exemple : 3), calcule les coordonnées d'arrivée (exemple : (5,3) ) puis
    # renvoie la valeur correspondante dans le tableau.
    # Rappel : (x,y) avec x = abscisse = n° colonne du tableau  et y = ordonnée = n° ligne du tableau.
    nouvelles_coordonnees = coordonnees_depart[0]+ nombre_deplacement*deplacement[0], coordonnees_depart[1]+ nombre_deplacement*deplacement[1]

    return nouvelles_coordonnees

def tableau_coordonnees(tableau, coordonnees):
    return tableau[coordonnees[1],coordonnees[0]]