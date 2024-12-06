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

    x_possibles = [x + directions[i][0] for i in range(len(directions))]
    y_possibles = [y + directions[i][1] for i in range(len(directions))]

    #for x_test, y_test in zip(x_possibles, y_possibles):
        #print(f"Coordonnées possibles (à tester) : {x_test, y_test}")

    return x_possibles, y_possibles


def test_déplacement_valide(tableau, x_test, y_test, path):
    # Vérifie si la position (x, y) est à l'intérieur de la matrice et est une cellule valide.
    flag_valide = 1
    if 0 <= x_test < tableau.shape[1] and 0 <= y_test < tableau.shape[0] :
         pass
    else : return 0  #on est hors de l'index, on sort de la fonction
    if tableau[y_test][x_test] in "#%" :
        flag_valide = 0

    if (x_test,y_test) in path :
        #print(f"la coordonnée ({x_test},{y_test} a déjà été visitée (présente dans le path")
        flag_valide = 0
    return flag_valide


def bfs(tableau):
    longueurs_chemins = []
    lignes_droites = []
    dico_ligne_droite = {} #un dico qui fait le lien entre le début de la ligne droite et la fin de la ligne droite
    start = np.where(tableau[0] == ".")[0]  # Position de départ
    start = (start[0],0)
    queue = deque([(start, [])])  # Utilisation d'une file pour BFS, avec chaque élément de la file contenant la position et le chemin parcouru.

    while queue:
        (x, y), path = queue.popleft()
        #print(f"\n \n On est sur la position : {x}, {y}")

        x_possible, y_possible =  déplacements_envisageables(tableau, x, y)
        # on teste si on arrive à la fin : on est à la fin lorsqu'aucune des 4 directions possibles ne peut être effectuée

        ligne_droite = True
        longueur_ligne_droite = 0
        coordonnées_entrée_ligne_droite = (x,y)
        while ligne_droite :
            #print(f"entrée while, x, y : {x}, {y} ")
            x_possible, y_possible =  déplacements_envisageables(tableau, x, y)
            compteur_chemins_connectés = 0
            for x_test, y_test in zip(x_possible, y_possible) : #Il y a 4 déplacements possibles
                if 0 <= x_test < tableau.shape[1] and 0 <= y_test < tableau.shape[0] and tableau[y_test][x_test] in (".><^v"):
                    compteur_chemins_connectés +=1
            #print(f"compteur : {compteur_chemins_connectés}")

            if compteur_chemins_connectés == 2 : # on est sur une ligne droite (dont un déjà parcouru)
                #pour ne pas faire de bruteforce, on ne touche pas à la file, on va simplement avancer sur le chemin jusqu'à une intersection
                path += [(x, y)]
                gestion_cas_douteux = 0 #une rustine pas très propre qui permet de sortir de la boucle quand
                # les deux chemins connectés sont dans le path et qu'on tombe dans une boucle infinie
                for x_test, y_test in zip(x_possible, y_possible) :
                    if tableau[y_test][x_test] in (".><^v") and (x_test, y_test) not in path :
                        x, y = x_test, y_test
                    else :
                        gestion_cas_douteux +=1

                if gestion_cas_douteux == 4 : # les deux chemins sont condamnés (dont aucun des 4 n'est exploitable)
                    #print(f"on a géré un cas douteux sur les coordonnées {x}, {y}")
                    break

            elif compteur_chemins_connectés == 1 : #normalement si aucun déplacement n'est valide (à part celui d'où on vient), c'est
                #soit que c'est un cul de sac (et on ne le comptabilise pas), soit qu'on est arrivés au bout du chemin.
                # Il y a également le cas particulier où on est en tout début de parcours.
                if y == 0 :
                    path += [(x, y)]
                    y = 1  #si on est sur la première ligne, le point suivant est forcément sur la ligne du dessous (on a d'ailleurs y_test = 1 )

                else :
                    ligne_droite = False

            else :
                ligne_droite = False

        #print(f"Après une petite ligne droite, on est désormais sur la position : {x}, {y}")
        x_possible, y_possible = déplacements_envisageables(tableau, x, y)
        for x_test, y_test in zip(x_possible, y_possible):
            if test_déplacement_valide(tableau, x_test, y_test, path):
                #print(f"le déplacement {x_test}, {y_test} est valide")
                new_path = path + [(x, y)]
                queue.append(((x_test, y_test), new_path))

        if y==tableau.shape[0]-1  and not (any(test_déplacement_valide(tableau, x_test, y_test, path) for x_test, y_test in
                   zip(x_possible, y_possible))) :

            new_path = path + [(x, y)]
            longueurs_chemins.append(len(new_path))
            print(f"\n \n \n\n\n\n AHHHHHHHHHHHHHHHHHHHHHHHHHHHH {longueurs_chemins}, {max(longueurs_chemins)}")
            #print(f"fin du chemin, new path : {new_path}, sortie aux coordonnées : {x}, {y}. \n Etat de la queue : {queue}")

    print(f"longueurs chemins : {longueurs_chemins}")
    print(new_path)
    longueur_max = max(longueurs_chemins)
    return longueur_max


longueur_max = bfs(tableau)
print(f"réponse : {longueur_max}")
