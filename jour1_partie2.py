def execution_jour1_partie2(chemin_fichier):
    with open(chemin_fichier, 'r') as fichier:
        contenu = fichier.read()
        lignes = contenu.splitlines()

    ligne = [ligne.split() for ligne in lignes]
    # On obtient une liste de listes, chaque élément de la "grande liste" étant une liste de deux éléments.
    # ligne = [['3', '4'], ['4', '3'], ['2', '5'], ['1', '3'], ['3', '9'], ['3', '3']]

    score_similarite_total=0
    for i in range(len(ligne)):
        #print(f"on cherche la similarité de l'élément {ligne[i][0]}")
        indice_similarite=0
        for j in range(len(ligne)):
            if ligne[i][0]==ligne[j][1]:
                indice_similarite+=1
        score_similarite=indice_similarite*int(ligne[i][0])
        #print(f"L'indice de similarité est : {indice_similarite}, pour un score de similarité de : {score_similarite}")
        score_similarite_total+=score_similarite

    print(f"le score de similarité total est : {score_similarite_total}")