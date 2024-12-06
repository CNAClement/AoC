import re

def execution_jour3_partie1(chemin_fichier):
    contenu = lecture_fichier(chemin_fichier)

    # pattern = re.compile("mul([1-9]{3},[1-9]{3})") #KO, le {3} signifie "exactement 3 chiffres" et pas "entre 1 et 3".
    # De plus, je ne suis pas trop sûr de la façon dont la virgule est prise en compte et les parenthèses ne sont pas prises en compte.
    pattern_mult = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    somme_totale = 0

    instructions_a_traiter = re.findall(pattern_mult, contenu)
    print(instructions_a_traiter)
    for instruction_a_traiter in instructions_a_traiter :
        operande_gauche, operande_droite = recuperation_operandes(instruction_a_traiter)
        resultat = multiplication_operandes(operande_gauche, operande_droite)
        somme_totale += resultat

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
    print(operande_gauche)
    return operande_gauche , operande_droite

def multiplication_operandes(operande_gauche, operande_droite):
    return operande_gauche * operande_droite

