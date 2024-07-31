from controls.tda.graph.graphLabeledNoManaged import GraphLabeledNoManaged
from controls.universidad.UniversidadDaoControl import UniversidadDaoControl
from controls.tda.graph.algoritmos.dijkstra import Dijkstra
from controls.tda.graph.algoritmos.floyd import Floyd

import os, sys

class UniversidadGrafo:
    def __init__(self) -> None:
        self.__name = "UniversidadGrafo.json"
        self.__grafo = None
        self.__ndao = UniversidadDaoControl()
        self.vertex_names = []
    
    def create_graph(self):
        list = self.__ndao._list()
        if list._lenght > 0:
            self.__grafo = GraphLabeledNoManaged(list._lenght)
            arr = list.toArray
            for i in range(0, len(arr)):
                self.__grafo.label_vertex(i, arr[i]._nombre)
                self.vertex_names.append(arr[i]._nombre)
            self.__grafo.paint_graph()
        return self.__grafo
    
    @property
    def save_graph(self):
        return self.__grafo.save_graph_label(filename= "UniversidadGrafo.json")
    
    @property
    def obtainWeigth(self):
        return self.__grafo.obtain_weigths(grafo=self.__grafo, filename="UniversidadGrafo.json")
    
    @property
    def DarGrafo(self):
        self.create_graph()
        print(self.__name)
        if self.__grafo.existeArchivo(self.__name):
            self.__grafo = self.__grafo.load_graph(filename=self.__name, atype=self.__grafo, model=UniversidadDaoControl)
        self.__grafo.save_graph_label(filename=self.__name)
        return self.__grafo
        
    def caminoCorto(self, origen: int, destino: int, algoritmo: int):
        if algoritmo == 1:
            busqueda = Dijkstra(self.__grafo, origen, destino)
        else:
            busqueda = Floyd(self.__grafo, origen, destino)
        return busqueda.caminoCorto()