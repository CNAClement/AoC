""" Nouvelle idée :
La même chose que l'idée précédente (décrite dans jour9_partie1_ko3.py mais en changeant l'ordre clé-valeur
du dictionnaire, plutôt que de faire dic = {identifiant, position} on va faire dic = {position, identifiant}
ce qui permettra peut-être de réduire l'aspect brute force en récupérant plus facilement les infos"""
import re
from utils_clement import lecture_fichier, chargement_tableau, reperage_position_caractere


def execution_jour9_partie1(chemin_fichier):
    ligne=lecture_fichier(chemin_fichier) #il n'y a qu'une seule ligne.
    nb_total_identifiants = len(ligne[0])//2
    print(f"nombre total d'identifiants : {nb_total_identifiants}")

    dictionnaire_identifiant_position = alimentation_dictionnaire_identifiant_position(ligne[0])
    print(f"fin de l'initialisation du dictionnaire : {dictionnaire_identifiant_position}" )
    partie_stable_complete = {}
    partie_a_traiter =  dictionnaire_identifiant_position
    #while not condition_fin(partie_a_traiter) :
    while len(partie_a_traiter) > 1 :
        dictionnaire_identifiant_position = deplacement_identifiants(partie_a_traiter)
        partie_stable, partie_a_traiter = separation_dictionnaires(dictionnaire_identifiant_position)
        partie_stable_complete = partie_stable_complete | partie_stable  # On concatène
    dictionnaire_identifiant_position = partie_stable_complete | partie_a_traiter
    print(f"Résultat partie 1 : {calcul_resultat(dictionnaire_identifiant_position)}")



def alimentation_dictionnaire_identifiant_position(ligne) :
    # print(f"ligne traitée : {ligne}")
    dictionnaire_identifiant_position = {}
    position_sur_nouvelle_ligne = 0
    for position_caractere, caractere in enumerate(ligne) :
        # print(f"On traite le caractère {caractere} (position {position_caractere} de la ligne).")
        # print(f"Equivaut à la position : {position_sur_nouvelle_ligne}")
        if position_caractere % 2 == 0: # une fois sur deux, on traite un block file auquel on doit affecter un identifiant
            for _ in range(int(caractere)) :
                dictionnaire_identifiant_position[position_sur_nouvelle_ligne + _] = position_caractere//2 #position_caractere//2 corresppond à l'identifiant, qu'on incrémente une fois sur deux.
        position_sur_nouvelle_ligne += int(caractere) # Si on tombe sur 3, alors on occupe 3 espace sur la ligne transformée

    return dictionnaire_identifiant_position

def deplacement_identifiants(dictionnaire_identifiant_position) :
    # On cherche la position de l'identifiant qui est le "plus à droite" sur la nouvelle ligne transformée,
    # c'est à dire celui qui a la position associée la plus haute dans le dictionnaire. C'est la plus
    # grande clé du dictionnaire.
    position_identifiant_a_deplacer = recherche_position_dernier_identifiant(dictionnaire_identifiant_position)
    identifiant_a_deplacer = dictionnaire_identifiant_position[position_identifiant_a_deplacer]

    # On repère la position du premier point, et on met à jour le dictionnaire en disant que la nouvelle position
    # de l'identifiant à déplacer vaut désormais la position du point et inversement.
    # Concrètement, cela revient à supprimer la position (= la clé) du dictionnaire, puisqu'une
    # position qui n'est pas dans le dictionnaire est occupée par un point, et rajouter la position
    # du point avec l'identifiant qui lui est désormais associé.
    position_premier_point = recherche_position_premier_point(dictionnaire_identifiant_position)
    # print(f"première position disponible : {position_premier_point}")
    # print(f"identifiant à déplacer : {identifiant_a_deplacer}, position {position_identifiant_a_deplacer}")
    # print(f"position du premier point : {position_premier_point}")
    dictionnaire_identifiant_position[position_premier_point] = identifiant_a_deplacer
    del dictionnaire_identifiant_position[position_identifiant_a_deplacer]
    return dictionnaire_identifiant_position

def separation_dictionnaires(dictionnaire_identifiant_position) :
    # Séparation en deux parties "stable" et "à traiter". La partie stable est l'ensemble des positions avant le premier
    # point, qui ne seront donc plus concernées par les itérations futures, cela évite donc d'itérer pour rien.
    position_premier_point = recherche_position_premier_point(dictionnaire_identifiant_position)
    partie_stable = {position: identifiant for position, identifiant in dictionnaire_identifiant_position.items() if position < position_premier_point - 1 }
    # le -1 permet de garder la première clé (pourtant stable) dans le dictionnaire à traiter, ce qui sera utile pour calculer la position du premier point, qui se base sur min(dic.keys() )
    partie_a_traiter = {position: identifiant for position, identifiant in dictionnaire_identifiant_position.items() if position >= position_premier_point - 1}
    # print(f"partie stable : {partie_stable}")
    # print(f"partie à traiter : {partie_a_traiter}")

    return partie_stable, partie_a_traiter





def recherche_position_premier_point(dic) :

    # La position du premier point est la première clé qui n'apparait pas dans le dictionnaire
    # (c'est à dire qui n'est pas occupée par un indice)

    position_premier_point = min(dic.keys()) # C'est pour initialiser, on sait que cette position est forcément occupée par l'identifiant 0
    while position_premier_point in [position for position in dic.keys()]:
        #Si on trouve cette position dans l'une clé, c'est que la position est déjà occupée par un
        # identifiant, donc pas par un point. Donc on teste le point suivant.
        position_premier_point += 1
    return position_premier_point

def recherche_position_dernier_identifiant(dic) :
    return max(dic.keys())

def calcul_resultat(dic):
    return sum(identifiant * position for identifiant, position in dic.items() )
