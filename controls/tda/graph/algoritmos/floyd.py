import numpy as np

class Floyd:
    def __init__(self, graph: object = None, start: int = 0, end: int = 0):
        self.__graph = graph 
        self.__start = start - 1 if start > 0 else 0  
        self.__end = end - 1 if end > 0 else 0 
        self.__matrix = np.full((self.__graph.num_vertex, self.__graph.num_vertex), np.inf)
        self.__distance = np.full((self.__graph.num_vertex, self.__graph.num_vertex), -1)
        self.__parent = np.full((self.__graph.num_vertex, self.__graph.num_vertex), -1)
        self.__camino = None

    @property
    def initMatrix(self):
        for i in range(self.__graph.num_vertex):
            for j in range(self.__graph.num_vertex):
                if i == j:
                    self.__matrix[i][j] = 0 
                elif self.__graph.exist_edges(i, j):
                    self.__matrix[i][j] = self.__graph.weigth_edges(i, j)  
                else:
                    self.__matrix[i][j] = np.inf  

    @property
    def __reconstruct_camino_mas_corto(self):
        path = []
        if self.__matrix[self.__start][self.__end] == np.inf:
            return None  #
        crawl = self.__start
        path.append(crawl + 1)  
        while crawl != self.__end:
            crawl = self.__parent[crawl][self.__end] 
            path.append(crawl + 1)  
        self.__camino = path[::-1] 
        return self.__camino
        
    @property
    def __printPath__(self):
        # Imprime el resultado del algoritmo de Floyd-Warshall
        print("Algoritmo de Floyd")
        print(f"El camino más corto entre: {self.__start + 1} y {self.__end + 1} es:")
        print(f"Distancia: {self.__matrix[self.__start][self.__end]}")
        print(f"Camino:", self.__camino)
        print("Vertex \t\t Distance")
        for i in range(self.__graph.num_vertex):
            print(f"{i + 1} \t\t {self.__matrix[i][self.__end]}")

    @property
    def floydWarshall(self):
        self.initMatrix 
        for i in range(self.__graph.num_vertex):
            for j in range(self.__graph.num_vertex):
                if self.__matrix[i][j] != np.inf:
                    self.__distance[i][j] = j
                    self.__parent[i][j] = i
        
        for k in range(self.__graph.num_vertex):
            for i in range(self.__graph.num_vertex):
                for j in range(self.__graph.num_vertex):
                    if self.__matrix[i][j] > self.__matrix[i][k] + self.__matrix[k][j]:
                        self.__matrix[i][j] = self.__matrix[i][k] + self.__matrix[k][j]
                        self.__distance[i][j] = self.__distance[i][k]
                        self.__parent[i][j] = self.__parent[k][j]
            
        self.__reconstruct_camino_mas_corto
        self.__printPath__
        return self.__matrix[self.__start][self.__end]  