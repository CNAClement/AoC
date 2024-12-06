"""Définition d'une loop : si l'agent repasse à la même position et dans la même direction (pas nécessairement la position de départ)
On ne peut rajouter qu'un seul obstacle, donc ça veut déjà dire qu'on peut se limiter aux 4883 positions visitées puisqu'on ne risque pas
de passer sur une autre position (ce qui aurait été possible avec plusieurs obstacles).
Donc idée "brute force" : récupérer les 4883 positions visitées et leur direction associée, et pour chacune d'entre elles, simuler la présence d'un obstacle et regarder si
A un moment donné, on revient à un couple (position, direction) déjà stocké
"""

import numpy as np

dict_direction = {"haut": (0, -1), "droite": (1,0) , "bas": (0, 1), "gauche": (-1, 0)}


def execution_jour6_partie2(chemin_fichier):
    tableau = chargement_tableau(chemin_fichier)
    agent_518, liste_visites = initialisation(tableau)
    while in_area(tableau, agent_518.position, agent_518.direction ) :
        liste_visites = deplacement_agent(tableau, agent_518 , liste_visites)
    liste_visites =  {x[0] for x in liste_visites} #On ne garde que la première partie du tuple, la direction n'est pas utile ici.
    # De plus on dédoublonne à l'aide du set (ici : { } ) .  Initialement : list({x[0] for x in liste_visites}) mais en fait le list() n'est même pas obligatoire.
    liste_visites.remove(recherche_position_direction(tableau)[0]) # On enlève le point de départ
    print(f"longueur de la liste (ou plutôt de l'ensemble) : {len(liste_visites)}")
    nombre_boucleries_possibles = 0
    compteur_pour_affichage = 0
    for position_visitee in liste_visites :
        compteur_pour_affichage += 1
        print(f"Nombre de positions testées : {compteur_pour_affichage}")
        tableau_avec_obstacle = ajout_obstacle_tableau(tableau, position_visitee)
        # On reset (à partir du tableau initial) la position, direction de l'agent et la liste des visites faites
        agent_518, liste_visites = initialisation(tableau)
        while in_area(tableau, agent_518.position, agent_518.direction ) :
            if (agent_518.position, agent_518.direction) in (liste_visites[:-1]) :
                nombre_boucleries_possibles += 1
                print(f"Bouclerie trouvée en position {position_visitee}")
                break
            liste_visites = deplacement_agent(tableau_avec_obstacle, agent_518 , liste_visites)
    print(f"Nombre de boucleries = {nombre_boucleries_possibles}")


class Agent_518:
    """ Les instances de cette classe sont des objets avec deux attributs :
        - position
        - direction

    et une méthode : direction() """

    def __init__(self,position:tuple,direction:str):
        self.position = position
        self.direction = direction

    def deplacement(self):
        self.position=tuple(x + y for x, y in zip(self.position, dict_direction[self.direction]))
        return self.position


def lecture_fichier(chemin_fichier):
    with open(chemin_fichier, 'r') as fichier:
        contenu = fichier.read()
        lignes = contenu.splitlines()
        return lignes

def chargement_tableau(chemin_fichier):
    lignes = lecture_fichier(chemin_fichier)
    parametre_nombre_colonnes_tableau = len(lignes[0])
    print(f"le tableau devrait avoir {len(lignes)} lignes et {parametre_nombre_colonnes_tableau} colonnes.")
    liste_caracteres = []
    for ligne in lignes:
        for caractere in ligne:
            liste_caracteres.append(caractere)

    array = np.asarray(liste_caracteres)
    tableau = array.reshape(int(len(liste_caracteres) / parametre_nombre_colonnes_tableau),
                            parametre_nombre_colonnes_tableau)
    return tableau


def initialisation(tableau):
    position, direction = recherche_position_direction(tableau)
    agent_518 = Agent_518(position, direction)
    liste_visites = []  # Contient la liste des (position, direction) .
    return agent_518, liste_visites

def recherche_position_direction(tableau):
    # position_agent = tuple(np.where(tableau == "^" ))
    # np.where renvoie deux tableaux numpy, un qui donne la position des indices sur l'axe horizontal et un qui
    # donne la position des indices sur l'axe vertical.
    # Plusieurs méthodes pour en tirer un tuple :
    # - soit : position_agent = tuple(coord[0] for coord in np.where(tableau == "^")) ==> à condition qu'il y ait une et une seule position de l'agent (KO si 0, pas fiable si >1 )
    # - soit : positions = list(zip(*np.where(tableau == "^")))
    position = tuple(int(coord[0]) for coord in np.where(tableau == "^"))
    position = (lambda x : (x[1] , x[0]))(position)  # (3, 4) devient (4,3), ce qui respecte la notation (abscisse, ordonnée)

    if tableau[position[1]][position[0]] == "^" :
        direction = "haut"
    elif tableau[position[1]][position[0]] == ">" :
        direction = "droite"
    if tableau[position[1]][position[0]] == "v" :
        direction = "bas"
    if tableau[position[1]][position[0]] == "<" :
        direction = "gauche"
    return position, direction

def in_area(tableau, position, direction ) : # Vérifie que l'agent ne va pas sortir du tableau
    # Si l'une des conditions est respectée (donc condition générale True alors on sort du tableau et on renvoie False.
    # Et inversement, si le test renvoie False, alors on sort en True.

    return not (coordonnee_suivante(position, direction)[0]<0 \
        or coordonnee_suivante(position, direction)[0] == tableau.shape[1] \
        or coordonnee_suivante(position, direction)[1] < 0 \
        or coordonnee_suivante(position, direction)[1] == tableau.shape[0])



def coordonnee_suivante(position, direction):
    nouvelles_coordonnees = (position[0] + dict_direction[direction][0] , position[1] + dict_direction[direction][1])
    return nouvelles_coordonnees

def tableau_coordonnees(tableau, coordonnees):
    return tableau[coordonnees[1]][coordonnees[0]]

def ajout_obstacle_tableau(tableau, coordonnees):
    tableau_modifié = tableau.copy()
    tableau_modifié[coordonnees[1]][coordonnees[0]]="#"
    return tableau_modifié


def deplacement_agent(tableau, agent_518, liste_visites ) :
    # Dictionnaire de correspondance entre ancienne direction et nouvelle direction en cas de rotation
    rotation_droite = {
        "haut": "droite",
        "droite": "bas",
        "bas": "gauche",
        "gauche": "haut"
    }
    nouvelles_coordonnees = coordonnee_suivante(agent_518.position , agent_518.direction )
    if tableau_coordonnees(tableau,nouvelles_coordonnees)=="#":
        agent_518.direction = rotation_droite[agent_518.direction]
        #print(f"Nouvelle direction : {agent_518.direction}")
    else :
        agent_518.deplacement()
        #print(f"Nouvelle position : {agent_518.position}")
        liste_visites.append((agent_518.position , agent_518.direction))
    return liste_visites






