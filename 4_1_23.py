#13759672 too low
with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\4_1_ori.txt', 'r') as fichier:
    contenu = fichier.read()
    lignes = contenu.splitlines()
print(f"taille du fichier : {len(contenu)}")
print(f"nombre de lignes : {len(lignes)}")


def separation_donnees(ligne):
    separation_idgame_numeros = ligne.split(sep=":")
    #print(f"id game = {separation_idgame_numeros[0]} et numéros = {separation_idgame_numeros[1]}")
    separation_winning_actual = separation_idgame_numeros[1].split(sep="|")
    #print(f"numéros gagnants = {separation_winning_actual[0]} et numéros possédés = {separation_winning_actual[1]}")
    numeros_gagnants=separation_winning_actual[0].split(sep=" ")
    numeros_possedes=separation_winning_actual[1].split(sep=" ")
    return numeros_gagnants,numeros_possedes

#def comparaison_numeros_exo1(numeros_gagnants,numeros_possedes):
#    nombre_numeros_gagnants=0
#    for numero_gagnant in numeros_gagnants:
#        if numero_gagnant in numeros_possedes and numero_gagnant != " " and numero_gagnant != "" :
#            nombre_numeros_gagnants+=1
#    if nombre_numeros_gagnants==0:
#        valeur_carte=0
#    else :
#        valeur_carte= 2**(nombre_numeros_gagnants-1)
#    print(f"valeur carte = {valeur_carte}")
#    return valeur_carte

def comparaison_numeros(numeros_gagnants,numeros_possedes):
    nombre_numeros_gagnants=0
    for numero_gagnant in numeros_gagnants:
        if numero_gagnant in numeros_possedes and numero_gagnant != " " and numero_gagnant != "" :
            nombre_numeros_gagnants+=1
    return nombre_numeros_gagnants #nombre de numéros gagnants par copie de la carte

def gain_copies(numero_carte, nombre_instances,nombre_numeros_gagnants):
    if numero_carte+nombre_numeros_gagnants<=len(lignes):
        for numero_copie in range(numero_carte+1,numero_carte+nombre_numeros_gagnants+1):
            nombre_instances[numero_copie-1]+=1*nombre_instances[numero_carte-1]
            #pas très utile de faire +1 et -1 derrière mais au moins c'est plus clair du fait que l'on parle de la copie de la carte n°3 (qui correspond à l'index [2] )
    else :
        for numero_copie in range(numero_carte+1, len(lignes)):
            nombre_instances[numero_copie]+=1*nombre_instances[numero_carte]
    print(nombre_instances)

#valeur_cartes=0
numero_carte=0
nombre_instances = [1]*len(lignes)
print(f"nombre d'instances : {nombre_instances}")
for ligne in lignes :
    numero_carte+=1
    print(f"traitement ligne {ligne}")
    numeros_gagnants,numeros_possedes=separation_donnees(ligne)
    nombre_numeros_gagnants=comparaison_numeros(numeros_gagnants,numeros_possedes)
    gain_copies(numero_carte, nombre_instances, nombre_numeros_gagnants)

nombre_scratchcards = 0
for nombre in nombre_instances:
    nombre_scratchcards+=nombre
#print(f"la réponse à la partie 1 est : {valeur_cartes}")
print(f"la réponse à la partie 2 est : {nombre_scratchcards}")




