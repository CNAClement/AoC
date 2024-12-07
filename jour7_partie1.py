import re
# 6391289353235 too low

def execution_jour7_partie1(chemin_fichier):
    lignes=lecture_fichier(chemin_fichier)
    somme_totale = 0
    lignes = ["20: 4 5 11"]
    #for ligne in lignes :
    for num_ligne, ligne in enumerate(lignes): #enumerate pour suivre le num de la ligne traitée à cause de la brute force
        #print(f"On traite la ligne n° {num_ligne} : {ligne}")
        liste_decomposee = pattern(ligne)
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
    print(liste_nombres)
    for i in range(2,len(liste_nombres)):
        print(f"On traite la {i}eme occurrence.")
        for resultat in liste_resultats :
            print(f"On traite {resultat}")
            liste_resultats = [res for res in liste_resultats if res != resultat] #on modifie la liste pour enlever le nombre que l'on est en train de traiter
            if resultat < liste_nombres[0] :
                resultat_somme = resultat + liste_nombres[i]
                resultat_multiplication = resultat * liste_nombres[i]
                if resultat_somme not in liste_resultats :
                    liste_resultats.append(resultat_somme)
                if resultat_multiplication not in liste_resultats :
                    liste_resultats.append(resultat_multiplication)
                print(f"A partir de la valeur {resultat} et du {i}eme membre de la liste ({liste_nombres[i]}), "
                      f"on obtient deux valeurs : {resultat_somme} (somme) et {resultat_multiplication} (multiplication).\n"
                      f"La liste de résultats vaut maintenant : {liste_resultats}.\n")
    print(f"{liste_nombres[0] in liste_resultats} ? Avec {liste_nombres[0]} dans {liste_resultats}")
    return liste_nombres[0] in liste_resultats




