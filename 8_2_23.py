import re
import sys
import time
from math import lcm
with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\8_1_ori.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")

start=time.time()
pattern_instructions = re.compile("^[LR]+$")
pattern_coordonnees = re.compile('([A-Z]{3}) = \(([A-Z]{3}),\s([A-Z]{3})\)$')

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
        if coordonnees[2]=="Z":
            print("coordonnées en Z  trouvées ! ")
            break
        else : nombre_steps+=1

    return coordonnees, nombre_steps


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

liste_nombres_steps = []
for coordonnees in liste_coordonnees_a_traiter :
    nombre_steps=1
    while coordonnees[2]!='Z':
        match_instructions = re.match(pattern_instructions, lignes[0])
        # attention, instructions sur plusieurs lignes
        if match_instructions:
            instructions = match_instructions.group()
        else:
            print("problème dans la prise en compte des instructions de la première ligne")
        coordonnees, nombre_steps =traitement_instructions(instructions,coordonnees,nombre_steps)
    liste_nombres_steps.append(nombre_steps)

print(f"Pour chacune des {len(liste_coordonnees_a_traiter)} coordonnées à traiter, le nombre de steps avant la première coordonnée en Z et la sortie de la boucle est {liste_nombres_steps}")
rep=lcm(*liste_nombres_steps)

print(f"réponse = {rep} en {time.time()-start} secondes")
