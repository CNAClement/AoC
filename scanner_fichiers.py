import os


def search_string_in_python_files(directory, search_string):
    """
    Parcourt tous les fichiers .py d'un répertoire pour rechercher une chaîne de caractères.

    Args:
        directory (str): Chemin du répertoire à analyser.
        search_string (str): La chaîne de caractères à rechercher.
    """
    for file in os.listdir(directory):  # Liste uniquement les fichiers/dossiers du répertoire courant
        file_path = os.path.join(directory, file)

        # Vérifie que c'est un fichier Python
        if os.path.isfile(file_path) and file.endswith(".py"):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if search_string in line:
                        print(f"Found in {file_path} (Line {i + 1}): {line.strip()}")
            except (UnicodeDecodeError, PermissionError) as e:
                print(f"Skipping {file_path} due to error: {e}")


if __name__ == "__main__":
    # Répertoire courant
    directory_to_search = os.getcwd()
    search_for = "rayon"

    print(f"Searching for '{search_for}' in Python files in directory: {directory_to_search}")
    search_string_in_python_files(directory_to_search, search_for)
