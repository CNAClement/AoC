import re
import sys
import time
with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\8_1_2.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")

start=time.time()
pattern_instructions = re.compile("^[LR]+$")
pattern_coordonnees = re.compile('([A-Z0-9]{3}) = \(([A-Z0-9]{3}),\s([A-Z0-9]{3})\)$')

def traitement_instructions(instructions,liste_coordonnees,nombre_steps,boucle):
    for instruction in instructions:
        print(f"coordonnées traitées : {liste_coordonnees}")
        print(f"on traite l'instruction : {instruction}")
        lignes_a_traiter=recherche_ligne(liste_coordonnees)
        liste_coordonnees_gauche,liste_coordonnees_droite=decoupage_ligne(lignes_a_traiter)
        if instruction=='L':
            liste_coordonnees=liste_coordonnees_gauche
        elif instruction=='R':
            liste_coordonnees=liste_coordonnees_droite
        else :
            print(f"instruction non comprise : {instruction}")
            sys.exit("Abend: Instruction non comprise. Arrêt du programme.")
        flag_arrivee=test_arrivee(liste_coordonnees)
        if flag_arrivee==1:
            break
        else : nombre_steps+=1
        boucle+=1
        if boucle==260:
            print(f"toujours là, toujours debout, {nombre_steps} steps, coordonnées : {liste_coordonnees} ")
            boucle=0

    return flag_arrivee, liste_coordonnees, nombre_steps


def recherche_ligne(liste_coordonnees):
    lignes_a_traiter =[]
    for coordonnees in liste_coordonnees:
        for ligne in lignes:
            if coordonnees in ligne[0:3] :
                lignes_a_traiter.append(ligne)
    return lignes_a_traiter


def decoupage_ligne(lignes_a_traiter):
    liste_coordonnees_gauche = []
    liste_coordonnees_droite = []
    for ligne_a_traiter in lignes_a_traiter:
        match_coordonnees = re.search(pattern_coordonnees, ligne_a_traiter)
        if match_coordonnees:
            coordonnees_gauche = match_coordonnees.group(2)
            coordonnees_droite = match_coordonnees.group(3)
            liste_coordonnees_gauche.append(coordonnees_gauche)
            liste_coordonnees_droite.append(coordonnees_droite)
        else :
            print(f"Pas de match du pattern sur la ligne {ligne_a_traiter}")
            sys.exit("Abend: Aucun match trouvé. Arrêt du programme.")
    return liste_coordonnees_gauche,liste_coordonnees_droite

def starting_nodes() :
    starting_nodes=[]
    for ligne in lignes:
        match_coordonnees = re.search(pattern_coordonnees, ligne)
        if match_coordonnees:
            if match_coordonnees.group(1)[2]=="A": #(si la 3eme lettre des coordonnées de départ commence par A)
                starting_nodes.append(match_coordonnees.group(1))
    return starting_nodes

def test_arrivee(current_positions):
    compteur_positions_de_fin=0
    flag_arrivee=0
    for coordonnees in current_positions:
        if coordonnees[2]=="Z":
            compteur_positions_de_fin+=1
    if compteur_positions_de_fin==len(current_positions):
        print("on est arrivé !")
        flag_arrivee = 1
    return flag_arrivee

flag_arrivee = 0
nombre_steps=1

liste_coordonnees=starting_nodes()
print(f"positions de départ : {liste_coordonnees}")

boucle=0

while flag_arrivee == 0 :
#if flag_arrivee == 0 :
    match_instructions = re.match(pattern_instructions, lignes[0])
    # attention, instructions sur plusieurs lignes
    if match_instructions:
        instructions = match_instructions.group()
    else:
        print("problème dans la prise en compte des instructions de la première ligne")
    flag_arrivee, liste_coordonnees, nombre_steps =traitement_instructions(instructions,liste_coordonnees,nombre_steps,boucle)

print(f"coordonnées fin d'instructions = {liste_coordonnees} en {nombre_steps} steps et en {time.time()-start} secondes")
