import re
from pathlib import Path #permet de récupérer le chemin du répertoire du fichier d'entrée (passé en paramètre par main) pour y écrire les fichiers en sortie.

def execution_jour5_partie1(chemin_fichier):
    fichier_ordre_pages, fichier_liste_pages = lecture_et_ecriture_fichiers(chemin_fichier)
    contenu=lecture_fichier(fichier_liste_pages)
    lignes=contenu.splitlines()
    somme_valeurs_milieu = 0
    for ligne in lignes :
        print(f"On traite la ligne {ligne}.")
        for element in ligne.split(',') :
            ordre_respecte=verification_ordre(element, ligne.split(','), lecture_fichier(fichier_ordre_pages).splitlines() )  #le 2eme paramètre renvoie une liste de lignes avec les ordres des pages
            if ordre_respecte == False :
                print(f"La ligne {ligne} ne respecte pas les exigences.")
                break
        if ordre_respecte == True : # On a itéré sur tous les éléments et ils respectent tous le bon ordre :
            print(f"La ligne {ligne} respecte les exigences.")
            somme_valeurs_milieu +=  milieu_ligne(ligne.split(','))
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

def verification_ordre(element, ligne_avec_element, ordre_pages):
    # on veut repérer les lignes où il apparait dans le fichier "ordre"
    # pour chacune de ces lignes, on veut récupérer l'élément_associé, celui en binome de notre élément.
    # On veut savoir s'il doit être avant ou après.
    # Enfin, on veut vérifier que l'ordre est respecté

    #print(f"On traite l'élément {element} en vérifiant la ligne : {ligne_avec_element}")
    for ligne in ordre_pages :
        if element in ligne :
            #print(f"On a trouvé l'élément {element} dans la ligne {ligne}")
            position = ligne.find(element) # renvoie la position de l'élément dans le couple
            if position == 0 :
                #print("première position")
                element_associe=ligne[3:]
                #print(f"Element associé : {element_associe}")
                if element_associe in ligne_avec_element :
                    if (ligne_avec_element.index(element_associe)-ligne_avec_element.index(element))>0:
                        #print(f"L'ordre est bien respecté")
                        continue
                    else :
                        #print(f"Ordre KO")
                        return False

            else :
                #print("deuxième position")
                element_associe=ligne[:2]
                #print(f"Element associé : {element_associe}")
                if element_associe in ligne_avec_element :
                    if (ligne_avec_element.index(element)-ligne_avec_element.index(element_associe))>0:
                        #print(f"L'ordre est bien respecté")
                        continue
                    else :
                        #print(f"Ordre KO")
                        return False

    return True

def milieu_ligne(ligne):
    print(f"la valeur du milieu est : {ligne[len(ligne)//2]}.")
    return int(ligne[len(ligne)//2])