import re
from utils_clement import lecture_fichier, chargement_tableau, reperage_position_caractere


def execution_jour9_partie1(chemin_fichier):
    ligne=lecture_fichier(chemin_fichier) #il n'y a qu'une seule ligne.
    nb_total_identifiants = len(ligne[0])//2
    print(f"nombre total d'identifiants : {nb_total_identifiants}")

    dictionnaire_identifiant = alimentation_dictionnaire_identifiant(ligne[0])
    print(f"fin de l'initialisation du dictionnaire : {dictionnaire_identifiant}" )
    partie_stable_complete = {}
    partie_a_traiter =  dictionnaire_identifiant
    point_depart = 0
    while len(partie_a_traiter) > 1 :
        identifiant_a_deplacer = recherche_identifiant_a_deplacer(dictionnaire_identifiant)
        point_depart, dictionnaire_identifiant = deplacement_identifiants(point_depart, partie_a_traiter)
        partie_stable = {identifiant : dictionnaire_identifiant[identifiant] for identifiant in dictionnaire_identifiant if dictionnaire_identifiant[identifiant][2] == 1}
        partie_a_traiter = {identifiant : dictionnaire_identifiant[identifiant] for identifiant in dictionnaire_identifiant if dictionnaire_identifiant[identifiant][2] == 0}

        partie_stable_complete = partie_stable_complete | partie_stable  # On concatène
    dictionnaire_identifiant_position = partie_stable_complete | partie_a_traiter
    print(f"Résultat partie 1 : {calcul_resultat(dictionnaire_identifiant_position)}")



def alimentation_dictionnaire_identifiant(ligne) :
    """    # Clé : identifiant
        # Valeurs :
        # - sa position de départ
        # - la longueur de sa position
        # - flag traité ou non (un identifiant n'est traité qu'une seule fois, donc après le premier traitement, on peut le mettre de côté).
    """
    dictionnaire_identifiant = {}
    position_sur_nouvelle_ligne = 0
    for position_caractere, caractere in enumerate(ligne) :
        # print(f"On traite le caractère {caractere} (position {position_caractere} de la ligne).")
        # print(f"Equivaut à la position : {position_sur_nouvelle_ligne}")
        if position_caractere % 2 == 0: # une fois sur deux, on traite un block file auquel on doit affecter un identifiant
            dictionnaire_identifiant[position_caractere // 2]= (position_sur_nouvelle_ligne , int(caractere) , 0)
        position_sur_nouvelle_ligne += int(caractere) # Si on tombe sur 3, alors on occupe 3 espace sur la ligne transformée

    return dictionnaire_identifiant

def recherche_identifiant_a_deplacer(dictionnaire_identifiant) :
    """  Cette fonction récupère l'identifiant dont la position est la plus grande (max(dic.values()[0])
     ainsi que la longueur nécessaire pour le déplacer (dic.values[0] )"""
    """derniere_position = 0
    for valeur in dictionnaire_identifiant.values():
        for _ in range(len(valeur)):
            if valeur[_] > derniere_position:
                derniere_position = valeur[_]

    identifiant_a_deplacer = 0
    while dictionnaire_identifiant[identifiant_a_deplacer][0] != derniere_position :
        identifiant_a_deplacer +=1
        # le while permet de s'arrêter sans parcourir l'ensemble du dictionnaire, puisqu'on sait que
        # chaque position n'est associée qu'à un et un seul identifiant, donc une fois trouvé, pas besoin de faire le reste."""

    # version alternative proposée par ChatGPT :
    # Fonctionnement de la fonction max : premier paramètre : la liste dont il doit renvoyer le max, deuxième
    # paramètre : la "clé de lecture" . Par défaut il renvoie le max tout court, mais on peut mettre key= lambda k:len(k)
    # pour renvoyer la plus grande longueur, ou encore (comme ici) lambda k : dic(k)
    identifiant_a_deplacer = max(dictionnaire_identifiant, key=lambda k: dictionnaire_identifiant[k][0])

    return identifiant_a_deplacer


def recherche_espace_libre(dictionnaire_identifiant, identifiant_a_deplacer) :
    """ Cette fonction récupère l'identifiant à déplacer et recherche un nombre suffisant d'espaces libres
    (c'est-à-dire des positions consécutives qui n'apparaissent pas dans le dictionnaire (not in values[1] )
    deux conditions : position < position_depart et longueur_necessaire atteinte.

    A partir de l'identifiant à déplacer, on accède facilement à sa position et à sa longueur.'"""

    print(f"Pour l'identifiant {identifiant_a_deplacer}, en position {dictionnaire_identifiant[identifiant_a_deplacer][0]}, "
          f"on a besoin d'une longueur de {dictionnaire_identifiant[identifiant_a_deplacer][1]}")

    # Rappel : la position dictionnaire_identifiant[identifiant_a_deplacer][0] est la plus grande position actuellement occupée par un identifiant.

def deplacement_identifiants(dictionnaire_identifiant) :
    # maj de à traiter : dictionnaire_identifiant[identifiant][2] == 1
    return point_depart, dictionnaire_identifiant

def recherche_position_premier_point(point_depart, dic) :

    # La position du premier point est la première clé qui n'apparait pas dans le dictionnaire
    # (c'est à dire qui n'est pas occupée par un indice)

    dic_trie = dict(sorted(dic.items(), key=lambda item: item[1][0]))
    # items renvoie la paire clé, valeur donc item[1] renvoie valeur donc item[1][0] renvoie le premier
    # élément du tuple valeur, c'est à dire la position. On obtient un dictionnaire trié sur la position.

    liste_triee = list(dic_trie) # on le convertit en liste pour pouvoir itérer dessus
    for num_element in range(point_depart, len(liste_triee) - 1 ) :
        tuple_valeurs = liste_triee[num_element][1]
        tuple_valeurs_suivant = liste_triee[num_element + 1 ][1]
        if tuple_valeurs[0] + tuple_valeurs[1] == tuple_valeurs_suivant[0]:
            print(f"Pas d'espace entre les éléments")
        else :
            position_premier_point = tuple_valeurs[0] + tuple_valeurs[1]

    # Tant que la valeur du point est comprise entre le début de la position et la fin de la position (donc début + longueur).

        #Si on trouve cette position dans l'une clé, c'est que la position est déjà occupée par un
        # identifiant, donc pas par un point. Donc on teste le point suivant.
        position_premier_point += 1
    return position_premier_point


def calcul_resultat(dic):
    return sum(identifiant * position for identifiant, position in dic.items() )
