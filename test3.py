from utils_clement import *
import math #petite aide pour trouver le signe donc le sens de déplacement de manière optimisée

mode = "test_small" # "test_small", "test_large" , "reel"
chemin_fichier_map = fr"C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2024\15_{mode}_map.txt"
chemin_fichier_deplacement = fr"C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2024\15_{mode}_deplacement.txt"


lignes_map = lecture_fichier(chemin_fichier_map)
tableau = chargement_tableau(lignes_map)
print(tableau)

print(lignes_map)

