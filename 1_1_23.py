numero_question=2  #54194 incorrect
with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\1_1.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes=contenu.splitlines()

dictionnaire = dict([("1", "one"), ("2", "two"), ("3", "three"), ("4", "four"), ("5", "five"), ("6", "six"), ("7", "seven"), ("8", "eight"), ("9","nine")])
liste_chiffres = []
reponse = 0


def somme_question(chaine_a_sommer): #récupère un groupe de nombres et les somme (exemple : 11, 15, 15, 20 ==> 61 )
    somme=0
    for nombre in chaine_a_sommer:
        somme+=int(nombre)
    return somme

def dictionnaire_replace(chaine) :  #remplace les chiffres écrits en lettres par des digits (exemple : "two" --> 2 )
    #ne sera plus utilisé (ne répond pas parfaitement au problème)
    for key, value in dictionnaire.items():
        chaine=chaine.replace(value,key)
    return chaine

def dictionnaire_cherche_position_insere_digit(chaine) :  #recherche un chiffre écrit en lettre dans la chaine, et retourne la position, puis insère un digit après cette position
    flag_chaine_trouvee = 0
    for key, value in dictionnaire.items(): #on recherche toutes les valeurs. Si plusieurs résultats, on ne renverra que le dernier trouvé :
        #ce n'est pas grave puisque on va appeler la fonction en boucle tant qu'elle trouve des choses
        #A moins que ça marche complètement dès le premier passage puisque c'est la chaine d'entrée qui est directement modifiée à chaque passage de la boucle
        if value in chaine :
            print(f"chaine trouvée : {value} dans {chaine}")
            flag_chaine_trouvee=1
            print(f"key : {key}")
            print(f"value : {value}")
            position=chaine.find(value)
            print(f"position : {position}")
            chaine="{}{}{}".format(chaine[:position+1],key,chaine[position+1:])
            #on insère un digit juste après le premier caractère de la chaine, de façon à "casser" le mot tout en le traitant (puisque le digit apparait)
            #et sans risquer de casser un éventuel mot suivant imbriqué (exemple : "eightwo" ) puisqu'aucun mot ne fait 2 caractères ou moins.
    return chaine, flag_chaine_trouvee

lignes_corrigees=lignes.copy()
for ligne in range(len(lignes_corrigees)):
    test_mot_chiffre=""
    flag_chaine_trouvee=1 #on initialise le flag pour rentrer au moins une fois dans le while
    while flag_chaine_trouvee==1:
        lignes_corrigees[ligne], flag_chaine_trouvee =dictionnaire_cherche_position_insere_digit(lignes_corrigees[ligne])

print(lignes)
print(f"{len(lignes)} lignes pour une longueur totale de {len(contenu)}")
print(f"lignes corrigées : {lignes_corrigees}")

def reponse_question(numero_question):
    liste_chiffres = []
    if numero_question == 1 :
        chaines=lignes
    elif numero_question ==2 :
        chaines=lignes_corrigees
    for ligne in range(len(chaines)):
        #print(f"ligne traitée : {chaines[ligne]}\nc'est la ligne n° {ligne+1}, de longueur {len(chaines[ligne])}")
        index = 0
        duo_chiffre=""
        for caractere in range(len(chaines[ligne])):
            caractere=chaines[ligne][index]
            if caractere.isdigit() == False:
                index+=1
            else:
                duo_chiffre += caractere
                break

        index = len(chaines[ligne])-1
        for caractere in range(len(chaines[ligne])):
            caractere=chaines[ligne][index]
            if caractere.isdigit() == False:
                index-=1
            else:
                duo_chiffre += caractere
                break
        liste_chiffres+=[duo_chiffre]

    print(f"liste chiffres : {liste_chiffres}")
    reponse = somme_question(liste_chiffres)
    return reponse


print(f"la réponse à la question est : {reponse_question(numero_question)}")

