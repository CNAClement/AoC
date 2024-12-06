def execution_jour1_partie1(chemin_fichier):
    with open(chemin_fichier, 'r') as fichier:
        contenu = fichier.read()
        lignes = contenu.splitlines()

    # lignes est une liste de ligne.
    # Chaque ligne est constituée d'une paire de valeurs, par exemple : ['3   4', '4   3' , ... ]
    liste_tuples= [tuple(map(int, paire.split())) for paire in lignes]
    # On obtient une liste de tuples : [(3, 4), (4, 3) , ... ]

    # On trie les éléments de gauche par ordre croissant :
    elements_gauche=sorted(x[0] for x in liste_tuples)
    # idem éléments de droite
    elements_droite=sorted(x[1] for x in liste_tuples)

    liste_tuples_triee = list(zip(elements_gauche,elements_droite))
    print(liste_tuples_triee)

    distance_totale=0
    for paire in liste_tuples_triee:
        distance=abs(paire[1]-paire[0])
        distance_totale+=distance

    print(distance_totale)