def execution_jour2_partie2(chemin_fichier):
    lignes=lecture_fichier(chemin_fichier)
    nombre_reports_safe=0
    for ligne in lignes :
        ligne_entiers=[int(x) for x in ligne.split()]
        print(f"On traite la liste : {ligne_entiers}")
        flag = all_increasing_safe(ligne_entiers, False)
        if flag :
            nombre_reports_safe += 1
            print(f"{ligne_entiers}")

        flag = all_decreasing_safe(ligne_entiers, False)
        if flag :
            nombre_reports_safe += 1
            print(f"{ligne_entiers}")
    print(f"La réponse à la partie 2 (nombre de reports safe) est : {nombre_reports_safe}")


def lecture_fichier(chemin_fichier):
    with open(chemin_fichier, 'r') as fichier:
        contenu = fichier.read()
        lignes = contenu.splitlines()
        return lignes

def all_increasing_safe(sequence, seuil_erreurs_depasse=False):
    # On parcourt tous les membres de la liste. Dès qu'un nombre est plus petit que le précédent
    # ou que la différence est plus grande que 3, on passe le seuil_erreurs à True (ça donne une chance supplémentaire),
    # on ignore le membre de la liste qui pose problème et on re-appelle la fonction avec le paramètre à True.
    # Si une deuxième erreur se produit, on sort en False.
    # Sinon, on sort en True à la fin de la boucle.

    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            if seuil_erreurs_depasse==False:
                # On teste en supprimant le nombre de droite, [89, 92, 95] devient [89, 95]
                sequence_droite = sequence[:i+1] + sequence[i+2:]
                # On teste en supprimant le nombre de gauche, [89, 92, 95] devient [92, 95]
                sequence_gauche = sequence[:i] + sequence[i+1:]
                # Si l'un des deux tests est True, alors on sort en True, sinon False
                return (all_increasing_safe(sequence_droite, True) or all_increasing_safe(sequence_gauche, True))
            else :
                return False
        if (sequence[i+1]-sequence[i])>3:
            if seuil_erreurs_depasse==False:
                # On teste en supprimant le nombre de droite, [89, 92, 95] devient [89, 95]
                sequence_droite = sequence[:i+1] + sequence[i+2:]
                # On teste en supprimant le nombre de gauche, [89, 92, 95] devient [92, 95]
                sequence_gauche = sequence[:i] + sequence[i+1:]
                # Si l'un des deux tests est True, alors on sort en True, sinon False
                return (all_increasing_safe(sequence_droite, True) or all_increasing_safe(sequence_gauche, True))
            else :
                return False
    #print(f"Croissance stricte et safe pour la liste {sequence}.")
    return True

def all_decreasing_safe(sequence, seuil_erreurs_depasse=False):
    # On parcourt tous les membres de la liste. Dès qu'un nombre est plus grand que le précédent
    # ou que la différence est plus grande que 3, on passe le seuil_erreurs à True (ça donne une chance supplémentaire),
    # on ignore le membre de la liste qui pose problème et on re-appelle la fonction avec le paramètre à True.
    # Si une deuxième erreur se produit, on sort en False.
    # Sinon, on sort en True à la fin de la boucle.

    for i in range(len(sequence) - 1):
        if sequence[i] <= sequence[i + 1]:
            if seuil_erreurs_depasse==False:
                # On teste en supprimant le nombre de droite, [89, 92, 95] devient [89, 95]
                sequence_droite = sequence[:i+1] + sequence[i+2:]
                # On teste en supprimant le nombre de gauche, [89, 92, 95] devient [92, 95]
                sequence_gauche = sequence[:i] + sequence[i+1:]
                # Si l'un des deux tests est True, alors on sort en True, sinon False
                return (all_decreasing_safe(sequence_droite, True) or all_decreasing_safe(sequence_gauche, True))
            else :
                return False
        if (sequence[i]-sequence[i+1])>3:
            if seuil_erreurs_depasse==False:
                # On teste en supprimant le nombre de droite, [89, 92, 95] devient [89, 95]
                sequence_droite = sequence[:i+1] + sequence[i+2:]
                # On teste en supprimant le nombre de gauche, [89, 92, 95] devient [92, 95]
                sequence_gauche = sequence[:i] + sequence[i+1:]
                # Si l'un des deux tests est True, alors on sort en True, sinon False
                return (all_decreasing_safe(sequence_droite, True) or all_decreasing_safe(sequence_gauche, True))
            else :
                return False
    #print(f"Décroissance stricte et safe pour la liste {sequence}.")
    return True




