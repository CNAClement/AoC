import re
import sys
import time
import numpy as np
from itertools import product

with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\12_1.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")

partie="partie2"
#patterns = re.compile("^[#]+\.|\.[#]+\.|\.[#]+$")
patterns = re.compile("[#]+")
start = time.time()
def trouver_emplacements_suspects(ligne):
    emplacements_suspects = []
    #print(f"ligne traitée : {ligne}")
    for index, caractere in enumerate(ligne) :
        if caractere == "?":
            emplacements_suspects.append(index)
    return emplacements_suspects


def generer_vecteurs_possibles(vecteur_entrée, emplacements_suspects):
    #print(f"vecteur en entrée : {vecteur_entrée}, emplacements à modifier : {emplacements_suspects}")
    combinaisons_possibles = product(["#", "."], repeat=len(emplacements_suspects)) #s'il y a 4 "?" , on peut répéter jusqu'à 4 fois "#" ou "."
    vecteurs_possibles = []
    for combinaison in combinaisons_possibles:
        #print(f"combinaison traitée : {combinaison}")
        vecteur_modifié = vecteur_entrée.copy()
        #print(f"vecteur modifié avant : {vecteur_modifié[0]}")
        for indice, valeur in zip(emplacements_suspects, combinaison):
            #print(f"position modifiée  : {indice}, valeur = {valeur} ")
            vecteur_modifié[0] = vecteur_modifié[0][:indice] + valeur + vecteur_modifié[0][indice+1:] #on modifie la première partie du vecteur, c'est-à-dire celle qui contient les motifs

            #print(f"vecteur modifié après : {vecteur_modifié[0]}")
        vecteurs_possibles.append(vecteur_modifié)
    return vecteurs_possibles

def tester_pertinence_vecteur(vecteurs_possibles):
    combinaisons_ok = 0
    for vecteur in vecteurs_possibles:
        if vecteur[0] != "."*len(vecteur[0]):
            motifs_trouves = re.findall(patterns, vecteur[0])
            if motifs_trouves :
                resultats_obtenus = [int(num) for num in vecteur[1].split(',')]
                nombre_casses_consecutifs = [motif.count('#') for motif in motifs_trouves]
                #print(f"on traite le vecteur : {vecteur[0]}, on a {nombre_casses_consecutifs} nombres consécutifs, on cherche le résultat : {resultats_obtenus} sur les motifs {motifs_trouves}")
                if nombre_casses_consecutifs == resultats_obtenus:
                    combinaisons_ok+=1
            else:
                print(f"Aucun match trouvé {vecteur[0]}")
                sys.exit("Abend: Aucun match trouvé. Arrêt du programme.")
        else : #print(f"vecteur full '.' : {vecteur}")
                continue
    return combinaisons_ok

def ajout_suspect_debut(vecteurs_entrée) :
    #print(f"vecteur en entrée : {vecteurs_entrée}")
    vecteurs_entrée_inc = vecteurs_entrée.copy()
    if vecteurs_entrée_inc[0][-1]!= "#" :
        vecteurs_entrée_inc[0]="?"+vecteurs_entrée_inc[0]
    #print(f"vecteurs entrée inc après ajout début  : {vecteurs_entrée_inc}")
    return vecteurs_entrée_inc

def ajout_suspect_fin(vecteurs_entrée) :
    #print(f"vecteur en entrée : {vecteurs_entrée}")
    vecteurs_entrée_inc = vecteurs_entrée.copy()
    if vecteurs_entrée_inc[0][0]!= "#" :
        vecteurs_entrée_inc[0]+="?"
    #print(f"vecteurs entrée après ajout fin : {vecteurs_entrée_inc}")
    return vecteurs_entrée_inc

def tester_impact_ajout(vecteur_entrée, vecteur_entrée_inc_deb,vecteur_entrée_inc_fin):
    #print(f"ajout avant : {vecteur_entrée_inc_deb}, ajout après : {vecteur_entrée_inc_fin}")
    combinaisons_ok_ligne = 0
    emplacements_suspects = trouver_emplacements_suspects(vecteur_entrée[0])
    emplacements_suspects_inc_deb = trouver_emplacements_suspects(vecteur_entrée_inc_deb[0])
    emplacements_suspects_inc_fin = trouver_emplacements_suspects(vecteur_entrée_inc_fin[0])
    print(f" emplacements suspects début : {emplacements_suspects_inc_deb}, emplacements suspects fin : {emplacements_suspects_inc_fin}")
    vecteurs_possibles = generer_vecteurs_possibles(vecteur_entrée, emplacements_suspects)
    vecteurs_possibles_inc_deb = generer_vecteurs_possibles(vecteur_entrée_inc_deb, emplacements_suspects_inc_deb)
    vecteurs_possibles_inc_fin = generer_vecteurs_possibles(vecteur_entrée_inc_fin, emplacements_suspects_inc_fin)
    print(f"combinaisons base : {vecteurs_possibles} ")
    nombre_combinaisons1 = tester_pertinence_vecteur(vecteurs_possibles)
    print(f"combinaisons début : {vecteurs_possibles_inc_deb} ")
    nombre_combinaisons_deb = tester_pertinence_vecteur(vecteurs_possibles_inc_deb)
    print(f"combinaisons fin : {vecteurs_possibles_inc_fin} ")
    nombre_combinaisons_fin = tester_pertinence_vecteur(vecteurs_possibles_inc_fin)
    print(f"combinaisons initiales : {nombre_combinaisons1}, avec ajout '?' au début : {nombre_combinaisons_deb}, avec ajout '?' à la fin : {nombre_combinaisons_fin}")
    if  nombre_combinaisons1 == nombre_combinaisons_deb and nombre_combinaisons1 == nombre_combinaisons_fin :
        combinaisons_ok_ligne = nombre_combinaisons1**5
    else :  combinaisons_ok_ligne = nombre_combinaisons1*max(nombre_combinaisons_deb, nombre_combinaisons_fin)**4
    #elif nombre_combinaisons1 == nombre_combinaisons_deb and nombre_combinaisons1 != nombre_combinaisons_fin :
    #    combinaisons_ok_ligne = nombre_combinaisons1*nombre_combinaisons_fin**4
    #elif nombre_combinaisons1 != nombre_combinaisons_deb and nombre_combinaisons1 == nombre_combinaisons_fin :
    #    combinaisons_ok_ligne = nombre_combinaisons1*nombre_combinaisons_deb**4
    #elif nombre_combinaisons1 != nombre_combinaisons_deb and nombre_combinaisons1 != nombre_combinaisons_fin :
    #    print("aie aie aie")
    #print(f"combinaisons sur le vecteur traité : {combinaisons_ok_ligne} ")
    return combinaisons_ok_ligne




combinaisons_ok = 0
for ligne in lignes :
    if partie == "partie1" :
        print(f"on traite la ligne : {ligne}")
        emplacements_suspects = trouver_emplacements_suspects(ligne)
        print(f"emplacements suspects : {emplacements_suspects}")
        vecteur_entrée=ligne.split() #on créé une liste, premier élément : le motif modifiable (avec les "?" , ".", "#" ), deuxième élément : le motif attendu
        vecteurs_possibles = generer_vecteurs_possibles(vecteur_entrée, emplacements_suspects)
        print(f"vecteurs possibles : {vecteurs_possibles}")
        combinaisons_ok_ligne = tester_pertinence_vecteur(vecteurs_possibles)
        combinaisons_ok += combinaisons_ok_ligne
    elif partie == "partie2" :
        vecteur_entrée=ligne.split() #on créé une liste, premier élément : le motif modifiable (avec les "?" , ".", "#" ), deuxième élément : le motif attendu
        print(f"on traite le vecteur : {vecteur_entrée}")
        vecteur_entrée_inc_deb = ajout_suspect_debut(vecteur_entrée)
        vecteur_entrée_inc_fin = ajout_suspect_fin(vecteur_entrée)
        combinaisons_ok_ligne=tester_impact_ajout(vecteur_entrée, vecteur_entrée_inc_deb , vecteur_entrée_inc_fin )
        combinaisons_ok += combinaisons_ok_ligne
        print(combinaisons_ok_ligne)

print(f"la réponse à la {partie} est : {combinaisons_ok}, durée = {time.time()-start}")


