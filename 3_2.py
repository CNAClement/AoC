# L = [("a",2),("b",3)]
# print(L[0])
#
# result = []
# record[0] for record in L if record[1] > 2
#
# print(result)


import numpy as np

with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2016\3_1_ori.txt', 'r') as fichier:
    contenu = fichier.read()
    ligne = contenu.splitlines()

print(f"lignes 1 à 3 : {ligne[0:3]} ")
print(f"longueur de la ligne : {len(ligne)}")

# ligne = c'est une liste de n éléments rangés 3 par 3 (exemple : ligne[1] vaut 572  189  424 ).
# On va chercher à la découper pour en faire une liste avec chaque élément séparé (ligne[0] vaudra 883, ligne[3] vaudra 572 ) .
# Problème : on ne peut pas appliquer la méthode split() à une liste ( ligne.split() ==> abend), uniquement à ses éléments (ligne[n].split() ==> 3 valeurs).
# On va donc faire varier n de 0 à len(liste)-1 et pour chacun de ces groupes, appliquer la méthode split pour obtenir des valeurs découpées.

valeurs_decoupees = []
for groupe in ligne:
    decoupage_valeur = [valeur for valeur in groupe.split()]
    valeurs_decoupees.extend(decoupage_valeur)

# print(valeurs_decoupees[0])
# print(f"valeurs découpées : {valeurs_decoupees}")
print(f"nombre de valeurs uniques : {len(valeurs_decoupees)}")

tableau_1d = np.array(valeurs_decoupees)
tableau_2d = tableau_1d.reshape(int(len(valeurs_decoupees) / 3), 3)
print(f"3 premières lignes du tableau 2d obtenu : \n {tableau_2d[0:3]}")
print(f"nombre de dimensions du tableau : {tableau_2d.ndim}")
print(f"1ere ligne 2eme colonne du tableau : {tableau_2d[0][1]}")
print(f"2eme ligne 1ere colonne du tableau : {tableau_2d[1][0]}")
print(f"nombre de lignes du tableau 2d: {tableau_2d.shape[0]}, nombre de colonnes : {tableau_2d.shape[1]} ")

# on va maintenant créer un tableau en 3 dimensions en groupant les valeurs 3 par 3 du tableau 2d

nombre_lignes_tableau_3d = int(tableau_2d.shape[0] / 3)
tableau_3d = np.zeros((nombre_lignes_tableau_3d, tableau_2d.shape[1]), dtype=object)

for colonne in range(tableau_2d.shape[1]):
    for ligne in range(nombre_lignes_tableau_3d):
        tableau_3d[ligne][colonne] = sorted(
            [int(tableau_2d[3 * ligne][colonne]), int(tableau_2d[3 * ligne + 1][colonne]), int(tableau_2d[3 * ligne + 2][colonne])])

# print(f"3 premières lignes du tableau 3d obtenu : \n {tableau_3d[0:3]}")

print(f"2eme ligne du tableau 3D: {tableau_3d[1]}")
print(f"2eme ligne 1ere colonne du tableau 3D: {tableau_3d[1][0]}")
print(f"2eme ligne 1ere colonne 1ere valeur du tableau 3D: {tableau_3d[1][0][0]}")
print(f"nombre de lignes du tableau 3d: {tableau_3d.shape[0]}, nombre de colonnes : {tableau_3d.shape[1]} ")

compteur = 0
compteur_invalides = 0
tableau_3d_binaire = tableau_3d.copy()


for colonne in range(tableau_3d.shape[1]):
    for ligne in range(nombre_lignes_tableau_3d):
        if int(tableau_3d[ligne][colonne][0]) + int(tableau_3d[ligne][colonne][1]) > int(tableau_3d[ligne][colonne][2]):
            tableau_3d_binaire[ligne][colonne] = 1
            compteur += 1
        else:
            tableau_3d_binaire[ligne][colonne] = 0
            compteur_invalides+=1
            print(f"Triangle invalide : {tableau_3d[ligne][colonne]} autour de la ligne {(ligne + 1) * 3} du fichier en entrée (colonne {colonne + 1} )")

print(f"nombre de triangles valides : {compteur}")
print(f"nombre de triangles invalides : {compteur_invalides}")

print(f"3 premières lignes du tableau binaire obtenu : \n {tableau_3d_binaire[0:3]}")
