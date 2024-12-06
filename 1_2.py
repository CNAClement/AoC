# Ouvre le fichier en mode lecture
with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2016\1_1.txt', 'r') as fichier:
    # Lit le contenu du fichier
    contenu = fichier.read()

# Divise le contenu en une liste de valeurs en utilisant la virgule comme délimiteur
valeurs = contenu.split(', ')


orientation = 'N'
x = 0
y = 0
localisation = [(0,0)]


# Parcourt la liste de valeurs
for indice, valeur in enumerate(valeurs, start=1):
    # print(f"Valeur {indice}: {valeur}")
    sens_mouvement = valeurs[indice-1][0]
    blocks = int(valeurs[indice-1][1:])
    if sens_mouvement == "R":
        if orientation == "N":
            orientation = 'E'
        elif orientation =='E':
            orientation = "S"
        elif orientation =='S':
            orientation = "O"
        else : orientation = 'N'
    else:
        if orientation == "N":
            orientation = 'O'
        elif orientation =='E':
            orientation = "N"
        elif orientation =='S':
            orientation = "E"
        else : orientation = 'S'

    if orientation == "N":
        y = y + blocks
    elif orientation == "S":
        y = y - blocks
    elif orientation == 'E':
        x = x + blocks
    else:
        x = x - blocks
    localisation.append((x,y))
    a = len(localisation)
    # print(f"localisation[a]={localisation[a - 1]}")
    #on itère pour voir si la dernière position (localisation[a] a déjà été trouvée avant.
    # Pour être puriste il faudrait mettre ce bloc avant le 1er mouvement et donc le premier append de localisation, mais en réalité on ne peut pas revenir à la position de départ dès le premier coup)
    for i in range(a-1):
        print(f"i = {i} et localisation(i) = {localisation[i]} et a = {a} et localisation(a) = {localisation[a-1]} " )
        if (localisation[a - 1]) == (localisation[i]):
            print(f"coordonnées trouvées en position ({x},{y}) à l'itération {a-1}")


print(f"x : {x} , y : {y}")





