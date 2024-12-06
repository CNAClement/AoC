# 29233045 too low
187194524
import re

def execution_jour3_partie2(chemin_fichier):
    contenu = lecture_fichier(chemin_fichier)
    traitement_enabled = True

    # On recherche les motifs de type "mul(23,4)" ou ( | )  de type "do()" ou de type "don't()"
    pattern_mult = re.compile(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))")
    somme_totale = 0

    instructions_a_traiter = re.findall(pattern_mult, contenu)
    print(f"Liste des instructions : {instructions_a_traiter}.")
    for instruction_a_traiter in instructions_a_traiter :
        print(f"On traite l'instruction {instruction_a_traiter}. Le flag enabled est : {traitement_enabled}")
        if instruction_a_traiter == "do()" :
            traitement_enabled = True
        elif instruction_a_traiter == "don't()" :
            traitement_enabled = False
        elif traitement_enabled == True :
        # (si l'instruction à traiter n'est pas de type "do()" ou "don't()", elle est de type mul(x,y) et on
        # ne la traite que si le flag traitement_enabled est déjà à True, sinon on ne fait rien.
            operande_gauche, operande_droite = recuperation_operandes(instruction_a_traiter)
            resultat = multiplication_operandes(operande_gauche, operande_droite)
            somme_totale += resultat
        else :
            continue

    print(f"Somme totale : {somme_totale}")




def lecture_fichier(chemin_fichier):
    with open(chemin_fichier, 'r') as fichier:
        contenu = fichier.read()
        return contenu


def recuperation_operandes(chaine):
    # A partir d'une chaine comme mul(2,4), on veut récupérer deux chiffres : 2 et 4 et les stocker dans deux variables distinctes.
    pattern_operandes = re.compile("\((\d{1,3}),(\d{1,3})\)")
    match = re.search(pattern_operandes, chaine)

    if match :
        operande_gauche = int(match.group(1))
        operande_droite = int(match.group(2))
    else :
        print(f"Problème de match sur la chaine {chaine}")
    return operande_gauche , operande_droite

def multiplication_operandes(operande_gauche, operande_droite):
    return operande_gauche * operande_droite

