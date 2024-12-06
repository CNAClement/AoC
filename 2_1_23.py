with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\2_1_ori.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")

nombre_max = dict([("red", 12), ("green", 13), ("blue", 14)])
print(nombre_max)


def decoupage_ligne(numero_ligne):
    #print(f"ligne traitée : {lignes[numero_ligne]}")
    decoupage_1 = lignes[numero_ligne].split(sep=":")
    # le premier élément de la liste ainsi splitée contient donc : "Game IDgame" .
    # On resplit cet élément avec "Game " en séparateur, le 2 eme élément de la liste contient donc : "IDgame"
    # print(f"découpage avec ID game : {decoupage_1[0]}")
    id_game = decoupage_1[0].split(sep="Game ")[1]

    # le 2eme élément de découpage_1 contient les différents sets de la game, séparés par des ;
    sets = decoupage_1[1].split(sep=";")
    # on obtient n sets
    #print(f"nombre de sets : {len(sets)}")
    #print(f"résultat : {sets}")
    return id_game, sets

def traitement_sets(sets,id_game, total_id):
    flag_impossible = 0
    #sets ressemble à quelque chose comme [' 9 red, 2 green, 2 blue', ' 3 blue, 7 green, 3 red', ' 2 blue, 1 red'] (noter les '' qui séparent les sets)
    for set in sets: #set serait : 9 red, 2 green, 2 blue
        cubes_tires_set = set.split(sep=',') #par exemple : [' 9 red', ' 2 blue', ' 2 green']
        #print(f"Cubes tirés dans le set  {cubes_tires_set}")
        for element in cubes_tires_set:
            nombre_couleur = element.split(sep=" ")
            #print(f"couleur : {nombre_couleur}")  # On obtient une liste du genre : couleur : ['', '4', 'green']
            #print(f"couleur : {nombre_couleur[2]}, nombre : {nombre_couleur[1]}")
            if int(nombre_couleur[1]) <= nombre_max[nombre_couleur[2]]:   # par exemple, si couleur[2] vaut "red", nombre_max["red"]=12
                #print("game possible")
                continue
            else:
                flag_impossible=1
                #print(f"la game {id_game} est impossible (set {cubes_tires_set})")
    if flag_impossible==0:
        total_id += int(id_game)
    return total_id


total_id = 0
for numero_ligne in range(len(lignes)):
    id_game, sets = decoupage_ligne(numero_ligne)
    total_id = traitement_sets(sets, id_game, total_id)

print(f"la réponse à l'exercice est : {total_id}")
