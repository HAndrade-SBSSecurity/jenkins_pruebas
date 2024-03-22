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
    lista = update_list(lista)  # Actualizar la lista
    subprocess.run(["git", "add", "do.py"])  # Agregar el archivo do.py al área de preparación
    subprocess.run(["git", "commit", "-m", "Actualización lista"])  # Hacer commit
    subprocess.run(["git", "pull"])  # Realizar un pull en el repositorio
    subprocess.run(["git", "push"])  # Realizar el push al repositorio
    print("git lista:" + lista + "lista en git")
    time.sleep(20)  # Esperar 1 minuto
    """if len(lista) % 3 == 0:  # Cada 3 minutos
        subprocess.run(["git", "pull"])  # Realizar un pull en el repositorio
        subprocess.run(["git", "add", "."])  # Agregar todos los cambios
        subprocess.run(["git", "commit", "-m", "Actualización automática"])  # Hacer commit
        subprocess.run(["git", "push"])  # Realizar un push"""