from controls.tda.graph.graphManaged import GraphManaged
from controls.exception.arrayPositionException import ArrayPositionException
from math import nan

class GraphLabeledManaged(GraphManaged):
    def __init__(self, num_vert) -> None:
        super().__init__(num_vert)
        self.__labels = []
        self.__labelsVertx = {}
        for i in range(0, self.num_vertex):
            self.__labels.append(None)

    def getVertex(self, label):
        try:
            return self.__labelsVertx[str(label)]
        except Exception as error:
            return -1 
    
    def label_vertex(self, v, label):
        self.__labels[v] = label
        self.__labelsVertx[str(label)] = v

    def getLabel(self, v):
        return self.__labels[v]
    
    def exist_edge(self, label1, label2):
        v = self.getVertex(label1) 
        v2 = self.getVertex(label2)
        if v != -1 and v2 != -1:
            return self.exist_edge(v, v2)
        else:
            return False
        
    def insert_edges_weigth_E(self, label1, label2, weigth):
        v1 = self.getVertex(label1)
        v2 = self.getVertex(label2)
        if v1 != -1 and v2 != -1:
            self.insert_edges_weigth(v1, v2, weigth)
        else:
            raise ArrayPositionException("Vertex not found")
        
    def insert_edges_E(self, label1, label2):
        self.insert_edges_weigth_E(label1, label2, nan)

    def weigth_edges_E(self, label1, label2):
        v1 = self.getVertex(label1)
        v2 = self.getVertex(label2)
        if v1 != -1 and v2 != -1:
            return self.weigth_edges(v1, v2)
        else:
            raise ArrayPositionException("Vertex not found")
        
    def adjacent_E(self, label):
        v = self.getVertex(label)
        if v != -1:
            return self.adjacent(v)
        else:
            raise ArrayPositionException("Vertex not found")