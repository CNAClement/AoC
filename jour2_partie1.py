def execution_jour2_partie1(chemin_fichier):
    lignes=lecture_fichier(chemin_fichier)
    nombre_reports_safe=0
    for ligne in lignes :
        ligne_entiers=[int(x) for x in ligne.split()]
        print(f"On traite la liste : {ligne_entiers}")
        flag = all_increasing_safe(ligne_entiers)
        if flag :
            nombre_reports_safe += 1
            print(ligne_entiers)
        flag = all_decreasing_safe(ligne_entiers)
        if flag :
            nombre_reports_safe += 1
            print(ligne_entiers)
    print(f"La réponse à la partie 1 (nombre de reports safe) est : {nombre_reports_safe}")


def lecture_fichier(chemin_fichier):
    with open(chemin_fichier, 'r') as fichier:
        contenu = fichier.read()
        lignes = contenu.splitlines()
        return lignes

def all_increasing_safe(sequence):
    # On parcourt tous les membres de la liste. Dès qu'un nombre est plus petit que le précédent
    # ou que la différence est plus grande que 3, on sort immédiatement en False
    # sinon, on sort en True à la fin de la boucle.

    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            #print(f"Pas de croissance stricte : {sequence[i+1]} est plus petit que {sequence[i]} (positions {i+1} et {i+2} de la liste)")
            return False
        if (sequence[i+1]-sequence[i])>3:
            #print(f"Croissance trop rapide entre les positions {i} et {i+1} de valeurs respectives {sequence[i]} et {sequence[i+1]} (écart {int(sequence[i+1]) - int(sequence[i])} ) ")
            return False
    #print(f"Croissance stricte et safe pour la liste {sequence}.")
    return True

def all_decreasing_safe(sequence):
    # On parcourt tous les membres de la liste. Dès qu'un nombre est plus grand que le précédent
    # ou que la différence est plus grande que 3, on sort immédiatement en False
    # sinon, on sort en True à la fin de la boucle.
    for i in range(len(sequence) - 1):
        if sequence[i] <= sequence[i + 1]:
            print(f"Pas de décroissance stricte : {sequence[i + 1]} est plus grand que {sequence[i]} (positions {i + 1} et {i + 2} de la liste)")
            return False
        if (sequence[i]-sequence[i+1])>3:
            print(f"Décroissance trop rapide entre les positions {i} et {i + 1} de valeurs respectives {sequence[i]} et {sequence[i + 1]} (écart {int(sequence[i])-int(sequence[i+1])} ) ")
            return False
    print(f"Décroissance stricte et safe pour la liste {sequence}.")
    return True




