def moore_dijkstra_1(G, s):
    inf = sum(sum(G[sommet][i] for i in G[sommet]) for sommet in G) + 1
        #On considère comme "infini" un majorant de la somme de toutes les
        #pondérations du graphe
    s_explore = {s : [0, [s]]}  #{'A': [0, ['A']]}   #sommets explorés
        #On associe au sommet d'origine s la liste [longueur, plus court chemin]  (le chemin va être incrémenté au fur et à mesure)
    s_a_explorer = {j : [inf, ""] for j in G if j != s}  #sommets à explorer
        #On associe à chaque sommet j à explorer la liste [longueur, sommet précédent]
    for suivant in G[s]:
        s_a_explorer[suivant] = [G[s][suivant], s]
        #pour le sommet s="A" :
        #G[s] = G["A"] =  {'B': 2, 'C': 1}     (et notamment : G["A"]["B"] = 2 )
        #s_a_explorer: {'B': [77, ''], 'C': [77, ''], 'D': [77, ''], 'E': [77, ''], 'F': [77, ''], 'G': [77, '']}
        # Donc par exemple : s_a_explorer['B'] = [77, '']
        # Donc en revenant à suivant in G[s]: pour suivant = "B" (et pas "'B': 2" comme j'aurais pu le croire, probablement une subtilité du fonctionnement d'un dictionnaire ... )
        # on dit que cette valeur [77, "" ] devient : (2 , "A")

    print("Dans le graphe d\'origine {} dont les arcs sont :".format(s))
    for k in G:
        print(k, ":", G[k])
    print()
    print("Plus courts chemin de")

    #On créé une boucle qui tourne tant que la liste des sommets à explorer contient
    #des points tels que la longueur provisoire calculée depuis l'origine est
    #inférieure à l'infini
    while s_a_explorer and any(s_a_explorer[k][0] < inf for k in s_a_explorer):
        s_min = min(s_a_explorer, key = s_a_explorer.get)
        #rappel : s_a_explorer: {'B': [2, 'A'], 'C': [1, 'A'], 'D': [77, ''], 'E': [77, ''], 'F': [77, ''], 'G': [77, '']}
        #s_min va prendre comme valeur "B" ou "C" par exemple. Il va commencer par "C" (minimum de la clé).
        longueur_s_min, precedent_s_min = s_a_explorer[s_min]
        #longueur = "1" , précédent = "A"   (s_a_explorer["C"]=[1,"A"] )
        for successeur in G[s_min]: #pour "C" , G["C"] = {'A': 1, 'B': 2, 'D': 4, 'E': 3, 'F': 5} , donc successeur va valoir "A" , puis "B" , puis "D" , puis "E", puis "F"
            if successeur in s_a_explorer: #donc pas "A"
                dist = longueur_s_min + G[s_min][successeur]  #exemple : G["C"]["B"] = 2 , G["C"]["D"] = 4 , G["C"]["F"] = 5 ,  donc dist respectives : 3 et 6
                if dist < s_a_explorer[successeur][0]: # 3 pour B et 5 pour D, comparés à 2 pour B, 77 pour D
                    s_a_explorer[successeur] = [dist, s_min] #pour D, s_a_explorer["D"] = [5,"C"] .  Pour F : [6,"F"]
                    print(s_a_explorer)
        s_explore[s_min] = [longueur_s_min, s_explore[precedent_s_min][1] + [s_min]]
        del s_a_explorer[s_min]
        print("longueur", longueur_s_min, ":", " -> ".join(s_explore[s_min][1]))

    for k in s_a_explorer:
        print("Il n\'y a aucun chemin de {} à {}".format(s, k))
        #si à la fin du while, il reste des sommets dans s_a_explorer, alors c'est qu'il n'y a pas de chemin.
    print()

    return s_explore


MonGraphe = {
    'A':{'B':2, 'C':1},
    'B':{'A':2, 'C':2, 'D':1, 'E':3},
    'C':{'A':1, 'B':2, 'D':4, 'E':3, 'F':5},
    'D':{'B':1, 'C':4, 'E':3, 'F':6, 'G':5},
    'E':{'B':3, 'C':3, 'D':3, 'F':1},
    'F':{'C':5, 'D':6, 'E':1, 'G':2},
    'G':{'D':5, 'F':2}
    }

print(f"G(s) : {MonGraphe['A']}")
moore_dijkstra_1(MonGraphe, 'A')