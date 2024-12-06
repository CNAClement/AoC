coordonnées_interdites = [(6, 2), (7, 2), (8, 2), (10, 2), (2, 3), (3, 3), (4, 3), (6, 3), (7, 3), (10, 3), (3, 4), (5, 4), (9, 4), (5, 5), (7, 5), (2, 6), (3, 6), (7, 6), (8, 6), (9, 6), (10, 6), (2, 7), (3, 7), (6, 7), (10, 7), (8, 8), (9, 8), (2, 9), (3, 9), (5, 9), (7, 9), (8, 9), (9, 9), (10, 9), (2, 10), (3, 10), (6, 10), (7, 10), (9, 10), (10, 10)]


def maj_coordonnées(x,y,sens):
    nouveau_x = x
    nouveau_y = y
    if dictionnaire_sens[sens]=="droite":
        nouveau_x = x + 1
    elif dictionnaire_sens[sens]=="bas":
        nouveau_y = y + 1
    elif dictionnaire_sens[sens]=="gauche":
        nouveau_x = x - 1
    elif dictionnaire_sens[sens]=="haut":
        nouveau_y = y - 1

    if coordonnées_valides(nouveau_x, nouveau_y):
        return 1, nouveau_x ,nouveau_y
    else : return 0, x, y

def coordonnées_valides(x,y):
    valide = False
    déplacement_impossible = [coordonnées for coordonnées in coordonnées_interdites if  coordonnées[0] == x % longueur_jardin
                              and coordonnées[1] == y % longueur_jardin]
    #print(f"déplacements impossibles : {déplacement_impossible}")
    if déplacement_impossible == [] :
        print(f"déplacement en {x} , {y} validé ")
        valide = True
    else :         print(f"déplacement en {x} , {y} non valide ")
    return valide




def déplacement(x,y,sens, count, nombre_pas):
    #à ce stade de l'écriture du programme, le pb est de gérer l'incrémentation de nombre de pas, actuellement partagé par tous les chemins
    #(c'est à dire que quand on teste un autre chemin, nombre de pas n'est pas réinitialisé)
    print(f"on se positionne sur les coordonnées {x}, {y}")
    nombre_pas += 1
    if nombre_pas == nombre_pas_paramétré :
        print("on a atteint le nombre de pas fixés")
        if coordonnées_valides(x,y) :
            print(f"on ajoute 1 à la fonction, count vaut : {count}")
            return 1 #la fonction retourne 1 si le déplacement est valide à la fin du nombre de pas autorisés
        else : return 0 #si le déplacement n'est pas valide, on retourne 0



    for sens in range(4):
        """Le but est de créér un nouvel appel à la fonction pour chaque sens+déplacement valide (donc potentiellement 4 appels si les 4 directions sont possibles)
        """
        print(f"sens  : {dictionnaire_sens[sens]}, nombre de pas : {nombre_pas}, coordonnées actuelles : ({x},{y})")
        valide, x, y = maj_coordonnées(x, y, sens)
        if valide :
            count += déplacement(x, y, sens, count, nombre_pas)  # récursivité
    return count



dictionnaire_sens = {0:"droite", 1:"bas", 2:"gauche", 3:"haut"}
#longueur_jardin = tableau.shape[0]
longueur_jardin = 10
nombre_pas_paramétré = 2
count=0
x,y = 6,6

count += déplacement(x,y, 1,  count, -1)
print(f"réponse : {count}")

