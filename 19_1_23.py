import re
import sys
import time
import copy
import numpy as np
with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\19_1_ori.txt', 'r') as fichier:
    #contenu = fichier.read()
    #lignes = contenu.splitlines()
    lignes = fichier.readlines()
start=time.time()
partie="partie1"



pattern_workflow1 = re.compile("([A-Za-z0-9]+){(.*)}")
pattern_instructions = re.compile("([xmas])([><=])(\d+):([A-Za-z0-9]+)")
pattern_xmas = re.compile("{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}")

lignes_workflow = []
valeurs_xmas = []
bloc_courant = lignes_workflow
for ligne in lignes:
    if not ligne.strip():     # Si la ligne est vide, changer de bloc
        bloc_courant = valeurs_xmas
    else:
        bloc_courant.append(ligne.strip())

def découpage_partxmas(partxmas):  #découpe les parts en entrée et trouve les valeurs de x, m, a, s
    match=re.search(pattern_xmas,partxmas)
    if match:
        valeur_x = int(match.group(1))
        valeur_m = int(match.group(2))
        valeur_a = int(match.group(3))
        valeur_s = int(match.group(4))
        print(
            f"Pour le part : {partxmas} : valeur x : {valeur_x}; valeur m : {valeur_m} , valeur a : {valeur_a} , valeur s : {valeur_s}")
    else:
        print(f"pattern non reconnu pour le part {partxmas}")
        sys.exit("Instruction non reconnue. Arrêt du programme")
    dico_xmas = {"x":valeur_x , "m":valeur_m , "a":valeur_a , "s":valeur_s}
    return dico_xmas

def recherche_workflow(workflow_a_tester): #à partir du nom d'un workflow, permet de trouver les tests à effectuer pour ce workflow
    for ligne in lignes_workflow:
        match1 = re.search(pattern_workflow1, ligne)
        if match1:
            nom_workflow = match1.group(1)
            instructions_workflow = match1.group(2).split(sep=',')
        else:
            print(f"pattern non reconnu pour la ligne {ligne}")
            sys.exit("Ligne non reconnue. Arrêt du programme")
        if nom_workflow == workflow_a_tester :
            break #ou découpage_instructions(instructions)
    return instructions_workflow

def découpage_instruction(instruction):
    match2 = re.search(pattern_instructions, instruction)
    if match2:
        catégorie = match2.group(1)
        opérateur = match2.group(2)
        valeur_comparée = int(match2.group(3))
        workflow_suivant = match2.group(4)
        print(
            f"Pour l'instruction : {instruction} : catégorie : {catégorie}; opérateur : {opérateur} , valeur comparée : {valeur_comparée} , workflow suivant : {workflow_suivant}")
    else:
        print(f"pattern non reconnu pour l'instruction {instruction} de la ligne {ligne}")
        sys.exit("Instruction non reconnue. Arrêt du programme")

    return catégorie,opérateur,valeur_comparée,workflow_suivant

def traitement_instructions(dico_xmas, workflow_a_tester, catégorie,opérateur,valeur_comparée,workflow_suivant):
    flag_fin = 0
    if eval(f"dico_xmas[catégorie] {opérateur} valeur_comparée"):  #exemple : si dico_xmax { x : 350} , opérateur = "<" , valeur comparée = 200 ==> if 350 < 200
        workflow_a_tester=workflow_suivant
        flag_fin=1
    return workflow_a_tester, flag_fin

réponse = 0
for partxmas in valeurs_xmas :
    print(f"partxmas traité : {partxmas}")
    dico_xmas = découpage_partxmas(partxmas)
    décision_prise = False
    workflow_a_tester = "in"
    while décision_prise == False :
        instructions_workflow =recherche_workflow(workflow_a_tester)
        for instruction in instructions_workflow[0:-1]:
            catégorie, opérateur, valeur_comparée, workflow_suivant = découpage_instruction(instruction)
            workflow_a_tester, flag_fin = traitement_instructions(dico_xmas, workflow_a_tester, catégorie,opérateur,valeur_comparée,workflow_suivant)
            if flag_fin==1: #l'instruction testée remplit les conditions, on sort de la boucle, sinon on passe à l'instruction suivante
                break
        if flag_fin == 0 : #Si à la fin des instructions, aucune d'entre elle n'a rempli les conditions :
            workflow_a_tester = instructions_workflow[-1]
        if workflow_a_tester == "A" :
            décision_prise = True
            réponse += sum(dico_xmas[catégorie] for catégorie in dico_xmas)
        elif workflow_a_tester == "R" :
            décision_prise = True
    print(réponse)






