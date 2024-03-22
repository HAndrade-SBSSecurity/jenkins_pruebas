"""import requests

# Variables con los datos de los repositorios
repo_do_url = "https://api.github.com/repos/HAndrade-SBSSecurity/do/contents"
repo_to_do_url = "https://api.github.com/repos/HAndrade-SBSSecurity/to_do/contents"
headers = {"HAndrade-SBSSecurity": "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"}

# Función para clonar el repositorio "do" y copiar el contenido al repositorio "to do"
def copy_repo_contents(source_url, dest_url):
    response = requests.get(source_url, headers=headers)
    files = response.json()

    for file in files:
        if file["type"] == "file":
            response_file = requests.get(file["download_url"], headers=headers)
            content = response_file.json()["content"]

            data = {
                "message": "Copiar archivo " + file["name"],
                "content": content,
                "branch": "main"
            }

            requests.put(dest_url + "/" + file["name"], headers=headers, json=data)

        elif file["type"] == "dir":
            copy_repo_contents(file["url"], dest_url + "/" + file["name"])

# Clonar el repositorio "do" y copiar el contenido al repositorio "to do"
copy_repo_contents(repo_do_url, repo_to_do_url)"""

import subprocess
import sys

def export_list(lista):
    # Puedes realizar cualquier operación que necesites con la lista aquí
    # Por ejemplo, imprimir la lista
    with open("lista.txt", "r") as file:
        lista = file.read().splitlines()
    print(lista)
    # Subir la lista al repositorio de GitHub
    subprocess.run(["git", "add", "lista.txt"])  # Agregar el archivo lista.txt al área de preparación
    subprocess.run(["git", "commit", "-m", "Actualización de lista"])  # Hacer commit
    subprocess.run(["git", "pull"])  # Realizar un pull en el repositorio
    subprocess.run(["git", "push"])  # Realizar el push al repositorio


if __name__ == "__main__":
    # Obtener la lista pasada como argumento desde el script principal
    lista = sys.argv[1:]

    # Llamar a la función para exportar la lista
    
    export_list(lista)
