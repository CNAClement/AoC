with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\2_1_ori.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")

def decoupage_ligne(numero_ligne):
    #print(f"ligne traitée : {lignes[numero_ligne]}")
    decoupage_1 = lignes[numero_ligne].split(sep=":")
    # le 2eme élément de découpage_1 contient les différents sets de la game, séparés par des ;
    sets = decoupage_1[1].split(sep=";")
    # on obtient n sets
    #print(f"nombre de sets : {len(sets)}")
    print(f"résultat : {sets}")
    return sets

def traitement_sets(sets):
    nombre_max_set = dict([("red", 0), ("green", 0), ("blue", 0)])
    #sets ressemble à quelque chose comme [' 9 red, 2 green, 2 blue', ' 3 blue, 7 green, 3 red', ' 2 blue, 1 red'] (noter les '' qui séparent les sets)
    for set in sets: #set serait : 9 red, 2 green, 2 blue
        cubes_tires_set = set.split(sep=',') #par exemple : [' 9 red', ' 2 blue', ' 2 green']
        #print(f"Cubes tirés dans le set  {cubes_tires_set}")
        for element in cubes_tires_set:
            nombre_couleur = element.split(sep=" ")
            #print(f"couleur : {nombre_couleur}")  # On obtient une liste du genre : couleur : ['', '4', 'green']
            #print(f"couleur : {nombre_couleur[2]}, nombre : {nombre_couleur[1]}")
            if int(nombre_couleur[1]) > int(nombre_max_set[nombre_couleur[2]]):   # par exemple, si couleur[2] vaut "red", on regarde si le nombre de cubes red tirés est plus grand que le max déjà atteint sur le set
                nombre_max_set[nombre_couleur[2]]=int(nombre_couleur[1])    # Si oui, le nouveau nombre max de cette couleur est mis à jour
    power_of_sets=nombre_max_set["red"]*nombre_max_set["blue"]*nombre_max_set["green"]
    return power_of_sets


somme_power_of_sets = 0
for numero_ligne in range(len(lignes)):
    sets = decoupage_ligne(numero_ligne)
    power_of_sets = traitement_sets(sets)
    print(f"puissance : {power_of_sets}")
    somme_power_of_sets+=power_of_sets

print(f"la réponse à l'exercice est : {somme_power_of_sets}")
