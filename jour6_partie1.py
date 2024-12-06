import numpy as np

dict_direction = {"haut": (0, -1), "droite": (1,0) , "bas": (0, 1), "gauche": (-1, 0)}


def execution_jour6_partie1(chemin_fichier):
    tableau = chargement_tableau(chemin_fichier)
    position, direction = recherche_position_direction(tableau)
    agent_518 = Agent_518(position, direction)
    #print(f"position de l'agent : {agent_518.position}, direction de l'agent : {agent_518.direction}.")
    while in_area(tableau, agent_518.position, agent_518.direction ) :
        deplacement_agent(tableau, agent_518)
    print(f"Nombre de positions distinctes visitées : {np.count_nonzero(tableau == 'X')}")

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

    maj_tableau(tableau, position)  #remplace le '^' par un 'X'
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

def maj_tableau(tableau, coordonnees) :
    tableau[coordonnees[1]][coordonnees[0]] = 'X'
    # Pour mémoire : il y a une subtilité qui fait que ça ne marche pas d'utiliser l'autre fonction "tableau_coordonnees"
    # pour faire : tableau_coordonnees(tableau, coordonnees) = 'X'
    # L'idée c'est que tableau_coordonnees(tableau, coordonnees) ne fait que renvoyer une valeur. Ca dit juste "la valeur de ce tableau à cet endroit est 4"


def deplacement_agent(tableau, agent_518) :
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
        maj_tableau(tableau, nouvelles_coordonnees)
    return tableau






