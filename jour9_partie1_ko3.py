""" Nouvelle idée :
 On parcourt la ligne pour faire un dictionnaire permettant d'associer un identifiant et sa ou ses positions
 sur la ligne "transformée" qu'on ne transforme pas effectivement, pour des questions de performance et
  de brute force). Ce dictionnaire contient les metadonnées de la ligne qu'on voudrait simuler..

 Puis une deuxième fonction qui repère la position du premier "." disponible, et modifie la dernière position de l'identifiant
 Une position qui n'est pas dans le dictionnaire (not in value) est occupée par un point. """

import re
from utils_clement import lecture_fichier, chargement_tableau, reperage_position_caractere


def execution_jour9_partie1(chemin_fichier):
    ligne=lecture_fichier(chemin_fichier) #il n'y a qu'une seule ligne.
    nb_total_identifiants = len(ligne[0])//2
    print(f"nombre total d'identifiants : {nb_total_identifiants}")

    dictionnaire_identifiant_position = alimentation_dictionnaire_identifiant_position(ligne[0])
    print(f"fin de l'initialisation du dictionnaire : {dictionnaire_identifiant_position}" )
    while not condition_fin(dictionnaire_identifiant_position) :
        dictionnaire_identifiant_position = deplacement_identifiants(dictionnaire_identifiant_position)
    print(f"Résultat partie 1 : {calcul_resultat(dictionnaire_identifiant_position)}")




def alimentation_dictionnaire_identifiant_position(ligne) :
    # print(f"ligne traitée : {ligne}")
    dictionnaire_identifiant_position = {}
    position_sur_nouvelle_ligne = 0
    for position_caractere, caractere in enumerate(ligne) :
        # print(f"On traite le caractère {caractere} (position {position_caractere} de la ligne).")
        # print(f"Equivaut à la position : {position_sur_nouvelle_ligne}")
        if position_caractere % 2 == 0: # une fois sur deux, on traite un block file auquel on doit affecter un identifiant
            dictionnaire_identifiant_position[position_caractere//2] = [position_sur_nouvelle_ligne + _ for _ in range(int(caractere)) ]
        position_sur_nouvelle_ligne += int(caractere) # Si on tombe sur 3, alors on occupe 3 espace sur la ligne transformée

    return dictionnaire_identifiant_position

def deplacement_identifiants(dictionnaire_identifiant_position) :
    # On repère la position de l'identifiant qui est le "plus à droite" sur la nouvelle ligne transformée,
    # c'est à dire celui qui a la position associée la plus haute dans le dictionnaire
    position_identifiant_a_deplacer = recherche_position_dernier_identifiant(dictionnaire_identifiant_position)
    for cle in dictionnaire_identifiant_position.keys() : #rappel : la valeur associée à l'identifiant est une liste d'au moins une position.
        if position_identifiant_a_deplacer in dictionnaire_identifiant_position[cle] :
            identifiant_a_deplacer = cle
    # print(f"identifiant à déplacer : {identifiant_a_deplacer} , position : {position_identifiant_a_deplacer}")

    # On repère la position du premier point, et on met à jour le dictionnaire en disant que la nouvelle position
    # de l'identifiant à déplacer vaut désormais la position du point.
    position_premier_point = recherche_position_premier_point(dictionnaire_identifiant_position)
    # print(f"position du premier point : {position_premier_point}")
    dictionnaire_identifiant_position[identifiant_a_deplacer].append(position_premier_point)
    dictionnaire_identifiant_position[identifiant_a_deplacer].remove(position_identifiant_a_deplacer)

    return dictionnaire_identifiant_position


def recherche_position_premier_point(dic) :

    # La position du premier point est la première valeur qui n'apparait pas dans le dictionnaire
    # (c'est à dire qui n'est pas occupée par un indice)

    position_premier_point = 0 # C'est pour initialiser, on sait que cette position est forcément occupée par l'identifiant 0
    while any(position_premier_point in liste for liste in dic.values()):
        #Si on trouve cette position dans l'une des listes (valeurs du dictionnaire), c'est que la position est déjà
        # occupée par un identifiant, donc pas par un point. Donc on teste le point suivant.
        position_premier_point += 1
    return position_premier_point

def recherche_position_dernier_identifiant(dic) :
    max = 0
    for valeur in dic.values():
        for _ in range(len(valeur)):
            if valeur[_] > max:
                max = valeur[_]
    return max

def condition_fin(dic) :
    # Tant que la condition n'est pas remplie et qu'il existe au moins un "." à gauche du dernier chiffre, on continue.
    return recherche_position_premier_point(dic) > recherche_position_dernier_identifiant(dic)


def calcul_resultat(dic):
    return sum(identifiant * position for identifiant, positions in dic.items() for position in positions)
