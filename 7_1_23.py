#250877377 too low (part2)
import re
import time
with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\7_1_ori.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")

start=time.time()
partie="partie2" #partie1 ou partie2, indique exercice à traiter

if partie=="partie1":
    ordre_carte="AKQJT98765432"
elif partie == "partie2":
    ordre_carte="AKQT98765432J"
else :
    print(f"la partie {partie} n'existe pas, c'est soit partie1 soit partie2")


def parsing(ligne) :
    pattern = re.compile(r'^([0-9a-zA-Z]{5}) (\d+)$')
    match = re.search(pattern, ligne)
    if match:
        main = match.group(1)
        bid = match.group(2)
        #print(f"Main : {main}, bid: {bid}")
    else:
        print("Aucune correspondance")
    return main, bid

def arrangement_main(main,bid) :
    main_triee=[0]*15 #le 14eme emplacement est pour le bid et le 15emetype de main
    for carte in main:
        main_triee[ordre_carte.index(carte)]+=1
    main_triee[13]=bid
    return main_triee

def type_main_partie1(main_incr,main_triee) :
        nombre_max=0
        for carte in range(13):
            if int(main_triee[carte])>nombre_max:
                nombre_max=int(main_triee[carte])
                carte_principale=carte
        #print(f"nombre max : {nombre_max} et carte principale : {carte_principale}")
        if nombre_max==5:
            main_triee[14]=1
            main_incr[2]=1
        elif nombre_max==4:
            main_triee[14]=2
            main_incr[2]=2
        elif nombre_max==3:
            nombre_max_secondaire=0
            for carte in range(13):
                if carte!=carte_principale:
                    if int(main_triee[carte]) > nombre_max_secondaire:
                        nombre_max_secondaire = int(main_triee[carte])
            if nombre_max_secondaire==2:
                main_triee[14]=3
                main_incr[2] = 3
            else :
                main_triee[14]=4
                main_incr[2] = 4
        elif nombre_max == 2:
            nombre_max_secondaire = 0
            for carte in range(13):
                if carte!=carte_principale:
                    if int(main_triee[carte]) > nombre_max_secondaire:
                        nombre_max_secondaire = int(main_triee[carte])
                if nombre_max_secondaire == 2:
                    main_triee[14] = 5
                    main_incr[2] = 5
                else:
                    main_triee[14] = 6
                    main_incr[2] = 6
        elif nombre_max == 1:
            main_triee[14]=7
            main_incr[2]=7
        else : print(f"vérifier la main, elle n'est d'aucun type : {main_triee}")
        return main_incr, main_triee


def type_main_partie2(main_incr, main_triee):
    nombre_max = 0
    for carte in range(0,12):  #on ne va pas compter les J , on les ajoutera ensuite au nombre_max trouvé sans les J
        if int(main_triee[carte]) > nombre_max :
            nombre_max = int(main_triee[carte])
            carte_principale = carte
    #print(f"main triee : {main_triee}")
    #print(f"nombre de jokers : {main_triee[12]}")

    # print(f"nombre max : {nombre_max} et carte principale : {carte_principale}")
    if nombre_max + int(main_triee[12] ) == 5:
        main_triee[14] = 1
        main_incr[2] = 1
    elif nombre_max + int(main_triee[12] )  == 4:
        main_triee[14] = 2
        main_incr[2] = 2
    elif nombre_max + int(main_triee[12] )  == 3:
        nombre_max_secondaire = 0
        for carte in range(12):
            if carte != carte_principale:
                if int(main_triee[carte]) > nombre_max_secondaire:
                    nombre_max_secondaire = int(main_triee[carte])
        if nombre_max_secondaire == 2:
            main_triee[14] = 3
            main_incr[2] = 3
        else:
            main_triee[14] = 4
            main_incr[2] = 4
    elif nombre_max + int(main_triee[12] )  == 2:
        nombre_max_secondaire = 0
        for carte in range(12):
            if carte != carte_principale:
                if int(main_triee[carte]) > nombre_max_secondaire:
                    nombre_max_secondaire = int(main_triee[carte])
            if nombre_max_secondaire == 2:   #le Joker ne doit jamais permettre de faire une double paire : si on avait déjà une paire, il fait un triple. Si on n'avait aucune paire et deux jokers, il fait un triple aussi.
                main_triee[14] = 5
                main_incr[2] = 5
            else:
                main_triee[14] = 6
                main_incr[2] = 6
    elif nombre_max == 1:
        main_triee[14] = 7
        main_incr[2] = 7
    else:
        print(f"vérifier la main, elle n'est d'aucun type : {main_triee}, {main_triee[12]}, {nombre_max}")
    return main_incr, main_triee

#def joker_travesti(main_incr) : #permet de déterminer quelle carte doit devenir le joker
    #important dans les cas des doubles paires (pour savoir quel est le meilleur full) ou en cas de carte haute (pour savoir laquelle devient un double)



def classement_mains(liste_main_incr) :
    #cle_dyn = lambda x: tuple(x[i] for i in range(15))
    clé = lambda x: (-x[2], [-ordre_carte.index(c) for c in x[0]]) #on tri par Score (x[2]) décroissant, puis par ordre de cartes (AKQJT98765432) décroissant de la main (x[0])
    liste_classee = sorted(liste_mains_incr, key=clé)
    print(f"liste classée : {liste_classee}")
    return liste_classee

def reponse_exo(liste_classee):
    reponse=0
    for indice in range(len(liste_classee)):
        reponse+=(indice+1)*int(liste_classee[indice][1])
    return reponse

liste_mains_incr=[]
for ligne in lignes:
    score = 0
    main,bid=parsing(ligne)
    main_incr=[main,bid,score]
    main_triee=arrangement_main(main,bid)
    if partie=="partie1":
        main_incr, main_triee=type_main_partie1(main_incr, main_triee)
    elif partie=="partie2":
        main_incr, main_triee=type_main_partie2(main_incr, main_triee)
        #if "J" in main :
            #joker_travesti

    liste_mains_incr.append(main_incr)

liste_classee = classement_mains(liste_mains_incr)
reponse = reponse_exo((liste_classee))

print(f"la réponse à l'exercice est : {reponse}")
print(f"durée du programme : {time.time()-start}")