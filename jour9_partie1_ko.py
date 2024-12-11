import numpy as np
from itertools import combinations
from utils_clement import lecture_fichier, chargement_tableau, reperage_position_caractere


def execution_jour9_partie1(chemin_fichier):
    ligne=lecture_fichier(chemin_fichier) #il n'y a qu'une seule ligne.
    nouvelle_ligne = transformation_ligne(ligne[0])
    print("fin de la transformation")
    partie_stable = ""
    partie_a_traiter = nouvelle_ligne
    while not condition_fin(partie_a_traiter) :
        partie_stable_iteration , partie_a_traiter = traitement_espaces_vides(partie_a_traiter)
        partie_stable += partie_stable_iteration

    nouvelle_ligne = partie_stable + partie_a_traiter
    print(calcul_resultat(nouvelle_ligne))



def transformation_ligne(ligne) :
    # Lire l'énoncé https://adventofcode.com/2024/day/9 , je ne l'expliquerai pas mieux. Pour une ligne donnée
    # composée successivement de blocks de fichiers et de blocks vides, on applique une transformation en mettant des "." pour les blocks vides et
    # un id fichier pour les blocks fichiers.
    nouvelle_ligne = ""
    for indice, chiffre in enumerate(ligne):
        for nombre_blocks_fichier in range(int(chiffre)):
            # On récupère le chiffre dans l'input et on ajoute dans "nouvelle_ligne" autant de caractères que le chiffre trouvé.
            if indice % 2 == 0:
                # Une fois sur deux, on rajoute "indice / 2" (car dans l'exo, on ne doit incrémenter
                # l'id block qu'une fois sur deux. Par exemple pour l'indice 10 et le chiffre "4" ,
                # on ajoute "5555" à nouvelle_ligne (on a 4 blocks dont on rajoute 4 "5' ).
                nouvelle_ligne += str(indice // 2)
            else:
                # L'autre fois sur deux, on rajoute des "." , par exemple, si on lit le chiffre "4",
                # On ajoute  "...." à nouvelle_ligne.
                nouvelle_ligne += "."

    return nouvelle_ligne

def condition_fin(ligne) :
    # Tant que la condition n'est pas remplie et qu'il existe au moins un "." à gauche du dernier chiffre, on continue.
    position_premier_point = ligne.find(".")
    position_dernier_chiffre =  max((i for i, caractere in enumerate(ligne) if caractere.isdigit()), default=-1)
    return position_premier_point > position_dernier_chiffre


def traitement_espaces_vides(ligne) :
    # print(f"On traite la ligne {ligne}")
    # On récupère le dernier block de fichiers et on le déplace à gauche sur le premier block vide (".") disponible.
    indice_envers = len(ligne) - 1 #on part de la fin
    while indice_envers >= 0 and ligne[indice_envers] == "." :
        indice_envers -= 1

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
    ligne_sans_point = ligne.replace(".","")
    checksum = 0
    for position, chiffre in enumerate(ligne_sans_point) :
        checksum += position * int(chiffre)
    return checksum

