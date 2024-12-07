import re
# 6391289353235 too low
# 6382287282786 encore plus low mais le code est mieux
# 61561126043536

def execution_jour7_partie1(chemin_fichier):
    lignes=lecture_fichier(chemin_fichier)
    lignes = ["5560244397: 722 77 4 7 37 4 1 3 97"]
    somme_totale = 0
    #for ligne in lignes :
    for num_ligne, ligne in enumerate(lignes): #enumerate pour suivre le num de la ligne traitée à cause de la brute force
        liste_decomposee = pattern(ligne)
        print(liste_decomposee)
        if calcul(liste_decomposee) :  # renvoie True si une combinaison d'opérations renvoie le premier terme
            somme_totale += liste_decomposee[0]
            print(f"ligne n° {num_ligne +1}")
    print(f"La somme totale est : {somme_totale}")


def lecture_fichier(chemin_fichier):
    with open(chemin_fichier, 'r') as fichier:
        contenu = fichier.read()
        lignes = contenu.splitlines()
        return lignes

def pattern(ligne) :
    pattern = re.compile(r"(\d+)+")
    liste_decomposee = pattern.findall(ligne)  #renvoie une liste dont le premier terme est le résultat du calcul cherché et les autres termes sont les composants de ce calcul
    # Exemple : ("21037: 9 7 18 13") renvoie ['21037', '9', '7', '18', '13']
    liste_decomposee = [int(x) for x in liste_decomposee]
    return liste_decomposee

def calcul(liste_nombres) :
    liste_resultats=[liste_nombres[1]] # On initialise une liste, au début elle ne contient que le premier membre de la suite.
    for i in range(2,len(liste_nombres)):
        liste_resultats_figee=liste_resultats.copy() # Evite modification in place, ce qui pose des problèmes sur le for
        print(f"\n\n\nliste (figée) des résultats traités : {liste_resultats_figee}")
        for resultat in liste_resultats_figee :
                resultat_somme = resultat + liste_nombres[i]
                resultat_multiplication = resultat * liste_nombres[i]
                if resultat_somme not in liste_resultats :
                    liste_resultats.append(resultat_somme)
                if resultat_multiplication not in liste_resultats :
                    liste_resultats.append(resultat_multiplication)
                liste_resultats.remove(resultat)  # on n'enlève qu'une seule valeur trouvée. Ainsi, si on a calculé 20 et qu'une valeur 20
                # était déjà dans la liste, on n'enlève que la première, que l'on vient de traiter.
        print(f"A partir de la valeur {resultat} de la liste résultats et du {i}eme membre de la liste des opérations ({liste_nombres[i]}), "
                  f"on obtient deux valeurs : {resultat_somme} (somme) et {resultat_multiplication} (multiplication).\n"
                  f"La liste de résultats (de longueur {len(liste_resultats)}) vaut maintenant : {liste_resultats}.\n")

    return liste_nombres[0] in liste_resultats




