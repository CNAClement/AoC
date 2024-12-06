import re
import sys
import time
with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2016\9_1_ori.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")

pattern_marker_complet = re.compile("(\(\d+x\d+\))")
pattern_marker = re.compile("(\d+)x(\d+)")

def reperage_marker(ligne, numero_caractere):
    marker=""
    numero_caractere+=1 #on saute la "(" en cours
    while ligne[numero_caractere] != ")":
        marker += ligne[numero_caractere]
        numero_caractere+=1
    #print(f"marker : {marker}")
    match_marker=re.search(pattern_marker,marker)
    if match_marker :
        longueur_repetition = int(match_marker.group(1))
        nombre_repetitions = int(match_marker.group(2))
        #print(f"longueur du marker : {longueur_repetition}, nombre de répétitions = {nombre_repetitions}")
    else :
        print(f"Pas de match du pattern pour le marker {marker}")
        sys.exit("Abend: Aucun match trouvé. Arrêt du programme.")
    return numero_caractere, longueur_repetition, nombre_repetitions

def process_marker(ligne, numero_caractere,longueur_repetition,nombre_repetitions):
    zone_a_repeter=""
    numero_caractere+=1 #permet de skip la parenthèse fermante ")"
    for _ in range(longueur_repetition):
        zone_a_repeter += ligne[numero_caractere]
        numero_caractere+=1
    #print(f"zone à répéter : {zone_a_repeter}")
    zone_repetee=zone_a_repeter*nombre_repetitions
    #print(f"zone répétée : {zone_repetee}, numéro de caractère : {numero_caractere}")
    return numero_caractere, zone_repetee

def réponse(lignes_decompactees) :
    #print(f"lignes décompactées : {lignes_decompactees}")
    reponse=sum(len(lignes) for lignes in lignes_decompactees)
    print(f"réponse : {reponse}")

lignes_decompactees=[]
def traitement_ligne(lignes):
    for ligne in lignes:
        print(f"ligne à traiter : {ligne} de longueur {len(ligne)}")
        partie_deja_traitee = ""
        numero_caractere=0
        for _ in range(len(ligne)):
            if numero_caractere<len(ligne):
                if ligne[numero_caractere]!="(" :
                    partie_deja_traitee+=ligne[numero_caractere]
                else :
                    numero_caractere, longueur_repetition, nombre_repetitions = reperage_marker(ligne, numero_caractere)
                    partie_non_traitee=ligne[numero_caractere+longueur_repetition+1:]
                    #print(f"partie non traitée : {partie_non_traitee}")
                    numero_caractere, zone_repetee = process_marker(ligne, numero_caractere, longueur_repetition, nombre_repetitions)
                    partie_deja_traitee += zone_repetee
                    numero_caractere=len(partie_deja_traitee)-1 #on reprend à l'endroit où on s'est arrêté, le -1 est là pour compenser le +1 qui va arriver juste après
                    ligne=partie_deja_traitee+partie_non_traitee
                    #if partie_non_traitee!="":
                        #print(f"état de la ligne après décompactage : {ligne}, on reprend au caractère {numero_caractere}, c'est-à-dire {ligne[numero_caractere]}")
            numero_caractere += 1
        lignes_decompactees.append(ligne)
        #print(lignes_decompactees)

traitement_ligne(lignes)
réponse(lignes_decompactees)

for ligne in lignes_decompactees:
    scan=re.findall(pattern_marker_complet,ligne)
    if scan :
        traitement_ligne([ligne])
    else :
        réponse(lignes_decompactees)


