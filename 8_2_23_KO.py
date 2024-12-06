import re
import sys
import time
from math import lcm

with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\8_1_2.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")

start=time.time()
pattern_instructions = re.compile("^[LR]+$")
pattern_coordonnees = re.compile('([A-Z0-9]{3}) = \(([A-Z0-9]{3}),\s([A-Z0-9]{3})\)$')

def traitement_instructions(instructions,coordonnees,nombre_steps):
    for instruction in instructions:
        #print(f"coordonnées traitées : {coordonnees}")
        #print(f"on traite l'instruction : {instruction}")
        ligne_a_traiter=recherche_ligne(coordonnees)
        #print(f"Coordonnée {coordonnees} trouvée sur la ligne {ligne_a_traiter}")
        coordonnees_gauche,coordonnees_droite=decoupage_ligne(ligne_a_traiter)
        #print(f"coordonnées gauche : {coordonnees_gauche}, coordonnées droite : {coordonnees_droite}")
        if instruction=='L':
            coordonnees=coordonnees_gauche
        elif instruction=='R':
            coordonnees=coordonnees_droite
        else :
            print(f"instruction non comprise : {instruction}")
            sys.exit("Abend: Instruction non comprise. Arrêt du programme.")
        # on met entre commentaires la condition de sortie, on va jusqu'au bout de la suite d'instructions jusqu'à trouver un cycle (c'est-à-dire être revenu à la situation initiale, mêmes coordonnées, mêmes instructions)
        #if coordonnees=="ZZZ":
        #    print("coordonnéées ZZZ trouvées ! ")
        #    break
        #else : nombre_steps+=1
        nombre_steps+=1
    return coordonnees, nombre_steps

def traque_Z(instructions,coordonnees,nombre_steps_Z,flag_Z):
    for instruction in instructions:
        #print(f"coordonnées traitées : {coordonnees}")
        #print(f"on traite l'instruction : {instruction}")
        ligne_a_traiter=recherche_ligne(coordonnees)
        #print(f"Coordonnée {coordonnees} trouvée sur la ligne {ligne_a_traiter}")
        coordonnees_gauche,coordonnees_droite=decoupage_ligne(ligne_a_traiter)
        #print(f"coordonnées gauche : {coordonnees_gauche}, coordonnées droite : {coordonnees_droite}")
        if instruction=='L':
            coordonnees=coordonnees_gauche
        elif instruction=='R':
            coordonnees=coordonnees_droite
        else :
            print(f"instruction non comprise : {instruction}")
            sys.exit("Abend: Instruction non comprise. Arrêt du programme.")
        if coordonnees[2]=="Z":
            print(f"coordonnée en Z trouvée ! Au step {nombre_steps_Z}")
            flag_Z=1
            break
        else : flag_Z = 0
        nombre_steps_Z+=1
    return coordonnees, nombre_steps_Z, flag_Z


def recherche_ligne(coordonnees):
    for ligne in lignes:
        if coordonnees in ligne[0:3] :
            ligne_a_traiter=ligne
    return ligne_a_traiter


def decoupage_ligne(ligne_a_traiter):
    match_coordonnees = re.search(pattern_coordonnees, ligne_a_traiter)
    if match_coordonnees:
        coordonnees_gauche = match_coordonnees.group(2)
        coordonnees_droite = match_coordonnees.group(3)
    else :
        print(f"Pas de match du pattern sur la ligne {ligne_a_traiter}")
        sys.exit("Abend: Aucun match trouvé. Arrêt du programme.")

    return coordonnees_gauche,coordonnees_droite

def starting_nodes() :
    starting_nodes=[]
    for ligne in lignes:
        match_coordonnees = re.search(pattern_coordonnees, ligne)
        if match_coordonnees:
            if match_coordonnees.group(1)[2]=="A": #(si la 3eme lettre des coordonnées de départ commence par A)
                starting_nodes.append(match_coordonnees.group(1))
    return starting_nodes



liste_coordonnees_a_traiter=starting_nodes()
print(f"liste des coordonnées finissant par un 'A' : {liste_coordonnees_a_traiter}")
liste_steps_coordonnees=[]
liste_steps_Z=[]
for coordonnees in liste_coordonnees_a_traiter:
    print(f"Coordonnée traitée : {coordonnees}")
    nombre_steps = 1
    coordonnees_occurrences=[(coordonnees,1)]
    occurrence_max=1
    while occurrence_max < 2 : #tant qu'une coordonnée n'a pas été traitée deux fois au début des instructions ( c'est-à-dire un cycle complet)
        match_instructions = re.match(pattern_instructions, lignes[0])
        # attention, instructions sur plusieurs lignes
        if match_instructions:
            instructions = match_instructions.group()
        else:
            print("problème dans la prise en compte des instructions de la première ligne")
        coordonnees, nombre_steps =traitement_instructions(instructions,coordonnees,nombre_steps)
        for indice in range(len(coordonnees_occurrences)):
            if coordonnees_occurrences[indice][0]==coordonnees:
                coordonnees_occurrences[indice][1]+=1
        coordonnees_occurrences.append([coordonnees,1])
        #print(f"coordonnées et occurrences : {coordonnees_occurrences}")
        occurrence_max=max(paire[1] for paire in coordonnees_occurrences)

    print(f"on a trouvé un cycle complet pour la coordonnée {coordonnees} en {nombre_steps} steps et en {time.time()-start} secondes")
    liste_steps_coordonnees.append(nombre_steps)
    print(f"on fait un dernier cycle ... coordonnée {coordonnees} en espérant trouver un Z ... ")
    flag_Z=0
    nombre_steps_Z=1
    while flag_Z == 0 :
        coordonnees, nombre_steps_Z, flag_Z = traque_Z(instructions, coordonnees, nombre_steps_Z,flag_Z)
    liste_steps_Z.append(nombre_steps_Z)

print(f"Pour chacune des {len(liste_coordonnees_a_traiter)} coordonnées à traiter, le nombre de steps avant le début de la première boucle est {liste_steps_coordonnees} et le nombre de steps avant d'arriver au Z dans la boucle est {liste_steps_Z}")
rep1=lcm(*liste_steps_coordonnees)
rep2=lcm(*liste_steps_Z)
print(f"lcm coordonnées : {rep1}, lcm Z : {rep2}")