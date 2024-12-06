import hashlib
import time

start=time.time()

def md5_hash(chaine):
    # Créer un objet de hachage MD5
    md5 = hashlib.md5()

    # Mettre à jour le hachage avec la chaîne encodée en UTF-8
    md5.update(chaine.encode('utf-8'))

    # Récupérer la représentation hexadécimale du hachage
    hachage_md5 = md5.hexdigest()

    return hachage_md5


def password_ready(chaine_a_hacher) :  #cette fonction détermine si le hash peut aider à générer le password, c'est-à-dire si les 5 premiers caractères sont égaux à 0
    hash=md5_hash(chaine_a_hacher)
    #print(f"chaine à hasher : {chaine_a_hacher}")
    #print(f"hash : {hash}")
    flag_ready=1
    for index in range(5):
        #print(f"passage n° {index+1}, le caractère est : {hash[index]}")
        if hash[index]=="0":
            continue
        else :
            flag_ready=0
            break
    return flag_ready

def remplissage_password(password,hash,lettre_a_trouver):
    #On détermine la lettre qui va potentiellement être changée :
    position_a_changer = hash[5]
    if position_a_changer.isdigit()==False:
        print(f"la position à changer n'est pas un chiffre ({position_a_changer})")
    else :
        position_a_changer=int(position_a_changer)
        if position_a_changer>7 :
            print(f"position hors range ({position_a_changer})")
        elif password[position_a_changer]==" ":
            password="{}{}{}".format(password[0:position_a_changer],hash[6],password[position_a_changer+1:])
            lettre_a_trouver+=1
            print(f"le password a avancé, il vaut maintenant '{password}'")
            print(f"recherche de la lettre n° {lettre_a_trouver}")
        else : print(f"Il y a déjà une lettre en position {position_a_changer} du password")
    return password, lettre_a_trouver

def password_complet(password) :
    flag_complet=0
    for caractere in password :
        if caractere ==" ":
            flag_complet=0
            break
        else : flag_complet=1
    return flag_complet

door_id = 'wtnhxymk'
index_chaine = "0"
chaine_a_hacher = door_id +index_chaine
index = 0
flag_ready = 0
flag_complet = 0
password = " "*8
lettre_a_trouver = 1
compteur_iteration=0

print(f"recherche de la lettre n° {lettre_a_trouver}")
while flag_complet == 0 :
    while flag_ready==0:
        compteur_iteration += 1
        flag_ready = password_ready(chaine_a_hacher)
        if flag_ready ==0:
            index+=1
            index_chaine=str(index)
            chaine_a_hacher = door_id + index_chaine
        else :
            hash = md5_hash(chaine_a_hacher) #on pourrait récupérer le retour de la fonction, qui a déjà calculé ce hash, mais ça serait lourd (plusieurs millions de retour pour rien avant d'avoir une lettre)
            print(f"On a un résultat positif, la chaine vaut {chaine_a_hacher}, le hash vaut {hash}")
    password,lettre_a_trouver =remplissage_password(password,hash,lettre_a_trouver)
    index += 1
    index_chaine = str(index)
    chaine_a_hacher = door_id + index_chaine
    flag_ready=0
    flag_complet = password_complet(password)

print(f"fin du programme, le mot de passe est : {password}\nce programme a mis pas moins de {compteur_iteration} itérations")
print(f"temps total : {time.time() - start }")



