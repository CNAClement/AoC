from utils_clement import lecture_fichier, chargement_tableau, reperage_position_caractere
import numpy as np
from itertools import combinations


def execution_jour8_partie2(chemin_fichier):
    contenu=lecture_fichier(chemin_fichier , "complet")
    ensemble_caracteres_distincts = set(contenu) - {"." , "\n" , "#"}
    lignes = contenu.splitlines()  # Plutôt que de refaire lecture_fichier() , permet de ne pas lire le fichier deux fois. "Contenu" était utile pour les caractères distincts.
    tableau = chargement_tableau(lignes)
    global nombre_lignes
    nombre_lignes = tableau.shape[0]
    global nombre_colonnes
    nombre_colonnes = tableau.shape[1]

    positions_antinodes = set()
    for caractere in ensemble_caracteres_distincts :
        liste_coordonnees_antennes = reperage_position_caractere(tableau, caractere)
        position_antinodes_caractere = [placement_antinodes((coordonnees_antenne1 , coordonnees_antenne2)) for coordonnees_antenne1, coordonnees_antenne2 in combinations(liste_coordonnees_antennes, 2)]  # combinaisons de 2 éléments sans répétition (donc j > i toujours vrai )
        #print(f"Position des antinodes avant aplatissement : {position_antinodes}")
        positions_antinodes_caractere = {x for y in position_antinodes_caractere for x in y}
        #print(f"Position des antinodes après aplatissement : {position_antinodes}")
        print(f"Nombre de positions pour le caractère {caractere} : {len(positions_antinodes_caractere)}")
        positions_antinodes = positions_antinodes.union(positions_antinodes_caractere)

    print(f"Nombre de positions : {len(positions_antinodes)}")
    resultat = comptage_antinodes(positions_antinodes)
    print(f"Il y a {resultat} antinodes.")

def placement_antinodes(couple_coordonnees ) :
    # Contrairement à la partie 1, les antinodes peuvent également se situer sur les positions des antennes elles-memes.
    distance = calcul_distance(couple_coordonnees)
    #print(f"On traite le couple : {couple_coordonnees} , distance séparant les antennes : {distance}")
    coordonnees_antinodes = None # Initialisation bidon pour pouvoir rentrer dans le while
    coordonnees_antinodes_complete = set()
    iteration = 0
    while coordonnees_antinodes != coordonnees_antinodes_complete :
        coordonnees_antinodes = coordonnees_antinodes_complete
        coordonnees_antinodes_iteration = {
            (coordonnees[0] + iteration * delta_x, coordonnees[1] + iteration * delta_y)
            for coordonnees in couple_coordonnees
            for delta_x, delta_y in [(distance[0], distance[1]), (-distance[0], -distance[1])]
            if 0 <= coordonnees[0] + iteration * delta_x < nombre_colonnes and 0 <= coordonnees[1] + iteration * delta_y < nombre_lignes
        }
        coordonnees_antinodes_complete = coordonnees_antinodes.union(coordonnees_antinodes_iteration)
        iteration +=1

    #print(f"Pour le couple d'antennes aux coordonnées {couple_coordonnees} séparés d'une distance de {distance}, les positions des antinodes seraient : {coordonnees_antinodes}")
    return coordonnees_antinodes

def calcul_distance(couples_coordonnees):
    coordonnee1=couples_coordonnees[0]
    coordonnee2=couples_coordonnees[1]
    return (coordonnee2[0] - coordonnee1[0], coordonnee2[1] - coordonnee1[1])

def comptage_antinodes(positions_antinodes):
    nombre_positions_validees = 0
    for coordonnees_antinode in positions_antinodes :
        if coordonnees_antinode[0] >= 0 and coordonnees_antinode[0]<nombre_colonnes\
            and coordonnees_antinode[1] >= 0 and coordonnees_antinode[1] < nombre_lignes :
            nombre_positions_validees += 1
    return nombre_positions_validees





