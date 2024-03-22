import subprocess
import time
import os

# Función para actualizar la lista
def update_list(lista):
    lista.append(len(lista))  # Agregar un elemento a la lista
    print(lista)
    return lista

# Verificar si la carpeta "do" ya existe
"""if not os.path.exists("do"):
    subprocess.run(["git", "clone", "https://github.com/HAndrade-SBSSecurity/do.git"])"""

lista = []  # Inicializar lista vacía
while True:
    print(f"lista comienzo while: {lista}")
    lista = update_list(lista)  # Actualizar la lista
    subprocess.run(["git", "add", "."])  # Agregar el archivo do.py al área de preparación
    subprocess.run(["git", "commit", "-m", "Actualización lista"])  # Hacer commit
    subprocess.run(["git", "pull"])  # Realizar un pull en el repositorio
    subprocess.run(["git", "push"])  # Realizar el push al repositorio
    print(f"git lista: {lista}")
    subprocess.run(["python", "to_do.py"])
    time.sleep(10)  # Esperar 1 minuto