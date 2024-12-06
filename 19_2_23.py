import re
import sys
import time
import copy
import numpy as np
from collections import deque

with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\19_1.txt', 'r') as fichier:
    #contenu = fichier.read()
    #lignes = contenu.splitlines()
    lignes = fichier.readlines()
start=time.time()


pattern_workflow1 = re.compile("([A-Za-z0-9]+){(.*)}")
pattern_instructions = re.compile("([xmas])([><=])(\d+):([A-Za-z0-9]+)")

lignes_workflow = []
for ligne in lignes:
    if not ligne.strip():     # Si la ligne est vide, on arrête, pas besoin de gérer les blocs de valeurs pour la partie 2
        break
    else:
        lignes_workflow.append(ligne.strip())

def recherche_workflow(workflow_complet):
#pour la partie 2 : permet d'extraire le nom du workflow de chaque ligne de chaque ligne, ce workflow sera le workflow parent
    match1 = re.search(pattern_workflow1, workflow_complet)
    if match1:
        workflow_parent = match1.group(1)
        instructions_workflow = match1.group(2).split(sep=',')
    else:
        print(f"pattern non reconnu pour le workflow {workflow_complet}")
        sys.exit("Ligne non reconnue. Arrêt du programme")
    return workflow_parent, instructions_workflow

def découpage_instruction(instruction):
    match2 = re.search(pattern_instructions, instruction)
    if match2:
        catégorie = match2.group(1)
        opérateur = match2.group(2)
        valeur_comparée = int(match2.group(3))
        workflow_suivant = match2.group(4)
       # print(f"Pour l'instruction : {instruction} : catégorie : {catégorie}; opérateur : {opérateur} , valeur comparée : {valeur_comparée} , workflow suivant : {workflow_suivant}")
    else:
        print(f"pattern non reconnu pour l'instruction {instruction} de la ligne {ligne}")
        sys.exit("Instruction non reconnue. Arrêt du programme")

    return catégorie,opérateur,valeur_comparée,workflow_suivant

def création_dictionnaire_graphe(workflow_parent, workflows_enfants): #permet d'associer un workflow parent à plusieurs workflow enfants
    dico_graphe[workflow_parent]=workflows_enfants
    return dico_graphe

def dfs_inadapté(dico_graphe, noeud): #pas adapté car trouve un chemin et s'arrête là
    dico_état = dict()
    for noeud_workflow in dico_graphe :
        dico_état[noeud_workflow]="non traité"
    dico_parents = dict()
    dico_parents[noeud]=None
    dico_état[noeud]="en cours de traitement"
    print(f"dico état : {dico_état['A']}")
    liste_attente = [noeud]
    while liste_attente :
        noeud_traité = liste_attente[-1]
        enfants_potentiels =  [noeud for noeud in dico_graphe[noeud_traité] if dico_état[noeud]=="non traité" ]
        # si le noeud "parent" n'a pas encore été traité, tous les noeuds associés dans le dico deviennent potentiellement des noeuds enfants
        if enfants_potentiels :
            enfant = enfants_potentiels[0] #on prend le premier trouvé
            dico_parents[enfant]=noeud_traité
            dico_état[enfant]="en cours de traitement"
            liste_attente.append(enfant)
        else :
            dico_état[noeud_traité]="définitivement traité"
            liste_attente.pop()
    print(dico_parents)
    # idée : on remonte l'arbre à partir du 1er parent de "A" trouvé, puis on supprime ce parent du dico_graphe
    #afin de forcer un nouveau chemin, et on recommence tant que de nouveaux chemins sont possibles (tant que "A" a un parent)
    return dico_parents


def trouver_chemin(graphe, début, objectif):
    stack = deque()
    stack.append((début, [début]))

    while stack:
        (noeud, path) = stack.pop()
        noeuds_adjacents = [enfant for enfant in graphe[noeud] if enfant not in path]

        for noeud_adjacent in noeuds_adjacents:
            if noeud_adjacent == objectif:
                yield path + [noeud_adjacent]
            else:
                stack.append((noeud_adjacent, path + [noeud_adjacent]))

def trouver_instructions(workflow): #à partir du nom d'un workflow, permet de trouver les tests à effectuer pour ce workflow
    for workflow_complet in lignes_workflow :
        #print(f"workflow_complet : {workflow_complet}")
        match1 = re.search(pattern_workflow1, workflow_complet)
        if match1:
            nom_workflow = match1.group(1)
            instructions_workflow = match1.group(2).split(sep=',')
        else:
            print(f"pattern non reconnu pour la ligne {ligne}")
            sys.exit("Ligne non reconnue. Arrêt du programme")
        if nom_workflow == workflow :
            #print(f"le workflow {workflow} a été trouvé dans {workflow_complet}")
            break
    return instructions_workflow

def calculer_combinaisons(chemins):
    liste_dicos = []
    # chemins : [['in', 'qqz', 'hdj', 'A'], ['in', 'qqz', 'hdj', 'pv', 'A'], ['in', 'qqz', 'qs', 'A'], ['in', 'qqz', 'qs', 'lnx', 'A'], ['in', 'qqz', 'qs', 'lnx', 'A'], ['in', 'px', 'A'], ['in', 'px', 'rfg', 'A'], ['in', 'px', 'qkq', 'A'], ['in', 'px', 'qkq', 'crn', 'A']]
    for chemin in chemins :  #['in', 'qqz', 'hdj', 'A'] , le dernier élément étant forcément le "A"
        dico_épreuves = {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}
        combinaisons_chemins = 1
        # {partxmas : [minimum, maximum] } pour réussir (ou échouer le cas échéant) l'épreuve et passer dans le chemin
        for numéro_workflow, nom_workflow in enumerate(chemin[:-1]) : #in    #on ne prend pas le "A"
            instructions_workflow=trouver_instructions(nom_workflow)  #in :  s<1351:px,qqz
            for instruction in instructions_workflow[0:-1] :  #s<1351:px
                catégorie, opérateur, valeur_comparée, workflow_suivant = découpage_instruction(instruction)
                if workflow_suivant ==  chemin[numéro_workflow+1] : #(si le prochain noeud du workflow est le prochain du path ==> il faut réussir la condition)
                    if opérateur == "<" and dico_épreuves[catégorie][1]>valeur_comparée :
                        #pour réussir le test, il faut être plus petit que la valeur donnée pour la catégorie considérée (x, m, a, s)
                        #ie : ce nombre devient le max, sauf si le max actuel est déjà plus bas
                        dico_épreuves[catégorie][1]=valeur_comparée
                        #print(f"on traite le chemin : {chemin}, on en est au workflow {nom_workflow}, le workflow suivant est {workflow_suivant}, les instructions sont {instruction}")
                        #print(f"on veut réussir le test pour que le chemin se fasse, dico pour la catégorie {catégorie}: {dico_épreuves[catégorie]}.")
                        break #pas besoin de faire les autres instructions
                    elif opérateur == ">" and dico_épreuves[catégorie][0]<valeur_comparée : #même principe que précédemment sauf que la valeur donnée devient le min, si elle est plus petite que le min actuel
                        dico_épreuves[catégorie][0] = valeur_comparée
                        #print(f"on traite le chemin : {chemin}, on en est au workflow {nom_workflow}, le workflow suivant est {workflow_suivant}, les instructions sont {instruction}")
                        #print(f"on veut réussir le test pour que le chemin se fasse, dico pour la catégorie {catégorie}: {dico_épreuves[catégorie]}.")
                        break
                elif workflow_suivant != chemin[numéro_workflow+1] : #le prochain noeud du workflow n'est pas celui qu'on cherche ==> il faut échouer le test
                    if opérateur == "<" and dico_épreuves[catégorie][0]<valeur_comparée :
                        #pour rater le test, il faut être plus grand que la valeur demandée pour la catégorie.
                        dico_épreuves[catégorie][0] = valeur_comparée
                        #print(f"on traite le chemin : {chemin}, on en est au workflow {nom_workflow}, le workflow suivant est {workflow_suivant}, les instructions sont {instruction}")
                        #print(f"on veut rater le test pour que le chemin se fasse, dico pour la catégorie {catégorie}: {dico_épreuves[catégorie]}.")
                    elif opérateur == ">" and dico_épreuves[catégorie][1]>valeur_comparée :
                        #pour rater, on doit être plus petit, la valeur devient donc le nouveau max (à condition qu'elle ne soit pas plus grande que le max actuel)
                        dico_épreuves[catégorie][1] = valeur_comparée
                        #print(f"on traite le chemin : {chemin}, on en est au workflow {nom_workflow}, le workflow suivant est {workflow_suivant}, les instructions sont {instruction}")
                        #print(f"on veut rater le test pour que le chemin se fasse, dico pour la catégorie {catégorie}: {dico_épreuves[catégorie]}. ")
        for xmas in dico_épreuves:
            combinaisons_chemins*= (dico_épreuves[xmas][1]-dico_épreuves[xmas][0]+1)
        #print(f"dico épreuves pour le chemin : {chemin} : \n {dico_épreuves} ")
        #print(f"{dico_épreuves} -> {combinaisons_chemins}")
        liste_dicos.append(dico_épreuves)
    print(liste_dicos)
        #print(f"combinaisons : {combinaisons_chemins}")

    return combinaisons_chemins




dico_graphe = {}
rangemax=4000

for workflow_complet in lignes_workflow :
    #print(f"workflow complet : {workflow_complet}")
    workflow_parent, instructions_workflow = recherche_workflow(workflow_complet)   #bpk{a<2727:zzk,s>1544:vc,a>3548:jjn,zbt}
    #partie2 : à partir de la ligne lue, on en retire le nom du workflow parent, ainsi que le bloc d'instructions à passer
    workflows_enfants = []
    for instruction in instructions_workflow[0:-1]:
        catégorie, opérateur, valeur_comparée, workflow_suivant = découpage_instruction(instruction)
        workflows_enfants.append(workflow_suivant)
    workflows_enfants.append(instructions_workflow[-1])
    #print(f"liste workflow enfants pour le workflow complet : {workflow_complet} : {workflows_enfants}")
    création_dictionnaire_graphe(workflow_parent,workflows_enfants)
dico_graphe["A"]=[noeud for noeud in dico_graphe if dico_graphe[noeud]==["A"]]
dico_graphe["R"]=[noeud for noeud in dico_graphe if dico_graphe[noeud]==["R"]]
# les noeuds "A" et "R" sont uniquement liés à leurs "parents"

print(f"dictionnaire graphe : {dico_graphe}")
#dfs_inadapté(dico_graphe, "in" )
chemins = list(trouver_chemin(dico_graphe, 'in', 'A'))
print(f"chemins : {chemins}")
combinaisons_chemins = calculer_combinaisons(chemins)

print(f"réponse : {combinaisons_chemins}")