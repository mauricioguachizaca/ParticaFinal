import sys
import os
import time

# Añadir la ruta raíz del proyecto a sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(root_dir)

from controls.universidad.universidadgrafo import UniversidadGrafo
from controls.tda.graph.algoritmos.dijkstra import Dijkstra
from controls.tda.graph.algoritmos.floyd import Floyd

def measure_time(graph, start, end):
    floyd = Floyd(graph, start, end)
    start_time = time.time()
    floyd.floydWarshall
    end_time = time.time()
    return end_time - start_time

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

        # Medir el tiempo de ejecución del algoritmo de Floyd-Warshall
        start_vertex = 1  # Ejemplo, puedes ajustar según tus necesidades
        end_vertex = grafo.num_vertex  # Ejemplo, puedes ajustar según tus necesidades
        time_taken = measure_time(grafo, start_vertex, end_vertex)
        print(f"Tiempo de ejecución del algoritmo de Floyd-Warshall: {time_taken:.6f} segundos")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
