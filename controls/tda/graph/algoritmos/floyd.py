from controls.tda.graph.graphLabeledNoManaged import GraphLabeledNoManaged
class Floyd:
    def __init__(self, graph: object = None, origen: int = 0, destino: int = 0):
        self.__graph = graph or GraphLabeledNoManaged()
        self.__origen = origen - 1 if origen > 0 else 0
        self.__destino = destino - 1 if destino > 0 else 0
        self.numV = self.__graph.num_vertex
        self.distanciaTotal = [[float('inf')] * self.numV for _ in range(self.numV)]
        self.siguiente = [[-1] * self.numV for _ in range(self.numV)]
        
        for i in range(self.numV):
            for j in range(self.numV):
                weight = self.__graph.getWeigth(i, j)
                if weight is not None:
                    self.distanciaTotal[i][j] = weight
                    self.siguiente[i][j] = j

    def buscarCaminos(self):
        for k in range(self.numV):
            for i in range(self.numV):
                for j in range(self.numV):
                    if self.distanciaTotal[i][k] + self.distanciaTotal[k][j] < self.distanciaTotal[i][j]:
                        self.distanciaTotal[i][j] = self.distanciaTotal[i][k] + self.distanciaTotal[k][j]
                        self.siguiente[i][j] = self.siguiente[i][k]

    def ruta(self):
        origen = self.__origen
        destino = self.__destino
        if self.siguiente[origen][destino] == -1:
            return []
        path = [origen]
        while origen != destino:
            origen = self.siguiente[origen][destino]
            if origen == -1:
                return []
            path.append(origen)
        for i in range(len(path)):
            path[i] += 1
        return path

    def distancia(self):
        return self.distanciaTotal[self.__origen][self.__destino]

    def caminoCorto(self):
        self.buscarCaminos()
        camino = self.ruta()
        distancia = self.distancia()
        return camino, distancia
