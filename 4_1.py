with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2016\4_1_ori.txt', 'r') as fichier:
    contenu = fichier.read()
    rooms=contenu.splitlines()
    print(f"longueur du fichier : {len(contenu)}")

with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2016\4_1_output.txt', 'w') as fichier_output:
    fichier_output.write("")


def ecrire_fichier(texte) :
    with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2016\4_1_output.txt', 'a') as fichier_output:
        texte_saut = texte + "\n"
        fichier_output.write(texte_saut)

reponse = 0
vraies_rooms =""
rooms_a_trouver = []
rooms_leurres = []
liste_vrais_noms_id = []

def nouvelle_lettre(lettre,clé) :
    return chr((ord(lettre) - ord('a') + clé) % 26  + ord('a')) #permet de transformer une lettre en une autre lettre, par exemple b+3 ==> f
                                                                #le modulo permet de rester dans les lettres de l'alphabet : z+1==>a

def decryptage(nom,id_secteur) :
    vrai_nom=""
    for caractere in nom:
        vrai_nom+=nouvelle_lettre(caractere,id_secteur)
    return vrai_nom


for ligne in range(len(rooms)):
    vraie_room = False
    nom = ""
    id_secteur = ""
    checksum = ""
    index = 0
    #print(f"on traite la ligne : {rooms[ligne]}")
    #print(f"longueur de la ligne : {len(rooms[ligne])}")
    caractere = rooms[ligne][index]

    while caractere.isdigit() == 0:
        caractere = rooms[ligne][index]
        if caractere.isdigit() == 0:
            if caractere.islower() == 1 or caractere == '-':
                nom += caractere
            else:
                print(f"la lettre {caractere} est en majuscule ou KO en position {index}")
        else:
            #print("je suis un énorme fils de pute qui ne comprend pas une instruction simple")
            break
        index += 1
    nom = nom.replace("-", "")
    while caractere.isdigit() == 1:
        caractere = rooms[ligne][index]
        if caractere.isdigit() == 1:
            id_secteur += caractere
        else:
            #print("je suis un énorme fils de pute qui ne comprend pas une instruction simple")
            break
        index += 1

    while caractere.isdigit() == 0 and index < len(rooms[ligne]):
        caractere = rooms[ligne][index]
        if caractere.isdigit() == 0 and index < len(rooms[ligne]):
            checksum += caractere
        #else:
          #  print("je suis un énorme fils de pute qui ne comprend pas une instruction simple")
        index += 1
    checksum = checksum.replace("[", "")
    checksum = checksum.replace("]", "")
    checksum = checksum.replace(" ", "")

    #print(f"nom : {nom}")
    #print(f"id_secteur : {id_secteur}")
    #print(f"checksum : {checksum}")

    def lettre_vers_numero(lettre):
        return ord(lettre) - ord('a')


    # "a" vaut "0", "b" vaut "1" etc.


    compteur_lettres_nom = []
    for i in range(26):
        compteur_lettres_nom.append(
            [0, chr(ord('a') + i)])  # permet de faire le lien entre un chiffre et une lettre (exemple : 0 ==> a , 1 ==> b )
    for lettre in nom:
        compteur_lettres_nom[lettre_vers_numero(lettre)][0] += 1

    compteur_trie = sorted(compteur_lettres_nom, key=lambda x: (-x[0], x[1]))
    # on tri avec les valeurs numériques (1ere colonne : x[0] dans l'ordre décroissant, et dans un second temps, on départage les égalités avec un tri
    # secondaire sur les caractères dans l'ordre alphabétique sur la 2eme colonne x[1]

    #print(f"le compteur trié est : \n {compteur_trie} ")

    compteur_check=0
    for check in range(len(checksum)):
        if checksum[check] == compteur_trie[check][1]:
            compteur_check+=1

    if compteur_check==5:
        reponse += int(id_secteur)
        vraie_room = True
        rooms_a_trouver.append(rooms[ligne])
        vraies_rooms+=decryptage(nom,int(id_secteur))
        liste_vrais_noms_id.append([decryptage(nom,int(id_secteur)),id_secteur])
        texte_a_ecrire = decryptage(nom,int(id_secteur))+"    , avec : " + id_secteur
        ecrire_fichier(texte_a_ecrire)
    else:
        rooms_leurres.append(rooms[ligne])

#print(f"liste des rooms : {rooms_a_trouver}")
#print(f"liste des leurres : {rooms_leurres}")
#print(f"vrais noms : {vraies_rooms}")

print(f"la réponse à la partie 1 de l'exercice est : {reponse}")

for room in range(len(liste_vrais_noms_id)):
    if liste_vrais_noms_id[room][0]=="northpoleobjectstorage":
        print(f"La réponse à la partie 2 de l'exercice est : l'ID secteur de northpoleobjectstorage est {liste_vrais_noms_id[room][1]}  (ligne {room+1})")
#print(f"la liste des vraies rooms et de leur ID_secteur est : {liste_vrais_noms_id}")
