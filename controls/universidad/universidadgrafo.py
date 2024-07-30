from controls.tda.graph.graphLabeledNoManaged import GraphLabeledNoManaged
from controls.tda.graph.graphLabeledManaged import GraphLabeledManaged
from controls.universidad.UniversidadDaoControl import UniversidadDaoControl
import os, sys

class UniversidadGrafo:
    def __init__(self):
        # Imprime la ruta del directorio actual
        print(sys.path[0])
        # Define el nombre del archivo JSON basado en el nombre del archivo actual
        self.__name = os.path.basename((__file__)).replace('.py', '.json')
        # Crea una instancia de UniversidadDaoControl
        self.__ndao = UniversidadDaoControl()
        self.__grafo = None
        
    def create_graph(self):
        # Obtiene la lista de UniversidadDaoControl
        list = self.__ndao._lista
        if list._length > 0:
            # Crea una instancia de GraphLabeledNoManaged con el tamaño de la lista
            self.__grafo = GraphLabeledNoManaged(list._length)
            # Convierte la lista a un array
            array = list.toArray
            # Etiqueta cada vértice del grafo con los elementos del array
            for i in range(0, len(array)):
                self.__grafo.labelVertex(i, array[i])
            # Pinta el grafo etiquetado
        else:
            # Lanza una excepción si la lista está vacía
            raise Exception("Vacio")

    @property
    def get_graph(self):
        # Crea el grafo si aún no ha sido creado
        self.create_graph()
        if self.__grafo is None:
            return []
        # Reconstruye el grafo etiquetado si existe el archivo
        if self.__grafo.existFileGraph(self.__name):
            self.__grafo = self.__grafo.recontruct_graph_labeled_with_lat_long(
                file=self.__name, atype=self.__grafo, model=UniversidadDaoControl)
        # Guarda el grafo etiquetado en un archivo
        self.__grafo.save_graph_labeled(file=self.__name)
        # Pinta el grafo etiquetado
        return self.__grafo   
    
    @property
    def save_graph(self):
        # Guarda el grafo etiquetado en un archivo
        self.__grafo.save_graph_labeled(file=self.__name)

    @property
    def obtainWeigths(self):
        if self.__grafo is not None:
            # Obtiene los pesos del grafo desde el archivo
            return self.__grafo.obtain_weigths(graph=self.__grafo, file=self.__name)
        return []
