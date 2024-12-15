from utils_clement import lecture_fichier
def execution_jour11_partie1(chemin_fichier):
    ligne=lecture_fichier(chemin_fichier)[0] #une seule ligne
    liste_pierres=ligne.split()

    for i in range(75) :
        liste_pierres = maj_liste_pierres(liste_pierres)
    print(f"Résultat : {len(liste_pierres)}")


def maj_liste_pierres(liste_pierres):
    nouvelle_liste = []

    for numero_pierre in range(len(liste_pierres)):
        if liste_pierres[numero_pierre] == "0":
            nouvelle_liste.append("1")
        elif len(liste_pierres[numero_pierre]) % 2 == 0:
            milieu = int(len(liste_pierres[numero_pierre]) / 2 )
            nouvelle_liste.append(str(int(liste_pierres[numero_pierre][:milieu]))) #la petite zumba str > int > str permet de se débarasser des 0 à gauche : 072 > 72
            nouvelle_liste.append(str(int(liste_pierres[numero_pierre][milieu:])))
        else:
            nouvelle_liste.append(str(int(liste_pierres[numero_pierre]) * 2024))
    liste_pierres = nouvelle_liste
    return liste_pierres
