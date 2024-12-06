import numpy as np

with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2016\3_1_ori.txt', 'r') as fichier :
        contenu = fichier.read()
        ligne = contenu.splitlines()
        compteur=0

print(contenu)

for indice in range(len(ligne)):
    triangle = [int(triangle_char) for triangle_char in ligne[indice].split()] #on prend une ligne du fichier. Triangle_char est le triplet correspondant, puis on convertit en numérique.
    triangle_tri=sorted(triangle)
    if triangle_tri[0]+triangle_tri[1]<triangle_tri[2]:
        a=1 #print(f"le triangle {triangle} à la ligne {indice+1} n'est pas valide")
    elif triangle_tri[0]+triangle_tri[1]==triangle_tri[2]:
        print(f"le triangle {triangle} à la ligne {indice + 1} est plat ")
    else :
        compteur+=1

print(f"le nombre de triangles valides est {compteur}")