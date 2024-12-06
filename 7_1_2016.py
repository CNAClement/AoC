with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2016\7_1_ori.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")


# def decoupage_ligne(numero_ligne):
#    #print(f"ligne traitée : {lignes[numero_ligne]}")
#    decoupage_1 = lignes[numero_ligne].split(sep="[")
#    #le premier élément est déjà exploitable, le 2eme doit de nouveau être splitté
#    decoupage_2 = decoupage_1[1].split(sep="]")
#    partie_1=decoupage_1[0]
#    partie_2=decoupage_2[0] #intra_bracket
#    partie_3=decoupage_2[1]
#    return partie_1 , partie_2 , partie_3


def decoupage_ligne(numero_ligne):
    outer_bracket = []
    inner_bracket = []
    iteration = 1
    index = 0
    while index <= len(lignes[numero_ligne]) - 1:
        mot = ""
        if lignes[numero_ligne][index] != "[" and lignes[numero_ligne][index] != "]":
            while index < len(lignes[numero_ligne]) and lignes[numero_ligne][index] != "[" and lignes[numero_ligne][index] != "]" :
                mot += lignes[numero_ligne][index]
                index += 1
            outer_bracket.append(mot)
        elif lignes[numero_ligne][index] == "[":
            index = index + 1  # on avance d'un cran pour ne pas écrire le "[" dans le mot
            while index < len(lignes[numero_ligne]) and lignes[numero_ligne][index] != "]" :
                mot += lignes[numero_ligne][index]
                index += 1
            inner_bracket.append(mot)
        else:
            index = index + 1  # on est arrivé au "]", on sort donc du bracket, on avance d'un cran et on reprend la boucle
        iteration += 1
    return inner_bracket, outer_bracket

def test_tls(partie) : #partie représente soit inner_bracket soit outer_bracket
    flag_tls = 0
    abba=""
    for mot in partie:
        if len(mot)<4:
            continue
        else :
            for index in range(len(mot)-3):
                if mot[index]==mot[index+3]:
                    if mot[index+1]==mot[index+2] and mot[index] != mot[index+1]:
                        flag_tls=1
                        abba=mot[index:index+4]
                        break
    return flag_tls, abba

def test_ssl(outer_bracket, inner_bracket) :
    flag_ssl = 0
    aba=[]
    for mot in outer_bracket:
        if len(mot)<3:
            continue
        else :
            for index in range(len(mot)-2):
                if mot[index]==mot[index+2]:
                    if  mot[index] != mot[index+1]:
                        aba.append(mot[index:index+3])
    if aba != []:
        #pour chaque aba de la liste (il peut y en avoir plusieurs), on va tester sa présence dans chaque mot des outer brackets.
        #par exemple aba = [[aba],[xyz]] et outer_bracket = ['aaxyz', 'axaaba ']
        for mot_aba in aba:
            for mot in inner_bracket:
                if len(mot) < 3:
                    continue
                else:
                    for index in range(len(mot) - 2):
                        if mot[index] == mot_aba[1] and mot[index+1] == mot_aba[0] and mot[index+2] == mot_aba[1]:
                            flag_ssl = 1
                            break
    return flag_ssl, aba


compteur_tls=0
compteur_ssl=0
for ligne in range(len(lignes)):
    print(f"traitement de la ligne n° {ligne+1} : {lignes[ligne]}  (taille : {len(lignes[ligne])})")
    inner_bracket, outer_bracket = decoupage_ligne(ligne)
    print(f"inner_bracket : {inner_bracket} et outer_bracket = {outer_bracket}")
    #flag_tls_outer_bracket, abba = test_tls(outer_bracket)
    #if flag_tls_outer_bracket==1:
        #print(f"Il y a bien une Autonomous Bridge Bypass Annotation ({abba} dans la partie hors bracket de {lignes[ligne]})")
    #flag_tls_inner_bracket, abba = test_tls(inner_bracket)
    #if flag_tls_outer_bracket==1:
        #print(f"Il y a bien une Autonomous Bridge Bypass Annotation ({abba} dans la partie bracket de {lignes[ligne]})")
    #if flag_tls_outer_bracket==1 and flag_tls_inner_bracket==0:
    #    print(f"les deux conditions sont respectées")
    #    compteur_tls+=1
    #else :
    #    print(f"une condition n'est pas respectée")

    flag_ssl, aba = test_ssl(outer_bracket, inner_bracket)
    if flag_ssl == 1 :
        #print(f"on a un ssl fonctionnel pour la ligne {lignes[ligne]} avec aba = {aba}")
        compteur_ssl+=1

print(f"le nombre d'IPs qui supportent TLS est : {compteur_tls}")
print(f"le nombre d'IPs qui supportent SSL est : {compteur_ssl}")