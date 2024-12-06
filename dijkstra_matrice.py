def moore_dijkstra_2 (M, s):
    inf = sum(sum(ligne) for ligne in M) + 1
    nb_sommets = len(M)
    s_explore = {s : [0, [s]]} #{0: [0, [0]]} pour le premier passage
    #On associe au sommet d'origine s la liste [longueur, plus court chemin]
    s_a_explorer = {j : [inf, ""] for j in range(nb_sommets) if j != s}
    #{1: [77, ''], 2: [77, ''], 3: [77, ''], 4: [77, ''], 5: [77, ''], 6: [77, '']}
    #On associe à chaque sommet j à explorer la liste [longueur, sommet précédent]
    for suivant in range(nb_sommets):
        if M[s][suivant]:  #par exemple ici, M[0][suivant] va valoir : 0 (donc False : le if n'est pas respecté), puis 2, 1, 0, 0 ...
            s_a_explorer[suivant] = [M[s][suivant], s] # s_a_explorer[0] =  s_a_explorer[1] = [2, 0], s_a_explorer[2] = [1,0]
            #{1: [2, 0], 2: [1, 0], 3: [77, ''], 4: [77, ''], 5: [77, ''], 6: [77, '']}

    print("Dans le graphe d\'origine {} de matrice d\'adjacence :".format(s))
    for ligne in M:
        print(ligne)
    print()

    while s_a_explorer and any(s_a_explorer[k][0] < inf for k in s_a_explorer):
        s_min = min(s_a_explorer, key=s_a_explorer.get)
        longueur_s_min, precedent_s_min = s_a_explorer[s_min]
        for successeur in range(nb_sommets):
            if M[s_min][successeur] and successeur in s_a_explorer:
                dist = longueur_s_min + M[s_min][successeur]
                if dist < s_a_explorer[successeur][0]:
                    s_a_explorer[successeur] = [dist, s_min]
        s_explore[s_min] = [longueur_s_min, s_explore[precedent_s_min][1] + [s_min]]
        del s_a_explorer[s_min]
        print()
        print("On a sélectionné le sommet {}".format(s_min))
        print("Plus courts chemins de longueur", longueur_s_min, ":", " -> ".join(map(str, s_explore[s_min][1])))
        print("La nouvelle liste des sommets explorés est : ")
        print(s_explore)
        print("La nouvelle liste des sommets à explorer est : ")
        print(s_a_explorer)
        print()

    for k in s_a_explorer:
        print("Il n\'y a pas de chemin de {} à {}".format(s, k))

    return s_explore


maMatrice = [[0, 2, 1, 0, 0, 0, 0],
             [2, 0, 2, 1, 3, 0, 0],
             [1, 2, 0, 4, 3, 5, 0],
             [0, 1, 4, 0, 3, 6, 5],
             [0, 3, 3, 3, 0, 1, 0],
             [0, 0, 5, 6, 1, 0, 2],
             [0, 0, 0, 5, 0, 2, 0]]

moore_dijkstra_2(maMatrice, 0)