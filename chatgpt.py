def find_first_duplicate_location_with_info(instructions):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_direction = 0
    x, y = 0, 0
    localisation = set([(0, 0)])  # Utilise un ensemble pour améliorer les performances lors de la recherche

    for indice, valeur in enumerate(instructions, start=1):
        sens_mouvement = valeur[0]
        blocks = int(valeur[1:])
        if sens_mouvement == "R":
            current_direction = (current_direction + 1) % 4
        else:
            current_direction = (current_direction - 1) % 4

        for pas in range(blocks):
            if current_direction == 0:
                y += 1
            elif current_direction == 1:
                x += 1
            elif current_direction == 2:
                y -= 1
            else:
                x -= 1

            current_location = (x, y)
            if current_location in localisation:
                distance = abs(x) + abs(y)
                return distance, (x, y), indice, pas + 1

            localisation.add(current_location)

    # Si aucune position n'est visitée deux fois
    return None, None, None, None

# Instructions fournies
instructions = ["R4", "R3", "R5", "L3", "L5", "R2", "L2", "R5", "L2", "R5", "R5", "R5", "R1", "R3", "L2", "L2", "L1", "R5", "L3", "R1", "L2", "R1", "L3", "L5", "L1", "R3", "L4", "R2", "R4", "L3", "L1", "R4", "L4", "R3", "L5", "L3", "R188", "R4", "L1", "R48", "L5", "R4", "R71", "R3", "L2", "R188", "L3", "R2", "L3", "R3", "L5", "L1", "R1", "L2", "L4", "L2", "R5", "L3", "R3", "R3", "R4", "L3", "L4", "R5", "L4", "L4", "R3", "R4", "L4", "R1", "L3", "L1", "L1", "R4", "R1", "L4", "R1", "L1", "L3", "R2", "L2", "R2", "L1", "R5", "R3", "R4", "L5", "R2", "R5", "L5", "R1", "R2", "L1", "L3", "R3", "R1", "R3", "L4", "R4", "L4", "L1", "R1", "L2", "L2", "L4", "R1", "L3", "R4", "L2", "R3", "L1", "L5", "R4", "R5", "R2", "R5", "R1", "R5", "R1", "R3", "L3", "L2", "L2", "L5", "R2", "L2", "R5", "R5", "L2", "R3", "L5", "R5", "L2", "R4", "R2", "L1", "R3", "L5", "R3", "R2", "R5", "L1", "R3", "L2", "R2", "R1"]

# Utilisation avec les instructions fournies
result, coordinates, iteration, step = find_first_duplicate_location_with_info(instructions)
print(f"Résultat : {result} blocs, Coordonnées : {coordinates}, Itération : {iteration}, Pas : {step}")
