from controls.tda.graph.graphLabeledManaged import GraphLabeledManaged
from controls.exception.arrayPositionException import ArrayPositionException
from math import nan

class GraphLabeledNoManaged(GraphLabeledManaged):
    def _init_(self, num_vert):
        super()._init_(num_vert)
        self.__labels = []
        for i in range(0, self.num_vertex):
            self.__labels.append(None)

    def insert_edges_weight_E(self, label1, label2, weight):
        v1 = self.getVertex(label1)
        v2 = self.getVertex(label2)
        if v1 == -1 or v2 == -1:
            self.insert_edges_weight(v1, v2, weight)
            self.insert_edges_weight(v2, v1, weight) 
        else:
            raise ArrayPositionException("Vertex not found")
        
    def insert_edges_weigth(self, v1, v2, weigth):
        super().insert_edges_weigth(v2, v1, weigth)
        super().insert_edges_weigth(v1, v2, weigth)

    def getWeigth(self, v1, v2):
        return super().weigth_edges(v1, v2)
    
    def getLabel(self, v):
        return super().getLabel(v)