# Pas lancé par le main parce que deux types de données dans le fichier en entrée, que je choisis
# de splitter manuellement pour ne pas m'embêter. On pourrait le faire avec un re.compile() .

"""
Logique du script :
On rentre dans le tableau en allant dans une position donnée. S'il y a un point juste à côté, on s'y déplace directement.
Sinon, si on rencontre un objet "O", on cherche le premier espace libre de l'autre côté, puis une fois qu'on
obtient cette position, on itère depuis cette position jusqu'à notre position actuelle en déplaçant l'objet "de proche en proche".
"""

from utils_clement import *
import math #petite aide pour trouver le signe donc le sens de déplacement de manière optimisée
mode = "reel" # "test_small", "test_large" , "reel"


def deplacement_tableau(tableau, position_robot , vect_deplacement):
    coordonnees_testees = maj_coordonnees(position_robot , vect_deplacement)
    #print(f"Coordonnees_testees : {coordonnees_testees} , caractère correspondant : {tableau[coordonnees_testees[1]][coordonnees_testees[0]]}")
    if tableau_coordonnees(tableau, coordonnees_testees) == "#" :
    #    print("pas de mise à jour")
        pass
    elif tableau_coordonnees(tableau, coordonnees_testees) == "." :
        maj_tableau(tableau,coordonnees_testees,"@")
        maj_tableau(tableau,position_robot,".")
        position_robot = coordonnees_testees
        #print(f"On a déplacé le robot qui se trouve maintenant en position {position_robot}.")
    elif tableau_coordonnees(tableau, coordonnees_testees) == "O" :
        #print("Objet à déplacer, on regarde derrière.")
        position_libre = chercher_espace_libre(tableau , coordonnees_testees, vect_deplacement )
        if position_libre == 0 :
            pass
            #print("Pas de position libre trouvée dans ce sens.")
        else :
            if vect_deplacement in ( (0,1), (0,-1)) : #déplacement vertical
                tableau = deplacer_objets(tableau, 1 , position_libre , position_robot)

            elif vect_deplacement in ( (1,0), (-1,0)) : #déplacement horizontal
                tableau = deplacer_objets(tableau, 0 , position_libre , position_robot)
            maj_tableau(tableau, position_robot, ".")
            #print(f"On a maj le tableau, la position du robot était {position_robot}, tableau vaut : {tableau_coordonnees(tableau, position_robot)}")
            position_robot = coordonnees_testees
    else :
        print("Cas impossible, ni # ni . ni O.")
        exit(1)

    return tableau , position_robot

def chercher_espace_libre(tableau, position, sens):
    while tableau_coordonnees(tableau, position) not in ('#' , "."):
        position = maj_coordonnees(position, sens)
    if tableau_coordonnees(tableau, position) == '#' :
        return 0
    elif tableau_coordonnees(tableau, position) == '.' :
        #print(f"Espace libre dans ce sens, en position {position}.")
        return position
    else :
        print("Cas normalement impossible.")
        exit(1)

def deplacer_objets(tableau, vertical, borne_depart, borne_arrivee) :  # Le deuxième paramètre vaut 1 pour vertical et 0 pour horizontal. Ca peut être vu comme un boléen (vertical = True ) mais en réalité c'est plutôt une coordonnée [0] ou [1]
    coordonnees = borne_depart
    signe_sens = int(math.copysign(1, (borne_arrivee[vertical] - borne_depart[vertical]))) #donnera -1 pour un déplacement vers la gauche ou le haut et 1 pour un déplacement vers la droite ou le bas (1.0 sans le int() )
    for _ in range(borne_depart[vertical], borne_arrivee[vertical], signe_sens):  # on veut itérer à l'envers si on va vers la gauche ou vers le haut, de l'emplacement libre jusqu'à la pierre
        if vertical :
            coordonnees_suivantes = maj_coordonnees(coordonnees, (0, signe_sens ))
        else :
            coordonnees_suivantes = maj_coordonnees(coordonnees, (signe_sens , 0)) # -1 pour un déplacement vers le haut, 1 vers le bas
        #print(f"Les coordonnées 'suivantes' (prochaine itération) sont : {coordonnees_suivantes}, à cet endroit, il y a : {tableau_coordonnees(tableau, coordonnees_suivantes)}")

        maj_tableau(tableau, coordonnees, tableau_coordonnees(tableau , coordonnees_suivantes))  # On met à jour le tableau avec la valeur du tableau à la coordonnée précédente. Exemple : .O. ==> .OO ==> ..O
        #print(f"On a maj les coordonnées : {coordonnees} , maintenant il y a : {tableau_coordonnees(tableau, coordonnees)}")
        #print(f"on est maintenant sur la coordonnée {coordonnees_suivantes}")
        coordonnees = coordonnees_suivantes
    return tableau

def gps_score(tableau) :
    """Fonction qui recherche la position de tous les O du tableau et renvoie un résultat de
    100 * son abscisse + son ordonnée."""
    liste_positions_pierres = recherche_valeurs(tableau, "O")
    print(liste_positions_pierres)
    fonction_calcul = lambda liste : 100 * sum(map(lambda t: t[0], liste)) +  sum(map(lambda t: t[1], liste))
    return fonction_calcul(liste_positions_pierres)

chemin_fichier_map = fr"C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2024\15_{mode}_map.txt"
chemin_fichier_deplacement = fr"C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2024\15_{mode}_deplacement.txt"


lignes_map = lecture_fichier(chemin_fichier_map)
tableau = chargement_tableau(lignes_map)
print(tableau)

deplacements = lecture_fichier(chemin_fichier_deplacement, "complet")
position_robot = reperage_position_caractere(tableau , "@")[0]

for deplacement in deplacements :
    if deplacement == "^" :
        #print(f"On tente de se déplacer vers le haut, position {position_robot}.")
        tableau, position_robot = deplacement_tableau(tableau , position_robot , (0,-1))
    elif deplacement == "<" :
        #print(f"On tente de se déplacer vers la gauche, position {position_robot}.")
        tableau, position_robot = deplacement_tableau(tableau , position_robot , (-1,0))
    elif deplacement == ">" :
        #print(f"On tente de se déplacer vers la droite, position {position_robot}.")
        tableau, position_robot = deplacement_tableau(tableau , position_robot , (1,0))
    elif deplacement == "v" :
        #print(f"On tente de se déplacer vers le bas, position {position_robot}.")
        tableau, position_robot = deplacement_tableau(tableau , position_robot , (0,1))

print(tableau)
print(f"Le résultat de la partie 1 est : {gps_score(tableau)}")