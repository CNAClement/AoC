import re
import sys
import time
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
        if coordonnees=="ZZZ":
            print("coordonnéées ZZZ trouvées ! ")
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

coordonnees="AAA"
nombre_steps=1

while coordonnees!='ZZZ':
    match_instructions = re.match(pattern_instructions, lignes[0])
    # attention, instructions sur plusieurs lignes
    if match_instructions:
        instructions = match_instructions.group()
    else:
        print("problème dans la prise en compte des instructions de la première ligne")
    coordonnees, nombre_steps =traitement_instructions(instructions,coordonnees,nombre_steps)



print(f"coordonnées fin d'instructions = {coordonnees} en {nombre_steps} steps et en {time.time()-start} secondes")
