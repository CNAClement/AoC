with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2016\6_1.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes=contenu.splitlines()

print(lignes)
print(f"{len(lignes)} lignes pour une longueur totale de {len(contenu)}")

lettres_finales =""

taille_de_ligne = len(lignes[0])
for numero_ligne in range(len(lignes)):
    if len(lignes[numero_ligne]) != taille_de_ligne:
        print(f"il y a un problème de taille : au moins une ligne n'est pas de la même longueur que la 1ere.\nTaille de la première ligne : {taille_de_ligne}, taille de la ligne KO (en position {numero_ligne}) : {len(lignes[numero_ligne])} ")


for position in range(taille_de_ligne):
    lettre_frequence = []
    compteur_lettres = [["a", 0], ["b", 0], ["c", 0], ["d", 0], ["e", 0], ["f", 0], ["g", 0], ["h", 0], ["i", 0],
                        ["j", 0], ["k", 0], ["l", 0], ["m", 0], ["n", 0], ["o", 0], ["p", 0], ["q", 0], ["r", 0],
                        ["s", 0], ["t", 0], ["u", 0], ["v", 0], ["w", 0], ["x", 0], ["y", 0], ["z", 0]]
    for numero_ligne in range(len(lignes)):
        equivalence_lettre_num = ord(lignes[numero_ligne][position]) - ord('a')
        #print(f"lettre : {lignes[numero_ligne][position]} , ce qui correspond au numéro : {equivalence_lettre_num} " )
        compteur_lettres[equivalence_lettre_num][1]+=1
    lettre_frequence+=sorted(compteur_lettres, key=lambda x: -x[1])[0]
    #print(f"la lettre la plus fréquente sur la position {position+1} avec son nombre d'occurrences est : {lettre_frequence}")
    lettres_finales+=str(lettre_frequence[0])

print(f"lettres finales : {lettres_finales}")

