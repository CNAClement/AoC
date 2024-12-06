with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2016\2_1_ori.txt', 'r') as fichier:
    contenu= fichier.read()
    ligne = contenu.splitlines()
print(ligne)
print(ligne[0])
print(ligne[1])

print(contenu[1])
print(f"taille du fichier : {len(contenu)} " )
print(f"nombre de lignes : {len(ligne)}")


for numero_ligne in range(len(ligne)):
    position_actuelle = '5'
    print(f"traitement de la ligne {numero_ligne+1}")

    for indice in range(len(ligne[numero_ligne])):
        #exemple : numero_ligne = 2 , alors ligne[numero_ligne] = contenu de la 3eme ligne, alors len(ligne[numero_ligne])  = longueur de cette ligne
        instruction=ligne[numero_ligne][indice]
        #on se place sur une ligne donnée et on parcourt tous ses caractères du premier jusqu'au dernier caractère
        if position_actuelle == '1':
            if instruction == 'L':
                position_actuelle = '1'
            elif instruction == 'U':
                position_actuelle = '1'
            elif instruction == 'D' :
                position_actuelle = '4'
            elif instruction == 'R' :
                position_actuelle = '2'
        elif  position_actuelle == '2' :
            if instruction == 'L':
                position_actuelle = '1'
            elif instruction == 'U':
                position_actuelle = '2'
            elif instruction == 'D' :
                position_actuelle = '5'
            elif instruction == 'R' :
                position_actuelle = '3'
        elif  position_actuelle == '3' :
            if instruction == 'L':
                position_actuelle = '2'
            elif instruction == 'U':
                position_actuelle = '3'
            elif instruction == 'D' :
                position_actuelle = '6'
            elif instruction == 'R' :
                position_actuelle = '3'
        elif  position_actuelle == '4' :
            if instruction == 'L':
                position_actuelle = '3'
            elif instruction == 'U':
                position_actuelle = '1'
            elif instruction == 'D' :
                position_actuelle = '7'
            elif instruction == 'R' :
                position_actuelle = '5'
        elif  position_actuelle == '5' :
            if instruction == 'L':
                position_actuelle = '4'
            elif instruction == 'U':
                position_actuelle = '2'
            elif instruction == 'D' :
                position_actuelle = '8'
            elif instruction == 'R' :
                position_actuelle = '6'
        elif  position_actuelle == '6' :
            if instruction == 'L':
                position_actuelle = '5'
            elif instruction == 'U':
                position_actuelle = '3'
            elif instruction == 'D' :
                position_actuelle = '9'
            elif instruction == 'R' :
                position_actuelle = '6'
        elif  position_actuelle == '7' :
            if instruction == 'L':
                position_actuelle = '7'
            elif instruction == 'U':
                position_actuelle = '4'
            elif instruction == 'D' :
                position_actuelle = '7'
            elif instruction == 'R' :
                position_actuelle = '8'
        elif  position_actuelle == '8' :
            if instruction == 'L':
                position_actuelle = '7'
            elif instruction == 'U':
                position_actuelle = '5'
            elif instruction == 'D' :
                position_actuelle = '8'
            elif instruction == 'R' :
                position_actuelle = '9'
        elif  position_actuelle == '9' :
            if instruction == 'L':
                position_actuelle = '8'
            elif instruction == 'U':
                position_actuelle = '6'
            elif instruction == 'D' :
                position_actuelle = '9'
            elif instruction == 'R' :
                position_actuelle = '9'
    print(f"position actuelle : {position_actuelle}")