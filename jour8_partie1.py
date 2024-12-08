from utils_clement import lecture_fichier, chargement_tableau, reperage_position_caractere
import numpy as np
from itertools import combinations


def execution_jour8_partie1(chemin_fichier):
    contenu=lecture_fichier(chemin_fichier , "complet")
    ensemble_caracteres_distincts = set(contenu) - {"." , "\n" , "#"}
    lignes = contenu.splitlines()  # Plutôt que de refaire lecture_fichier() , permet de ne pas lire le fichier deux fois. "Contenu" était utile pour les caractères distincts.
    tableau = chargement_tableau(lignes)
    global nombre_lignes
    nombre_lignes = tableau.shape[0]
    global nombre_colonnes
    nombre_colonnes = tableau.shape[1]

    print(tableau)
    positions_antinodes = []
    for caractere in ensemble_caracteres_distincts :
        liste_coordonnees_antennes = reperage_position_caractere(tableau, caractere)
        print(f"liste des coordonnées des fréquences {caractere} : {liste_coordonnees_antennes}")

        position_antinodes = [placement_antinodes((coordonnees_antenne1 , coordonnees_antenne2)) for coordonnees_antenne1, coordonnees_antenne2 in combinations(liste_coordonnees_antennes, 2)]  # combinaisons de 2 éléments sans répétition (donc j > i toujours vrai )
        print(f"Position des antinodes : {position_antinodes}")
        positions_antinodes += position_antinodes
    print(f"somme des positions : {positions_antinodes}")
    positions_tot = {x for y in positions_antinodes for x in y}
    comptage_antinodes(positions_tot)

def placement_antinodes(couple_coordonnees ) :
    # Connaissant les coordonnées des antennes et la distance qui les sépare, on peut déduire la position des antinodes.
    # Il suffit de faire coordonnees - distance et coordonnees + distance, et de ne garder que les résultats qui ne sont pas égaux à une des deux coordonnées (en attendant de trouver plus optimisé ...)
    # Comme les noeuds doivent être de part et d'autres des antennes (donc "à l'extérieur" du segment), il y a deux de ces opérations qui partent "dans le mauvais sens"
    # et ne font que retomber sur l'autre antenne (en effet : si deux points sont distants de d et qu'on fait coord(point 1) + d dans le mauvais sens, on arrive sur coord(point 2)

    # Par exemple pour (3,3) et (4,4) , séparés d'une distance (1,1) : il suffit de faire (3,3) + (1,1) et  (3,3) - (1,1) , (4,4) + (1,1) et (4,4) - (1,1) et enlever la 1ere et la 4eme.
    # ps : on peut se contenter de tester l'abscisse. Si on arrive sur une abscisse déjà occupée, alors on est forcément sur la même coordonnée complète.

    abscisses_antennes = {coordonnees[0] for coordonnees in couple_coordonnees}
    # print(f"Abscisses déjà occupées par les antennes : {abscisses_antennes}.")
    distance = calcul_distance(couple_coordonnees)
    print(f"Distance séparant les antennes : {distance}")
    #coordonnees_antinodes1 = {(coordonnees[0] + distance[0], coordonnees[1] + distance[1]) for coordonnees in
    #                         couple_coordonnees if coordonnees[0] + distance[0] not in abscisses_antennes }
    #coordonnees_antinodes2 = {(coordonnees[0] - distance[0], coordonnees[1] - distance[1]) for coordonnees in
    #                          couple_coordonnees if coordonnees[0] - distance[0] not in abscisses_antennes}

    # coordonnees_antinodes = coordonnees_antinodes1.union(coordonnees_antinodes2)

    # Plus élégant : rajouter une boucle for dans la compréhension, avec delta permettant de soit ajouter soit retirer la distance.
    coordonnees_antinodes = {
        (coordonnees[0] + delta_x, coordonnees[1] + delta_y)
        for coordonnees in couple_coordonnees
        for delta_x, delta_y in [(distance[0], distance[1]), (-distance[0], -distance[1])]
        if coordonnees[0] + delta_x not in abscisses_antennes
    }

    print(f"Pour le couple d'antennes aux coordonnées {couple_coordonnees} séparés d'une distance de {distance}, la position des antinodes serait : {coordonnees_antinodes}")
    return coordonnees_antinodes

def calcul_distance(couples_coordonnees):
    coordonnee1=couples_coordonnees[0]
    coordonnee2=couples_coordonnees[1]
    return (coordonnee2[0] - coordonnee1[0], coordonnee2[1] - coordonnee1[1])

def comptage_antinodes(positions_antinodes):
    nombre_positions_validees = 0
    print(nombre_lignes, nombre_colonnes)
    for coordonnees_antinode in positions_antinodes :
        if coordonnees_antinode[0] >= 0 and coordonnees_antinode[0]<nombre_colonnes\
            and coordonnees_antinode[1] >= 0 and coordonnees_antinode[1] < nombre_lignes :
            nombre_positions_validees += 1
            #print(f"Coordonnées antinode OK : {coordonnees_antinode}")
    print(f"Il y a {nombre_positions_validees} antinodes.")





