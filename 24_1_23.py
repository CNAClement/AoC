import matplotlib.pyplot as plt
import numpy as np
import re
import sys
from itertools import combinations



with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\24_1_ori.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")
partie = "testdd"
if partie == "test":
    borne_inf = 7
    borne_sup = 27
else :
    borne_inf = 200000000000000
    borne_sup = 400000000000000

def tracer_droite(x,y):
    # Définir les points pour la première droite
    x1 = np.linspace(-10, 10, 100)
    y1 = 2 * x1 + 3

    # Tracer les droites
    plt.plot(x1, y1, label='Droite 1')

    # Ajouter les labels et la légende
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()

    # Afficher le graphique
    plt.show()

def trouver_coefficients(px,py,vx,vy,liste_coefficients):
    pente = vy/vx
    ordonnée_origine = py - pente * px
    #print(f"pente : {pente}, ordonnée : {ordonnée_origine}")
    liste_coefficients.append((pente,ordonnée_origine,px,py,vx,vy)) #on a besoin de px, vx, py et vy pour déterminer si le croisement a lieu dans le futur ou le passé
    return liste_coefficients

def chercher_intersection(liste_coefficients):
    croisements_futurs = 0 #croisements dans la zone de test
    paires = list(combinations(liste_coefficients, 2))
    #print(f"paires : {paires}")

    for paire in paires :
        #print(f"paire : {paire}")
        if paire[0][0]!=paire[1][0]:
            #les pentes ne sont pas les mêmes : les droites vont se croiser
            # Former le système d'équations : résoudre y1 = y2  (avec y1 et y2 qui valent respectivement ax1 + b1) revient à résoudre Ax + B avec A et B matrices des coefficients
            A = np.array([[paire[0][0], -1], [paire[1][0], -1]])
            B = np.array([-paire[0][1], -paire[1][1]])

            # Résoudre le système d'équations
            intersection = np.linalg.solve(A, B)

            # Afficher le résultat
            print("Intersection des droites :", tuple(intersection))

            if borne_inf<=tuple(intersection)[0]<=borne_sup and borne_inf<=tuple(intersection)[1]<=borne_sup :
                flag_passé = 0
                for droite in paire :
                    if (droite[4]<0 and tuple(intersection)[0]> droite[2]) or (droite[4]>0 and tuple(intersection)[0] < droite[2]) :
                        #si vx (paire[4] ) supérieur à 0 (ie : x augmente au cours du temps) et que l'intersection est plus petite que l'abscisse de départ : le croisement au eu lieu dans le passé
                        print(f"croisement dans le passé pour la droite {droite}")
                        flag_passé = 1

                if flag_passé == 0 :
                    croisements_futurs +=1
                    print(f"croisement comptabilisé pour la paire {paire}\n à l'intersection {intersection[0]}, {intersection[1]}")

            #else :
                #print(f"les rochers vont se croiser en dehors de la zone de test, aux coordonnées ({tuple(intersection)[0]}, {tuple(intersection)[1]})")
        #else : print("droites parallèles")
    return croisements_futurs

pattern = re.compile("(-?\d+), (-?\d+), (-?\d+) @ (-?\d+), (-?\d+), (-?\d+)")

liste_coefficients = []
for ligne in lignes :
    match = re.search(pattern, ligne)
    if match :
        px = int(match.group(1))
        py = int(match.group(2))
        pz = int(match.group(3))
        vx = int(match.group(4))
        vy = int(match.group(5))
        vz = int(match.group(6))
        #print(f"px : {px}, py : {py}, pz : {pz}, vx : {vx}, vy : {vy}, vz : {vz}")
    else :
        print(f"Pas de pattern trouvé pour la ligne {ligne}")
        sys.exit("Pas de match trouvé, arrêt du programme")
    liste_coefficients=trouver_coefficients(px,py,vx,vy,liste_coefficients)

#print(liste_coefficients)
chercher_intersection(liste_coefficients)
print(chercher_intersection(liste_coefficients))
