import os
import importlib #permet de faire des imports dynamiques
import time
#68008093867584115146642116657 too high

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def recuperation_donnees(jour, chemin_fichier):
    import requests
    from dotenv import load_dotenv  # permet de récupérer les variables d'environnement stockée dans un fichier.
    load_dotenv("var.env")

    cookie_session = os.getenv("COOKIE_SESSION")
    cookies = { 'session': cookie_session }
    url = f"https://adventofcode.com/2024/day/{jour}/input"


    # Envoyer la requête GET avec le cookie
    response = requests.get(url, cookies=cookies)

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Écrire le contenu dans un fichier texte
        with open(chemin_fichier, 'w') as f:
            f.write(response.text)
        print(f"Contenu du site récupéré et chargé dans {chemin_fichier} .")
    else:
        print(f"Erreur lors de l'accès à la page : {response.status_code}")

if __name__ == '__main__':
    test = False
    jour = 11
    partie = 1
    chemin_fichier=rf"C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2024\{jour}_test.txt" if test \
            else rf"C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2024\{jour}.txt"

    print(f"on traite le fichier : {chemin_fichier}")

    script_jour = f"jour{jour}_partie{partie}"
    fonction_jour = f"execution_jour{jour}_partie{partie}"
    start = time.time()

    # Si nécessaire, on récupère les données sur le site.
    if (test == False and not os.path.exists(chemin_fichier) ) :
        recuperation_donnees(jour, chemin_fichier)

    try:
        module = importlib.import_module(script_jour)
        fonction = getattr(module, fonction_jour)
        fonction(chemin_fichier)
    except (ModuleNotFoundError, AttributeError) as e:
        print(f"Erreur : {e}")
    print(f"réponse en {time.time() - start} secondes.")


