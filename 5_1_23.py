#3205909201 too high
#la réponse à la partie 2 est : 77435348, ce qui correspond à la graine 3205462429
with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\5_1_ori.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")

partie="partie2" #indique l'exercice à traiter

seeds=[]
seed_to_soil_map=[]
soil_to_fertilizer_map=[]
fertilizer_to_water_map=[]
water_to_light_map=[]
light_to_temperature_map=[]
temperature_to_humidity_map=[]
humidity_to_location_map=[]
liste_map=[seed_to_soil_map,soil_to_fertilizer_map,fertilizer_to_water_map,water_to_light_map,light_to_temperature_map,temperature_to_humidity_map,humidity_to_location_map]

remplissage_map = 0

def mapping(nombre,map):
    nombre = int(nombre)
    #print(f"map : {map}")
    nombre_mappé=0 #initialisation permettant plus tard de gérer le cas où le nombre n'est dans aucune range de map
    for ligne in range(1,len(map)): #on ne prend pas en compte la première ligne de map, qui est un "titre"
        map_for = map[ligne].split()
        #print(f"map traitée: {map[0]} sur l'instruction' : {map[ligne]}")
        map_for[0] = int(map_for[0])
        map_for[1] = int(map_for[1])
        map_for[2] = int(map_for[2])
        if nombre in range(map_for[1],map_for[1]+map_for[2]):
            position=nombre - map_for[1] #(exemple le nombre 20 est en position 20-5 de la range qui va de 5 à 30, rajouter+1 si on parle en français et pas en Python)
            nombre_mappé=map_for[0]+position
            #print(f"Le nombre {nombre} est bien en range de {map_for[1]} à {map_for[1]+map_for[2]}, en position {position+1}\nL'instruction correspondante est {map_for} (sur la map {map[0]})")
            #print(f"Le nombre mappé est : {nombre_mappé}")
    if nombre_mappé==0 : #on ne l'a trouvé dans aucune range de map
        #print(f"le nombre {nombre} n'a été trouvé dans aucune des instructions de la map {map[0]}")
        nombre_mappé=nombre
    #print(f"on en est au nombre {nombre_mappé} pour la map {map[0]}")
    return nombre_mappé

for ligne in lignes:
    if ligne[0:6]=="seeds:":
        remplissage_map = seeds
    elif ligne=="seed-to-soil map:":
        remplissage_map=seed_to_soil_map
    elif ligne=="soil-to-fertilizer map:":
        remplissage_map=soil_to_fertilizer_map
    elif ligne=="fertilizer-to-water map:":
        remplissage_map=fertilizer_to_water_map
    elif ligne=="water-to-light map:":
        remplissage_map=water_to_light_map
    elif ligne=="light-to-temperature map:":
        remplissage_map=light_to_temperature_map
    elif ligne=="temperature-to-humidity map:":
        remplissage_map=temperature_to_humidity_map
    elif ligne=="humidity-to-location map:":
        remplissage_map=humidity_to_location_map
    elif ligne == "" :
        remplissage_map=0

    if remplissage_map != 0:
        remplissage_map.append(ligne)

seeds = seeds[0][7:]  #on enlève le début de la phrase "seeds:"
print(f"longueur seeds={len(seeds)}")

numero_ligne=0
print(f"liste des maps : {liste_map}")

localisations = []
if partie=="partie1":
    seeds_a_traiter=seeds.split()
    print(f"liste des seeds à traiter {seeds_a_traiter}")
    for seed in seeds_a_traiter:
        seed = int(seed)
        nombre_mappé = seed
        for map in liste_map:
            nombre_mappé = mapping(nombre_mappé, map)
        # print(f"la localisation est : {nombre_mappé}")
        localisations.append(nombre_mappé)
    print(f"la réponse à la partie 1 est : {min(localisations)}")
elif partie=="partie2":
    seeds_split=seeds.split()
    for indice in range(0,len(seeds_split),2):  #on utilise un pas de 2
        #print(f"début de la range : {int(seeds_split[indice])}, fin de la range : {int(seeds_split[indice])}+{int(seeds_split[indice+1])} = {int(seeds_split[indice])+int(seeds_split[indice+1])}")
        #for seed in range(  int(seeds_split[indice]),   int(seeds_split[indice])+int(seeds_split[indice+1]), 5000 ):
        for seed in range(  3205462429 - 10000,   3205462429 + 10000 ):
            seed = int(seed)
            nombre_mappé = seed
            for map in liste_map:
                nombre_mappé = mapping(nombre_mappé, map)
            # print(f"la localisation est : {nombre_mappé}")
            localisations.append((nombre_mappé,seed))
    print(f"la réponse à la partie 2 est : {min(localisations)[0]}, ce qui correspond à la graine {min(localisations)[1]}")
    #print(f"la réponse à la partie 2 est : {min(localisations)[0]}, ce qui correspond à la graine {min(localisations)[1]}")
else: print(f"la partie à traiter {partie} n'existe pas, c'est soit 'partie1' soit 'partie2'")