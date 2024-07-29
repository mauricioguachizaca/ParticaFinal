import sys
import os

# Agrega el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

print("PYTHONPATH:", sys.path)

from controls.universidad.universidadgrafo import UniversidadGrafo

def main():
    try:
        universidad_grafo = UniversidadGrafo()
        grafo = universidad_grafo.get_graph
        print("Grafo creado y guardado con éxito:")
        print(grafo)
        universidad_grafo.save_graph
        pesos = universidad_grafo.obtainWeigths
        print("Pesos del grafo:")
        print(pesos)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

