#La petite course de voiture avec le bouton sur lequel il faut appuyer
import re
import time
with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\6_1_ori.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")

start=time.time()
partie="partie1" #partie1 ou partie2, indique exercice à traiter
pattern_time_groupe='Time:[\s]+(\d+)[\s]+(\d+)[\s]+(\d+)'

if partie=="partie2":
    contenu=contenu.replace(" ","")
    lignes = contenu.splitlines()
    longueur_ligne = len(lignes[0].split())  # on doit enlever le -1 du cas "partie 1", sinon on tombe sur le résultat 0, ce qui pose problème pour la boucle range(0)
else : longueur_ligne=len(lignes[0].split())-1 #longueur d'une ligne, moins le titre. Exemple : ['Time:', '53', '89', '76', '98'] ==> taille = 4 . Permet de savoir le nombre de durées / distances à traiter.

print(lignes)

def push_button(duree,record):
    temps_perdu=duree
    vitesse=duree
    duree_restante=(record - temps_perdu)
    distance_parcourue=duree_restante*vitesse
    return distance_parcourue

def comparaison_distance(distance_parcourue,record):
    nombredefaconsdegagner=0
    for facon in range(len(distance_parcourue)):
        if distance_parcourue[facon]>record:
            #print(f"record battu ({distance_parcourue} au lieu de {record})")
            nombredefaconsdegagner+=1
    return nombredefaconsdegagner

for ligne in lignes:
    if "Time:" in ligne :
        durees=re.findall('\d+',ligne)
    elif 'Distance:' in ligne :
        distances=re.findall('\d+',ligne)
    else : print("ligne non reconnue")
print(f"Time : {durees}, distances = {distances}")
print(lignes[0])
nombre_facons_course=[]
marge_erreur=1

for num_course in range(longueur_ligne):
    distance_parcourue_course=[]
    print(f"on est sur la course {num_course+1} de durée {durees[num_course]} et de distance {distances[num_course]}")
    for appui_bouton in range(int(durees[num_course])+1):
        #print(f"appui bouton = {appui_bouton}")
        distance_parcourue=push_button(appui_bouton,int(durees[num_course]))
        distance_parcourue_course.append(distance_parcourue)
    #print(f"distance_parcourue_course : {distance_parcourue_course}")
    nombredefaconsdegagner=comparaison_distance(distance_parcourue_course,int(distances[num_course]))
    nombre_facons_course.append(nombredefaconsdegagner)
    #print(nombredefaconsdegagner)
print(f"nombres de façon de gagner par course : {nombre_facons_course}")
for course in range(len(nombre_facons_course)):
    #marge_erreur=nombre_facons_course[course]*marge_erreur
    marge_erreur*=nombre_facons_course[course]

print(f"marge d'erreur : {marge_erreur}")
print(f"temps : {time.time() - start} secondes")

