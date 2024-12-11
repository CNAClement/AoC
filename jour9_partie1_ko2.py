""" KO car une fois que j'ai déplacé un identifiant > 1 chiffre (par exemple 10) , je n'ai plus aucun moyen
de savoir si c'est 1 suivi de 0 (donc deux multiplications à faire) ou 10 (une seule multiplication).
 """

import re
from utils_clement import lecture_fichier, chargement_tableau, reperage_position_caractere


def execution_jour9_partie1(chemin_fichier):
    ligne=lecture_fichier(chemin_fichier) #il n'y a qu'une seule ligne.
    nb_total_indices = len(ligne[0])//2
    print(f"nombre total d'indices : {nb_total_indices}")

    dictionnaire_indice_occurrence , nouvelle_ligne = transformation_ligne(ligne[0])
    print("fin de la transformation")
    partie_stable = ""
    partie_a_traiter = nouvelle_ligne

    while not condition_fin(partie_a_traiter) :
        identifiant, nombre_occurrences_identifiant = dictionnaire_identifiant_occurrence.popitem()  # On récupère le dernier identifiant écrit et le nombre de fois où il apparait (rappel : une fois par block file).
        for _ in nombre_occurrences_identifiant :
            partie_stable_iteration , partie_a_traiter = traitement_espaces_vides(partie_a_traiter , identifiant)
            partie_stable += partie_stable_iteration

    nouvelle_ligne = partie_stable + partie_a_traiter
    print(calcul_resultat(nouvelle_ligne))



def transformation_ligne(ligne) :
    # Lire l'énoncé https://adventofcode.com/2024/day/9 , je ne l'expliquerai pas mieux. Pour une ligne donnée
    # composée successivement de blocks de fichiers et de blocks vides, on applique une transformation en mettant des "." pour les blocks vides et
    # un id fichier pour les blocks fichiers.
    nouvelle_ligne = ""
    print(f"ligne avant transformation : {ligne}")
    dictionnaire_indice_occurrence = {}  # Ce dictionnaire permet de noter combien de fois chaque indice apparait (donc dictionnaire[indice] = nb_block_files )
    for indice, nombre_blocks_fichier in enumerate(ligne):
        for _ in range(int(nombre_blocks_fichier)):
            # On récupère le chiffre dans l'input et on ajoute dans "nouvelle_ligne" autant de caractères que le chiffre trouvé.
            if indice % 2 == 0:
                # Une fois sur deux, on rajoute "indice / 2" (car dans l'exo, on ne doit incrémenter
                # l'id block qu'une fois sur deux. Par exemple pour l'indice 10 et le chiffre "4" ,
                # on ajoute "5555" à nouvelle_ligne (on a 4 blocks dont on rajoute 4 "5' ).
                nouvelle_ligne += str(indice // 2)
                dictionnaire_indice_occurrence[indice//2] = nombre_blocks_fichier
            else:
                # L'autre fois sur deux, on rajoute des "." , par exemple, si on lit le chiffre "4",
                # On ajoute  "...." à nouvelle_ligne.
                nouvelle_ligne += "."

            if len(str(indice // 2)) != len(str((indice+1) // 2)) : # On veut gérer le cas où on change de puissance de 10 (passage de 9 à 10, 99 , 100 ) ...
                nouvelle_ligne += '|'

    print(f"ligne transformée : {nouvelle_ligne}")
    print(f"Dictionnaire association indice et nombre d'occurrences de l'indice : {dictionnaire_indice_occurrence}")
    return dictionnaire_indice_occurrence , nouvelle_ligne

def condition_fin(ligne) :
    # Tant que la condition n'est pas remplie et qu'il existe au moins un "." à gauche du dernier chiffre, on continue.
    position_premier_point = ligne.find(".")
    position_dernier_chiffre =  max((i for i, caractere in enumerate(ligne) if caractere.isdigit()), default=-1)
    return position_premier_point > position_dernier_chiffre


def traitement_espaces_vides(ligne , identifiant) :
    print(f"On traite la ligne {ligne} pour déplacer l'indeitifiant {identifiant}")

    longueur_identifiant = len(identifiant)
    # On récupère le dernier block de fichiers (qui peut être sur plusieurs chiffres pour les indices > 9 )
    # et on le déplace à gauche sur le premier block vide (".") disponible.
    derniere_position_identifiant = ligne.rfind(identifiant)  # Recherche de la première occurrence de l'identifiant, en partant de la fin (en parcourant la ligne en sens inverse).
    # La position renvoyée est bien celle de l'identifiant dans la chaine lue "dans le bon sens".
    premiere_position_point = ligne.find(".")
    if premiere_position_point < derniere_position_identifiant :
        ligne = ligne[:derniere_position_identifiant] + "." + ligne[derniere_position_identifiant+longueur_identifiant:]
        # On remplace l'identifiant par un seul point, par exemple pour l'identifiant 99 dans "12.2.99" ==> "12.2.." .
        ligne = ligne[:premiere_position_point] + str(identifiant) + ligne[premiere_position_point + 1 :]  # On remplace le point par l'identifiant, par exemple : 12.2.. ==> 12992..

    if indice_envers >= 0:  # On a trouvé un caractère autre que "." , on le stocke et on le remplace par un "."
        chiffre_trouve = ligne[indice_envers]
        ligne = ligne[:indice_envers] + "." + ligne[indice_envers+1:]
        indice_endroit = 0
        while indice_endroit < len(ligne) and ligne[indice_endroit] != "." :
            indice_endroit += 1
        if indice_endroit < len(ligne) : # On a trouvé un "." , on le remplace par le chiffre trouvé précédemment
            partie_stable = ligne[:indice_endroit] # Cette partie de la ligne ne bougera plus, on ne la traite plus.
            partie_a_traiter = chiffre_trouve+ligne[indice_endroit+1:]
    else:
        print("Tous les caractères sont '.'")
    return partie_stable , partie_a_traiter

def calcul_resultat(ligne):
    print(f"ligne : {ligne}")
    ligne_sans_point = ligne.replace(".","")
    morceaux_de_ligne = ligne_sans_point.split('|') # On sépare les lignes chaque fois que l'indice change de puissance de 10
    checksum = 0

    for num_morceau , morceau in enumerate(morceaux_de_ligne) : #Sur le premier morceau, les indices sont entre 0 et 9, sur le 2eme : entre 10 et 99, etc.
        print(f"morceau : {morceau}")
        checksum_morceau = 0
        longueur_indice = num_morceau + 1 # Sur le 0eme morceau, on est sur des indices entre 0 et 9 , puis 10 et 99 pour le morceau "1", etc.
        for position, chiffre in enumerate(morceau) :
            if position % longueur_indice == 0 :
                position_reelle = 10**(longueur_indice-1) + position//longueur_indice if longueur_indice > 1 else position # Le cas 10^0 = 1 esst chiant ...
                # Si on est sur le "3eme" morceau (num_morceau = 2), on est sur des indices entre 100 et 999 (longueur 3).
                # Donc les positions 0 à 2 du morceau correspondent à la position réelle 100, puis 3 à 5 à la position 101, etc.
                checksum_morceau += position_reelle * int(morceau[position : position +longueur_indice])
                #par exemple, sur le morceau "100101102103" qui représente les indices de longueur 3,
                # le premier chiffre (obtenu pour "position" = 0) sera : morceau[0:3]
                # le deuxième chiffre (obtenu pour position = 1 ) sera  : morceau[3:6] = 101
        checksum += checksum_morceau
    return checksum
