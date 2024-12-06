import re
import sys
import time
with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\9_1_ori.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")

def vecteur_par_difference(ligne_split):
    nouveau_vecteur=[""]*(len(ligne_split)-1)
    for index in range(len(ligne_split)-1):
        nouveau_vecteur[index]=int(ligne_split[index+1])-int(ligne_split[index])
    return nouveau_vecteur

def calcul_partie1(ligne_split,reponse_exercice1):
    liste_vecteurs=[]
    indice=0
    while ligne_split != [0]*len(ligne_split):
        liste_vecteurs.append(ligne_split+["0"])
        indice+=1
        #print(f"liste vecteurs après : {liste_vecteurs}")
        ligne_split=vecteur_par_difference(ligne_split)
    liste_vecteurs.append([0]*(len(ligne_split)+1))
    for indice in range(len(liste_vecteurs)-2,-1,-1): #on commence à longueur de vecteur -2 (pour ne pas prendre en compte celui plein de 0)  et on descend de 1 en 1 jusqu'à -1 sans l'inclure (donc jusqu'à 0)
        liste_vecteurs[indice][-1]=int(liste_vecteurs[indice][-2])+int(liste_vecteurs[indice+1][-1])
    #print(liste_vecteurs)
    reponse_exercice1+=liste_vecteurs[0][-1]
    return reponse_exercice1

def calcul_partie2(ligne_split,reponse_exercice2):
    liste_vecteurs=[]
    indice=0
    while ligne_split != [0]*len(ligne_split):
        liste_vecteurs.append(["0"]+ligne_split)
        indice+=1
        ligne_split=vecteur_par_difference(ligne_split)
    liste_vecteurs.append([0]*(len(ligne_split)+1))
    for indice in range(len(liste_vecteurs)-2,-1,-1): #on commence à longueur de vecteur -2 (pour ne pas prendre en compte celui plein de 0)  et on descend de 1 en 1 jusqu'à -1 sans l'inclure (donc jusqu'à 0)
        liste_vecteurs[indice][0]=int(liste_vecteurs[indice][1])-int(liste_vecteurs[indice+1][0])
    print(liste_vecteurs)
    reponse_exercice2+=liste_vecteurs[0][0]
    return reponse_exercice2

reponse_exercice1=0
reponse_exercice2=0
for ligne in lignes :
    ligne_split=ligne.split()
    reponse_exercice1=calcul_partie1(ligne_split,reponse_exercice1)
    reponse_exercice2=calcul_partie2(ligne_split,reponse_exercice2)


print(f"la réponse à la partie 1 est : {reponse_exercice1} et la réponse à la partie 2 est {reponse_exercice2}")






