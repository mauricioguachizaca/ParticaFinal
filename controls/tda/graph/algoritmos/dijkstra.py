import numpy as np
from controls.tda.graph.graphLabeledNoManaged import GraphLabeledNoManaged
class Dijkstra:
    def __init__(self, graph: object = None, origen: int = 0, destino: int = 0):
        self.__graph = graph or GraphLabeledNoManaged()
        self.__origen = origen - 1 if origen > 0 else 0
        self.__destino = destino-1 if destino > 0 else 0
        self._visitado = [False] * self.__graph.num_vertex
        self._distancia = [np.inf] * self.__graph.num_vertex
        self._parent = [-1] * self.__graph.num_vertex
        self.__camino = []
    
    def caminoCorto(self):
        self._distancia[self.__origen] = 0
        for _ in range(self.__graph.num_vertex):
            u = self._minimo()
            self._visitado[u] = True
            for v in range(self.__graph.num_vertex):
                if not self._visitado[v] and self.__graph.getWeigth(u, v) != None:
                    if self._distancia[u] + self.__graph.getWeigth(u, v) < self._distancia[v]:
                        self._distancia[v] = self._distancia[u] + self.__graph.getWeigth(u, v)
                        self._parent[v] = u
        self.__camino = self._camino()
        distancia = self.distanciaRecorrida()
        return self.__camino , distancia
    
    def _camino(self):
        camino = []
        destino = self.__destino
        while destino != -1:
            camino.insert(0, destino)
            destino = self._parent[destino]
        for i in range(len(camino)):
            camino[i] += 1
        return camino

    def _minimo(self):
        minimo = np.inf
        for v in range(self.__graph.num_vertex):
            if not self._visitado[v] and self._distancia[v] < minimo:
                minimo = self._distancia[v]
                u = v
        return u
    
    def distanciaRecorrida(self):
        return self._distancia[self.__destino]
    
    
    
   