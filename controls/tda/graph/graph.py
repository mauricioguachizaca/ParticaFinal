import sys
import os, json
import geopy.distance
import static.d3

from math import nan, sin, cos, sqrt, atan2, radians, asin 

class Graph:
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        static_dir = os.path.join(current_dir, 'static')
        
        d3_dir = os.path.join(static_dir, 'd3')
        
        self.__URLFILESGRAPH = os.path.join(d3_dir, 'graph.js')
        self.__URLFILEGRAPHJSON = os.path.join(d3_dir, 'graphs.json')

    @property
    def num_vertex(self):
        raise NotImplementedError("Please implement this method")

    @property
    def num_edges(self):
        raise NotImplementedError("Please implement this method")
    
    def exist_edges(self, v1, v2):
        raise NotImplementedError("Please implement this method")
    
    def weigth_edges(self, v1, v2):
        raise NotImplementedError("Please implement this method")
    
    def insert_edges_weigth(self, v1, v2, weigth):
        raise NotImplementedError("Please implement this method")
    
    def insert_edges(self, v1, v2):
        raise NotImplementedError("Please implement this method")
    
    def adjacent(self, v1):
        raise NotImplementedError("Please implement this method")
    
    def getLabel(self, vertex):
        raise NotImplementedError("Please implement this method")
    
    def getVertex(self, label):
        raise NotImplementedError("Please implement this method")

    def newGraph(self, num_vertex):
        raise NotImplementedError("Please implement this method")
    

    def existFileGraph(self, file):
        url = self.__URLFILEGRAPHJSON + file
        return os.path.exists(url)
    
    def __str__(self) -> str:
        out = ""
        for i in range(0, self.num_vertex):
            out += "V" + str(i) + " -> "
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    out += "ady V" + str(adj._destination + 1) + " weigth " + str(adj._weigth) + " -> \n"
        return out
    

    @property
    def print_graph(self):
        print(self.__str__())

    @property
    def print_graph_labeled(self):
        out = ""
        for i in range(0, self.num_vertex):
            out += "V" + str(i) + " -> " + str(self.getLabel(i)) + " -> "
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    out += "ady V" + str(adj._destination + 1) + " weigth " + str(adj._weigth) + " -> \n"
        print(out)

    def __transform_graphLabeled__(self):
        json_str = "["
        for i in range(0, self.num_vertex):
            adjs = self.adjacent(i)
            json_str += '\n\t{\n\t\t"labelId":' + f"{str(self.getVertex(self.getLabel(i)) + 1)},"
            if not adjs.isEmpty:
                json_str += '\n\t\t"destinations": ['
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    json_str += '\n\t\t\t{\n\t\t\t\t"from":' + f"{str(self.getVertex(self.getLabel(i)) + 1)}" + ', \n\t\t\t\t"to":' + f"{str(self.getVertex(self.getLabel(adj._destination)) + 1)}" + ', \n\t\t\t\t"weigth":' + str(adj._weigth) + '\n\t\t\t},'
                json_str = json_str[:-1]
                json_str += '\n\t\t]'
                json_str += '\n\t},'
            else:
                json_str += '\n\t\t"destinations": []\n'
                json_str = json_str[:-1]
                json_str += '\n\t},'
        json_str = json_str[:-1]
        json_str += '\n]'
        return json_str

    def save_graph_labeled(self, file='graph.json'):
        url = self.__URLFILEGRAPHJSON + file
        a = open(url, 'w')
        a.write(self.__transform_graphLabeled__())
        a.close()

    def recontruct_graph_labeled_with_lat_long(self, file='graph.json', atype: object = None, model: object = None):
        url = self.__URLFILEGRAPHJSON + file
        a = open(url, 'r')
        data = json.load(a)
        a.close()
        newGraph = atype
        newModel = model()._lista

        modelos = []
        for item in data:
            model = newModel.get(item['labelId'] - 1)
            newGraph.labelVertex(item['labelId'] - 1, model)
            modelos.append(model)
        for item in data:
            destination = item['destinations']
            if destination != []:
                for dest in item['destinations']:
                    distancia = calculate_weigth_geographic(modelos[dest['from'] - 1], modelos[dest['to'] - 1])
                    newGraph.insert_edges_weigth(dest['from'] - 1, dest['to'] - 1, distancia)
        return newGraph
    
    def obtain_weigths(self, graph: object = None, file='graph.json'):
        print(graph)
        out = []
        for i in range(0, graph.num_vertex):
            info = {}
            adjs = graph.adjacent(i)
            if not adjs.isEmpty:
                info['labelId'] = graph.getVertex(graph.getLabel(i)) + 1
                info['destinations'] = []
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    info['destinations'].append({
                        'from': graph.getVertex(graph.getLabel(i)) + 1,
                        'to': adj._destination + 1,
                        'weigth': adj._weigth
                    })
                out.append(info)
        return out

def calculate_weigth_geographic(model1: object = None, model2: object = None):
    R = 6371.01  
    lat1 = model1._latitud
    lon1 = model1._longitud
    lat2 = model2._latitud
    lon2 = model2._longitud
    distancia = geopy.distance.distance((lat1, lon1), (lat2, lon2)).km
    return round(distancia, 2)
