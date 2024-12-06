import re
import sys
import time
import copy
import numpy as np
from collections import deque



def création_dictionnaire(dico):
    #permet de créer les connexions inverses, c'est-à-dire si dico["rhn"] = "jqt" , alors dico["jqt"] = "rhn"
    clés_dico = list(dico.keys())
    for clé in clés_dico :
        #print(f"\n\n clé traitée : {clé}")
        valeurs = dico[clé]
        #print(f"valeurs traitées : {valeurs}")
        for valeur in valeurs :
            #print(f"valeur traitée : {valeur}")
            if valeur in dico :
                dico[valeur].extend([clé for clé in dico if valeur in dico[clé] and clé not in dico[valeur]]) #and clé != valeur ?
                #valeur in dico[clé] : si la valeur est associée à une clé, on ajoute cette valeur en tant que clé et la clé en tant que valeur (inversion du sens)
                #clé not in dico[valeur] : si la clé fait déjà partie des valeurs associées à valeur (autrement dit : si l'inversion a déjà été faite), alors on n'ajoute pas de doublon.
            else :
                dico[valeur] = [clé for clé in dico if valeur in dico[clé]]
    return dico

def sélection_cut(dico_graphe):
    """ Fonction qui sélectionne un triplet de connexions à couper, une connexion étant symbolisée par une paire (entrée-sortie)
    Renvoie toutes les combinaisons (aka tous les triplets) possibles. Pas de paires redondantes au sein d'un même triplet.
    Il faut générer 3 paires : (x,y) , le x étant le numéro du noeud et le y étant l'enfant à couper"""

    triplets = []

    for clé1 in dico_graphe.keys():
        for valeur1 in dico_graphe[clé1]:
            for clé2 in dico_graphe.keys():
                for valeur2 in dico_graphe[clé2]:
                    for clé3 in dico_graphe.keys():
                        for valeur3 in dico_graphe[clé3]:
                            """L'association for clék / for valeurk permet de parcourir toutes les valeurs associées à une clé donnée. On fait ça 3 fois pour obtenir
3 paires. Donc par exemple, si on fixe clé1 = "jqt" , on va itérer sur toutes les valeurs possible ("rhn" , "xhk" , "nvd"), on commence
par fixer valeur1 = "rhn" et on obtient notre première paire : ("jqt" , "rhn") . Puis on recommence avec une paire2, puis une paire3, et on itère.
    """
                            if ((clé1 == clé2 and valeur1 == valeur2) or (
                                clé1 == clé3 and valeur1 == valeur3) or (
                                clé2 == clé3 and valeur2 == valeur3) or (
                                clé1 == valeur2 and clé2 == valeur1) or (
                                clé1 == valeur3 and clé3 == valeur1) or (
                                clé2 == valeur3 and clé3 == valeur2)):
                            # on vérifie que les paires 1 et 2 ne sont pas identiques
                            # on vérifie que les paires 1 et 2 ne sont pas inversées, c'est à dire qu'on n'a pas ("A","B") et ("B","A)

                                pass
                            else:
                                paire1 = (clé1, valeur1)
                                paire2 = (clé2, valeur2)
                                paire3 = (clé3, valeur3)
                                triplet = (paire1, paire2, paire3)
                                triplets.append(triplet)
    print(f"longueur triplets : {len(triplets)} triplets")
    return triplets
def destruction_graphe(dico_graphe, triplets):
    for numéro_triplet, triplet in enumerate(triplets) :
        """pour chaque triplet, on va couper les connexions, puis une fois les connexions coupées, 
        pour chaque combinaison {entrée, sortie} du dictionnaire, on regarde si un chemin est possible. Si aucun chemin n'est possible, alors
        on a créé deux groupes distincts"""
        dico_graphe=copy.deepcopy(dico_graphe_save) #on réinitialise le dictionnaire avant de tenter le prochain triplet
        connexions_cassées = []
        #print(f"triplet : {triplet}")
        #pour chaque paire du triplet (paire ressemblant à (clé, valeur) ), on veut supprimer dans le dictionnaire la valeur associée à la clé.
        for paire in triplet :
            #print(f"paire : {paire}")
            dico_graphe[paire[0]].remove(paire[1])  #dico_graphe[paire[0]] renvoie la liste associée à la clé paire[0] (donc à la première valeur de la paire).
                                                    # remove(paire[1]) supprime dans cette liste la 2eme valeur de la paire
            dico_graphe[paire[1]].remove(paire[0])  #gérer la suppression du lien dans les deux sens

        #if ( (('hfx', 'pzl')  in triplet or ('pzl', 'hfx')  in triplet) and (('bvb' , 'cmg' )  in triplet or ('cmg' , 'bvb') in triplet) and (( 'jqt' , 'nvd')  in triplet or ( 'nvd' , 'jqt') in triplet) ):
        #if ( (('hfx', 'pzl')  in triplet or ('pzl', 'hfx')  in triplet) and (('bvb' , 'cmg' )  in triplet or ('cmg' , 'bvb') in triplet)  ):

            #print(f"après destruction : {dico_graphe}")

        index_combinaison = 0
        for début in dico_graphe :
            for objectif in dico_graphe:
                if début != objectif :
                    index_combinaison +=1
                    #print(f"triplet n° : {numéro_triplet}, combinaison n° {index_combinaison} : début : {début}, objectif : {objectif}")
                    if trouver_chemin(dico_graphe, début, objectif) == False :
                        connexions_cassées.append((début,objectif))
                        return triplet, connexions_cassées
    return "pas de triplet cassé", "pas de connexions cassées"



def trouver_chemin(graphe, début, objectif):
    queue = deque()
    queue.append((début, [début]))
    groupe_connecté = False

    while queue and groupe_connecté == False:
        (noeud, path) = queue.pop() #popleft si bfs
        noeuds_adjacents = [enfant for enfant in graphe[noeud] if enfant not in path]

        for noeud_adjacent in noeuds_adjacents:
            if noeud_adjacent == objectif:
                groupe_connecté = True
                return 1
            else:
                queue.append((noeud_adjacent, path + [noeud_adjacent]))

    if groupe_connecté == False :
        return 0 #il y a une connexion cassée


def calcul_taille_groupes(dico, connexions_cassées, triplet):
    """    Pour chacun des deux groupes créés en coupant les 3 connexions, on calcule le nombre de connexions possibles"""
    #on détruit une dernière fois le dictionnaire avec le triplet trouvé :
    for paire in triplet:
        # print(f"paire : {paire}")
        dico[paire[0]].remove(paire[1])
        dico[paire[1]].remove(paire[0])

    tailles_groupes = []
    for début in connexions_cassées:
        taille_groupe_connecté = 1 #le noeud de départ est lui-même inclus dans le groupe. S'il est relié à 3 noeuds, cela forme un groupe de 4.
        taille_groupe_déconnecté = -1 #pour ne pas compter la connexion invalide où le noeud de départ et d'arrivée sont les mêmes
        for objectif in dico :
            if trouver_chemin(dico, début, objectif) :
                taille_groupe_connecté+=1  #on a trouvé un chemin possible entre le début et l'objectif
                #print(f"chemin entre {début} et {objectif} valide, taille : {taille_groupe_connecté}")
            else :
                taille_groupe_déconnecté +=1
                #print(f"chemin entre {début} et {objectif} NON valide, taille : {taille_groupe_déconnecté}")

        tailles_groupes.append((taille_groupe_connecté,taille_groupe_déconnecté))
    return tailles_groupes




with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\25_1_ori.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
start=time.time()

pattern = re.compile("([a-z]{3}): ([a-z\s]*[a-z]+[a-z\s]*)")
#le deuxième groupe contient des lettres séparées éventuellement (mais pas obligatoirement) par des espaces.
# Donc un groupe avec un motif caractères + espaces qui se répète 0 ou plusieurs fois, puis un groupe avec des caractères.

dico_graphe = {}

for ligne in lignes :
    match = re.search(pattern, ligne)
    if match :
        noeud_parent = match.group(1)
        noeuds_enfants = match.group(2).split(sep=" ")
        #print(f"noeud parent : {noeud_parent}, noeuds enfants : {noeuds_enfants}")
        dico_graphe[noeud_parent] = noeuds_enfants
    else :
        print(f"pas de pattern trouvé pour la ligne : {ligne}")
        sys.exit("Pas de pattern trouvé. Arrêt du programme.")



print(f"dico pré-construit : {dico_graphe}")
dico_graphe=création_dictionnaire(dico_graphe)
print(f"dico construit : {dico_graphe}\n taille : {len(dico_graphe)}")
dico_graphe_save = copy.deepcopy(dico_graphe)

triplets = sélection_cut(dico_graphe)
#for triplet in triplets :
#    if ((('hfx', 'pzl') in triplet or ('pzl', 'hfx') in triplet) and (
#            ('jqt', 'nvd') in triplet or ('nvd', 'jqt') in triplet)):
#       print(f"triplet : {triplet}")

triplet, connexions_cassées=destruction_graphe(dico_graphe, triplets)
print(f"Pas de chemin entre {connexions_cassées} après avoir coupé les connexions {triplet}")

taille_groupe = calcul_taille_groupes(dico_graphe_save,connexions_cassées[0], triplet)
print(taille_groupe)
print(f"réponse : {taille_groupe[0][0]*taille_groupe[0][1]} , ou encore {taille_groupe[1][0]*taille_groupe[1][1]} ")
