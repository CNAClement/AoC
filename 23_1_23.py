from collections import deque
import numpy as np
import time

with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\23_1_ori.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")

start=time.time()

new_list=[]
for ligne in lignes:
    for caractere in ligne :
        new_list.append(caractere)
array=np.asarray(new_list)
#print(f" array : {array} , nombre de lignes : {int(len(lignes))}, taille d'une ligne : {int(len(lignes[0]))}")
tableau=array.reshape(int(len(lignes)), int(len(lignes[0])))

def déplacements_envisageables(tableau, x, y) :
    # Explore les 4 directions possibles (haut, droite, bas, gauche)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    if tableau[y][x] != "#" :
        x_possibles = [x + directions[i][0] for i in range(len(directions))]
        y_possibles = [y + directions[i][1] for i in range(len(directions))]

    """    elif tableau[y][x] == ">" :
        x_possibles  = [x + 1]
        y_possibles = [y]

    elif tableau[y][x] == ">" :
        x_possibles  = [x + 1]
        y_possibles = [y]

    elif tableau[y][x] == "<" :
        x_possibles  = [x - 1]
        y_possibles = [y]

    elif tableau[y][x] == "v" :
        x_possibles  = [x]
        y_possibles = [y + 1]

    elif tableau[y][x] == "^" :
        x_possibles  = [x]
        y_possibles = [y - 1]"""

    #for x_test, y_test in zip(x_possibles, y_possibles):
        #print(f"Coordonnées possibles (à tester) : {x_test, y_test}")

    return x_possibles, y_possibles


def test_déplacement_valide(tableau, x_test, y_test, path):
    # Vérifie si la position (x, y) est à l'intérieur de la matrice et est une cellule valide.
    flag_valide = 1
    if 0 <= x_test < tableau.shape[1] and 0 <= y_test < tableau.shape[0] :
         pass
    else : return 0  #on est hors de l'index, on sort de la fonction
    if tableau[y_test][x_test] == "#" :
        flag_valide = 0

    if (x_test,y_test) in path :
        #print(f"la coordonnée ({x_test},{y_test} a déjà été visitée (présente dans le path")
        flag_valide = 0
    return flag_valide


def bfs(tableau):
    longueurs_chemins = []
    start = np.where(tableau[0] == ".")[0]  # Position de départ
    start = (start[0],0)
    queue = deque([(start, [])])  # Utilisation d'une file pour BFS, avec chaque élément de la file contenant la position et le chemin parcouru.

    while queue:
        (x, y), path = queue.popleft()
        #print(f"\n \n On est sur la position : {x}, {y}")

        x_possible, y_possible =  déplacements_envisageables(tableau, x, y)
        # on teste si on arrive à la fin : on est à la fin lorsqu'aucune des 4 directions possibles ne peut être effectuée
        if y==tableau.shape[0]-1  and not (any(test_déplacement_valide(tableau, x_test, y_test, path) for x_test, y_test in
                   zip(x_possible, y_possible))) :

            new_path = path + [(x, y)]
            longueurs_chemins.append(len(new_path))
            #print(f"fin du chemin, new path : {new_path}, sortie aux coordonnées : {x}, {y}. \n Etat de la queue : {queue}")

        x_possible, y_possible =  déplacements_envisageables(tableau, x, y)
        for x_test, y_test in zip(x_possible, y_possible) :
            #print(f"On regarde si le déplacement vers : {x_test}, {y_test} est valide")
            if test_déplacement_valide(tableau, x_test, y_test, path):
                #print("le déplacement est valide")
                new_path = path + [(x, y)]
                queue.append(((x_test, y_test), new_path))

            #else : print("le déplacement n'est pas valide" )

    #return None  # Aucun chemin trouvé
    return longueurs_chemins


longueurs_chemins = bfs(tableau)
print(longueurs_chemins)
print(f"réponse : {max(longueurs_chemins)-1}")
