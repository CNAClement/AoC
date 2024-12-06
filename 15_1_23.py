import re
import sys
import time
import numpy as np
with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\15_1_ori.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")
start=time.time()

sequence_initialisation = contenu.split(sep=',')
pattern = re.compile("^([a-z]+)(=|-)(\d*)$")

def traduction_sequence(sequence):
    match = re.search(pattern, sequence)
    if match:
        label = match.group(1)
        operation = match.group(2)
        focale_string = match.group(3)
        if focale_string:
            focale=int(focale_string)
        else : focale = None
        # print(f"séquence : {sequence}, groupe1 : {label}, groupe2 : {operation} , groupe3 : {focale}")
    else:
        print(f"pas de match pour la séquence : {sequence}")
        sys.exit("Pas de match. Arrêt du programme")
    return label, operation, focale

def algo_hash(sequence):
    hash=0
    valeur_actuelle = 0
    for caractere in sequence:
        code_asci=ord(caractere)
        valeur_actuelle+=code_asci
        valeur_actuelle*=17
        valeur_actuelle=valeur_actuelle%256
    #print(f"hash total : {valeur_actuelle}")
    return valeur_actuelle

def remplir_boite(label,operation,focale, boite ):
    if operation == "-":
        index_a_supprimer = next((i for i, tup in enumerate(boite) if tup[0] == label), None)
        if index_a_supprimer is not None :
            boite.pop(index_a_supprimer) #pop supprime un élément d'une liste en fonction de son index, contrairement à remove qui supprime en fonction de sa value
    if operation == "=":
        index_a_verifier = next((i for i, tup in enumerate(boite) if tup[0] == label), None)
        if index_a_verifier is not None :
            boite[index_a_verifier]=(label,focale)
        else :
            boite.append((label,focale))
    return boite


def puissance_focale(boites):
    puissance_focale_totale = 0  # reponse partie 2
    for numéro_boite, boite in enumerate(boites):
        puissance_focale_boite = 0
        if boite != []:
            print(f"boite numéro {numéro_boite} : {boite}")
            for numero_lentille in range(len(boite)):
                puissance_focale_lentille=(1+numéro_boite)*(1+numero_lentille)*boites[numéro_boite][numero_lentille][1]
                print(f"puissance focale lentille = {puissance_focale_lentille}")
                puissance_focale_boite+=puissance_focale_lentille
                #print(f"puissance focale boite = {puissance_focale_boite}")
        puissance_focale_totale+=puissance_focale_boite
    return puissance_focale_totale

boites = [[] for _ in range(256)]
reponse_partie_1=0
for sequence in sequence_initialisation:
    print(f"séquence traitée : {sequence}")
    label, operation, focale = traduction_sequence(sequence)
    #print(f"label : {label}, opération de type : {operation} et focale : {focale}")
    numero_boite=algo_hash(label)
    #print(f"numéro de boite (hash du label) : {numero_boite}")
    boites[numero_boite]=remplir_boite(label, operation, focale, boites[numero_boite])
puissance_focale_totale=puissance_focale(boites)
    #reponse_partie_1+=valeur_actuelle

print(f"la réponse à la partie 2 est : {puissance_focale_totale} en {time.time()-start} secondes")