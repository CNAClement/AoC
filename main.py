# Ouvre le fichier en mode lecture
with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2016\1_1.txt', 'r') as fichier:
    # Lit le contenu du fichier
    contenu = fichier.read()

# Divise le contenu en une liste de valeurs en utilisant la virgule comme délimiteur
valeurs = contenu.split(', ')
testvaleur = valeurs[1][1]
print(f"test valeur : {testvaleur}")

orientation = 'N'
x = 0
y = 0
localisation = []


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
    localisation.append(x,y)






print(f"x : {x} , y : {y}")

