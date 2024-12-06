# 4521 too low
import re
from pathlib import Path #permet de récupérer le chemin du répertoire du fichier d'entrée (passé en paramètre par main) pour y écrire les fichiers en sortie.

def execution_jour5_partie2(chemin_fichier):
    fichier_ordre_pages, fichier_liste_pages = lecture_et_ecriture_fichiers(chemin_fichier)
    ordre_pages=lecture_fichier(fichier_ordre_pages).splitlines()

    liste_pages=lecture_fichier(fichier_liste_pages)
    lignes=liste_pages.splitlines()
    somme_valeurs_milieu = 0
    for ligne in lignes :
        ligne_corrigee = corriger_ligne(ligne.split(',') , ordre_pages)
        if ligne_corrigee :
            print(f"On a dû corriger la ligne {ligne}.")
            print(f"La ligne corrigée est : {ligne_corrigee}.")

            #print(f"Si la ligne était recorrigée : {corriger_ligne(ligne_corrigee, fichier_ordre_pages)}")
            # On recorrige en boucle tant qu'il y a des modifications à effectuer :
            while corriger_ligne(ligne_corrigee, ordre_pages) :  #Tant que ça ne renvoie pas None
                print(f"Résultat du while : {corriger_ligne(ligne_corrigee, ordre_pages)}")
                print(f"La ligne {ligne_corrigee} a encore besoin d'être corrigée.")
                ligne_corrigee = corriger_ligne(ligne_corrigee, ordre_pages)
                print(f"Ligne recorrigée : {ligne_corrigee}")
            somme_valeurs_milieu +=  milieu_ligne(ligne_corrigee)
        else :
            print(f"La ligne {ligne} n'a pas besoin d'être corrigée.")

    print(f"Le résultat cherché (somme des valeurs du milieu) est {somme_valeurs_milieu}.")
def lecture_et_ecriture_fichiers(chemin_fichier):
    # Détecte le type de ligne dans le fichier en entrée et créé deux fichiers en sortie, selon le pattern trouvé.
    pattern_ordre_page=re.compile(r"\d{2}\|\d{2}")
    pattern_liste_pages = re.compile(r"^(\d{2},)+\d{2}$")  #succession de nombres à deux chiffres séparés par des virgules, sauf le dernier nombre qui n'esst pas suivi par une virgule

    chemin_fichier = Path(chemin_fichier)  # Conversion en objet Path
    repertoire = chemin_fichier.parent
    fichier_ordre_pages = repertoire/"ordre_pages_5.txt"
    fichier_liste_pages = repertoire/"liste_pages_5.txt"

    # Au lieu du with open(chemin_fichier) habituel, on fait chemin_fichier.open( ) qui est une méthode Pathlib.
    with chemin_fichier.open("r") as fichier_entree, \
            fichier_ordre_pages.open("w") as fichier_ordre, \
            fichier_liste_pages.open("w") as fichier_liste:

        for ligne in fichier_entree :
            if pattern_ordre_page.search(ligne):
                fichier_ordre.write(ligne)
            elif pattern_liste_pages.match(ligne):
                fichier_liste.write(ligne)

    return fichier_ordre_pages, fichier_liste_pages


def lecture_fichier(chemin_fichier):
    with open(chemin_fichier, 'r') as fichier:
        contenu = fichier.read()
        return contenu

def corriger_ligne(ligne , ordre_pages) :     # Je déplace cette fonction de l'appel principal afin de mieux pouvoir gérer le return
    #print(f"On traite la ligne {ligne}.")
    ligne=ligne[:]
    # Permet de faire une copy de la ligne (c'est l'équivalent de ligne.copy() ), ce qui évite les
    # effets de bord de la mutation in place lorsque je modifie la liste.
    flag_ligne_corrigee = False
    for element in ligne:
        print(flag_ligne_corrigee)
        flag_ligne_corrigee , ligne = verification_ordre(element, ligne, ordre_pages , flag_ligne_corrigee)  # le 2eme paramètre renvoie une liste de lignes avec les ordres des pages
        print(f"ligne corrigée sortie fonction : {ligne}")

    # l'idée est bien que la fonction verification_ordre pour chaque élément renvoie un Flag True s'il y a une modification à faire.
    # Cette fonction ne renvoie pas de flag False, autrement dit si un élément de la liste n'est pas à corriger mais qu'un
    # élément précédent l'était, on n'écrase pas le flag, qui reste quand même à True.
    # Pour cela, on a dû rajouter le paramètre "flag_ligne_corrigee" dans la fonction.

    return ligne if flag_ligne_corrigee else None


def verification_ordre(element, ligne_avec_element, ordre_pages , flag_ligne_corrigee):
    # on veut repérer les lignes où il apparait dans le fichier "ordre"
    # pour chacune de ces lignes, on veut récupérer l'élément_associé, celui en binome de notre élément.
    # On veut savoir s'il doit être avant ou après.
    # Enfin, on veut vérifier que l'ordre est respecté

    print(f"On traite l'élément {element} en vérifiant la ligne : {ligne_avec_element}")
    for ligne in ordre_pages :
        if element in ligne :
            position = ligne.find(element) # renvoie la position de l'élément dans le couple
            if position == 0 :
                element_associe=ligne[3:]
                if element_associe in ligne_avec_element :
                    if (ligne_avec_element.index(element_associe)-ligne_avec_element.index(element))>0:
                        #print(f"L'ordre est bien respecté")
                        continue
                    else :
                        # L'élément associé aurait dû être en deuxième position mais on l'a trouvé en première position.
                        # On le déplace juste après l'élément de base (.insert(nouvelle_position, element à insérer) ):
                        element_associe = ligne_avec_element.pop(ligne_avec_element.index(element_associe))
                        ligne_avec_element.insert(ligne_avec_element.index(element)+1 , element_associe)
                        print("ko1")
                        flag_ligne_corrigee = True

            else :
                element_associe=ligne[:2]
                if element_associe in ligne_avec_element :
                    if (ligne_avec_element.index(element)-ligne_avec_element.index(element_associe))>0:
                        #print(f"L'ordre est bien respecté")
                        continue
                    else :
                        print(f"Element : {element}, element associé : {element_associe}, positions respectives : {ligne_avec_element.index(element)} , {ligne_avec_element.index(element_associe)} ")

                        # L'élément associé aurait dû être en première position mais on l'a trouvé en deuxième position.
                        # On le déplace juste avant l'élément de base (.insert(nouvelle_position, element à insérer) ):
                        element_associe = ligne_avec_element.pop(ligne_avec_element.index(element_associe))
                        ligne_avec_element.insert(ligne_avec_element.index(element) , element_associe)
                        print(f"ligne corrigée : {ligne_avec_element}")
                        flag_ligne_corrigee = True

    return flag_ligne_corrigee, ligne_avec_element


def milieu_ligne(ligne):
    print(f"la valeur du milieu est : {ligne[len(ligne)//2]}.")
    return int(ligne[len(ligne)//2])