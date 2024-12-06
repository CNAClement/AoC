#249771500 too high
import re
import time
with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\7_1_ori.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")

start=time.time()
partie="partie1" #partie1 ou partie2, indique exercice à traiter

ordre_carte="AKQJT98765432"

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

def type_main(main_triee) :
    nombre_max=0
    for carte in range(13):
        if int(main_triee[carte])>nombre_max:
            nombre_max=int(main_triee[carte])
            carte_principale=carte
    #print(f"nombre max : {nombre_max} et carte principale : {carte_principale}")
    if nombre_max==5:
        main_triee[14]=1
    elif nombre_max==4:
        main_triee[14]=2
    elif nombre_max==3:
        nombre_max_secondaire=0
        for carte in range(13):
            if carte!=carte_principale:
                if int(main_triee[carte]) > nombre_max_secondaire:
                    nombre_max_secondaire = int(main_triee[carte])
        if nombre_max_secondaire==2:
            main_triee[14]=3
        else :
            main_triee[14]=4
    elif nombre_max == 2:
        nombre_max_secondaire = 0
        for carte in range(13):
            if carte!=carte_principale:
                if int(main_triee[carte]) > nombre_max_secondaire:
                    nombre_max_secondaire = int(main_triee[carte])
            if nombre_max_secondaire == 2:
                main_triee[14] = 5
            else:
                main_triee[14] = 6
    elif nombre_max == 1:
        main_triee[14]=7
    else : print("vérifier la main, elle n'est d'aucun type")

    return main_triee


def classement_mains(liste_mains_triees) :
    #cle_dyn = lambda x: tuple(x[i] for i in range(15))
    clé = lambda x: (-x[14], x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12])
    liste_mains_triees_final = sorted(liste_mains_triees, key=clé)
    print(f"main triée final : {liste_mains_triees_final}")
    return liste_mains_triees_final

def reponse_exo(liste_main_triee_final):
    reponse=0
    for indice in range(len(liste_main_triee_final)):
        reponse+=(indice+1)*int(liste_main_triee_final[indice][13])
        print(liste_main_triee_final[indice])
    return reponse


liste_mains_triees=[]
for ligne in lignes:
    main,bid=parsing(ligne)
    main_triee=arrangement_main(main,bid)
    main_triee=type_main(main_triee)
    liste_mains_triees.append(main_triee)

liste_main_triee_final = classement_mains(liste_mains_triees)
reponse = reponse_exo((liste_main_triee_final))

print(f"la réponse à l'exercice est : {reponse}")
print(f"durée du programme : {time.time()-start}")