import numpy as np

class Dijkstra:
    def __init__(self, graph: object = None, start: int = 0, end: int = 0):
        self.__graph = graph
        self.__start = start - 1 if start > 0 else 0 
        self.__end = end - 1 if end > 0 else 0
        self.__visited = [False] * self.__graph.num_vertex
        self.__distance = [np.inf] * self.__graph.num_vertex
        self.__parent = [-1] * self.__graph.num_vertex
        self.__camino = []

    def __minDistance(self):
        min = np.inf
        min_index = -1
        for i in range(0,self.__graph.num_vertex):
            if self.__visited[i]  == False and self.__distance[i] <= min:
                min = self.__distance[i]
                min_index = i
        return  min_index
    
    @property
    def __reconstruct_camino_mas_corto(self):
        crawl = self.__end
        camino = []
        while (self.__parent[crawl] != -1):
            camino.append(crawl+1)
            crawl = self.__parent[crawl]
        camino.append(self.__start+1)
        self.__camino = camino[::-1]
        if self.__distance[self.__end] == np.inf:
            self.__camino = None
            return "No hay camino"
        return camino

    @property
    def _paint_search_graph(self):
        camino = self.__camino
        if camino == None:
            newGraph = self.__graph.newGraph(0)
            newGraph.paint_search_graph()
            return
        newGraph = self.__graph.newGraph(len(camino))
        for i in range(0, len(camino)):
            newGraph.labelVertex(i, self.__graph.getLabel(camino[i]-1))
        for i in range(0, len(camino)):
            for j in range(0, len(camino)):
                if i != j:
                    newGraph.insert_edges_weigth(i, j, self.__graph.weigth_edges(camino[i]-1, camino[j]-1))
        print("ooooooo")
        newGraph.print_graph_labeled
        newGraph.paint_search_graph()
        return newGraph
    
    @property
    def __printPath__(self):
        print("Algoritmo de Dijkstra")
        print(f"El camino mas corto entre: " + str(self.__start + 1) + " y " + str(self.__end + 1))
        print(f"Distancia: " + str(self.__distance[self.__end]))
        print(f"Camino: ", self.__camino)
        print("Vertex \t\t Distance")
        for i in range(0, self.__graph.num_vertex):
            print(str(i+1) +  "\t\t" + str(self.__distance[i]))    

    @property
    def dijsktra(self):
        self.__distance[self.__start] = 0
        for i in range(0, self.__graph.num_vertex):
            u = self.__minDistance()
            self.__visited[u] = True
            for v in range(0, self.__graph.num_vertex):
                if self.__visited[v] == False and self.__graph.exist_edges(u, v) and self.__distance[u] + self.__graph.weigth_edges(u, v) < self.__distance[v]:
                    self.__distance[v] = self.__distance[u] + self.__graph.weigth_edges(u, v)
                    self.__parent[v] = u
        self.__reconstruct_camino_mas_corto
        self._paint_search_graph
        self.__printPath__
        return self.__distance[self.__end]        