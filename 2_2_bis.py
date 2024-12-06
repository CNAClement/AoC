with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2016\2_1_ori.txt', 'r') as fichier:
    contenu= fichier.read()
    ligne = contenu.splitlines()

coordonnees_interdites = [(0,1),(0,2),(0,3),(0,4),(0,5),(1,0),(2,0),(3,0),(4,0),(5,0),(6,1),(6,2),(6,3),(6,4),(6,5),(1,6),(2,6),(3,6),(4,6),(5,6),(1,1),(2,1),(4,1),(5,1),(1,2),(5,2),(1,4),(5,4),(1,5),(2,5),(4,5),(5,5)]
code = []

print(f"taille du fichier : {len(contenu)} " )
print(f"nombre de lignes : {len(ligne)}")
print(f"coordonnees interdites : {coordonnees_interdites}" )


for numero_ligne in range(len(ligne)):
    coordonnees_actuelles=(1,3)


    print(f"traitement de la ligne {numero_ligne+1}")
    for indice in range(len(ligne[numero_ligne])):
        # exemple : numero_ligne = 2 , alors ligne[numero_ligne] = contenu de la 3eme ligne, alors len(ligne[numero_ligne])  = longueur de cette ligne
        instruction = ligne[numero_ligne][indice]
        # on se place sur une ligne donnée et on parcourt tous ses caractères du premier jusqu'au dernier caractère
        if instruction == 'U' :
            ytest= coordonnees_actuelles[1] -1
            if (coordonnees_actuelles[0] , ytest) not in coordonnees_interdites:
                coordonnees_actuelles = (coordonnees_actuelles[0] , ytest)
        elif instruction == 'R' :
            xtest= coordonnees_actuelles[0] +1
            if (xtest, coordonnees_actuelles[1])  not in coordonnees_interdites:
                coordonnees_actuelles = (xtest, coordonnees_actuelles[1])
        elif instruction == 'D' :
            ytest= coordonnees_actuelles[1] +1
            if (coordonnees_actuelles[0] , ytest)  not in coordonnees_interdites:
                coordonnees_actuelles = (coordonnees_actuelles[0], ytest)
        elif instruction == 'L' :
            xtest= coordonnees_actuelles[0] -1
            if (xtest, coordonnees_actuelles[1])  not in coordonnees_interdites:
                coordonnees_actuelles = (xtest, coordonnees_actuelles[1])
    print(f"coordonnees_actuelles : {coordonnees_actuelles}")
    if coordonnees_actuelles == (3,1):
        code.append(1)
    elif coordonnees_actuelles == (2, 2):
        code.append(2)
    elif coordonnees_actuelles == (3, 2):
        code.append(3)
    elif coordonnees_actuelles == (4,2):
        code.append(4)
    elif coordonnees_actuelles == (1, 3):
        code.append(5)
    elif coordonnees_actuelles == (2, 3):
        code.append(6)
    elif coordonnees_actuelles == (3, 3):
        code.append(7)
    elif coordonnees_actuelles == (4,3):
        code.append(8)
    elif coordonnees_actuelles == (5, 3):
        code.append(9)
    elif coordonnees_actuelles == (2, 4):
        code.append("A")
    elif coordonnees_actuelles == (3, 4):
        code.append("B")
    elif coordonnees_actuelles == (4, 4):
        code.append("C")
    elif coordonnees_actuelles == (3, 5):
        code.append("D")
    print(code)

