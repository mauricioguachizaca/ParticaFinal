import sys
import os , json 
import geopy.distance
from math import nan, sin, cos, sqrt, atan2, radians, asin 
class Graph:
    def __init__(self):
        self.__URL = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(os.path.abspath(__file__)))))) + '/static/'
        self.__URLFILESGRAPH = self.__URL + '/static/js/graph'
        self.__URLFILEGRAPHJSON = self.__URL + '/data/graphs/'

    @property
    def num_vertex(self):
        raise NotImplementedError("Please implement this method")
    @property
    def num_edges(self):
        raise NotImplementedError("Please implement this method")
    
    def exist_edges(self, v1, v2):
        raise NotImplementedError("Please implement this method")
    
    def weigth_edges(self, v1,v2):
        raise NotImplementedError("Please implement this method")
    
    def insert_edges_weigth(self, v1, v2, weigth):
        raise NotImplementedError("Please implement this method")
    
    def insert_edges(self, v1, v2):
        raise NotImplementedError("Please implement this method")
    
    def adjacent(v1):
        raise NotImplementedError("Please implement this method")
    """ def setLabel(self, vertex, label):
        raise NotImplementedError("Please implement this method")"""
    def getLabel(self, vertex):
        raise NotImplementedError("Please implement this method")
    
    def getVertex(self, label):
        raise NotImplementedError("Please implement this method")
    
    def newGraph(self, num_vertex):
        raise NotImplementedError("Please implement this method")
    
    def paint_search_graph(self,nameComponent= 'mynetworkSearch', file="graphSearch.js"):
        self.paint_graph_labeled(file=file, nameComponent=nameComponent, mostrarCamino=True)

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
                    out += "ady V" + str(adj._destination+1) + " weigth " + str(adj._weigth) + " -> \n"
            
        return out
    
    @property
    def paint_graph(self, file='graph.js'):
        url = self.__URLFILESGRAPH + file
        print(url)
        js = 'var nodes = new vis.DataSet(['
        for i in range(0, self.num_vertex):
            js+= '\n{id:'+str(i+1)+', label: "'+str(i+1)+'"},'
        js = js[:-1]
        js += ']);\n'
    
        js+= '\n var edges = new vis.DataSet(['
        for i in range(0, self.num_vertex):
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    js += '{\nfrom: '+str(i+1)+', to: '+str(adj._destination)+', label: "'+str(adj._weigth)+'"},'
        js += ']);\n'
        js += 'var container = document.getElementById("mynetwork"); \n var data = { nodes: nodes, edges: edges, }; \n var options = {}; \nvar network = new vis.Network(container, data, options);'
        a = open(url , 'w')
        a.write(js)
        a.close()

    
    @property
    def paint_graph_labeled(self, file='graph.js', nameComponent= 'mynetwork', mostrarCamino=False):
        url = self.__URLFILESGRAPH + file
        camino = {}
        weigths = []
        if self.num_vertex == 0:
            js = 'var advertencia = document.getElementById("advertencia");\n'
            js += 'advertencia.innerHTML = "No hay datos para mostrar";'
            js += 'var weigths = document.getElementById("weigths");\n weigths.innerHTML = "";'
            js += 'vas camino = document.getElementById("camino");\n camino.innerHTML = "";'
            a = open(url , 'w')
            a.write(js)
            a.close()
            return
        
        js = 'var nodes = new vis.DataSet(['
        for i in range(0, self.num_vertex):
            js+= '/n{id:'+str(i)+', label: "'+str(self.getLabel(i))+'"},'
        js = js[:-1]
        js += ']);\n'

        js+= '\n var edges = new vis.DataSet(['
        for i in range(0, self.num_vertex):
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    if adj._weigth != None and adj._destination != None:
                        camino[self.getLabel(i)] = str(adj._weigth)
                        weigths.append(adj._weigth) if adj._weigth not in weigths else weigths
                        js += '{\nfrom: '+str(i)+', to: '+str(adj._destination)+', label: "'+str(adj._weigth)+'"},'
        js += ']);\n'
        js += 'var container = document.getElementById("'+nameComponent+'"); \n var data = { nodes: nodes, edges: edges, }; \n var options = {}; \nvar network = new vis.Network(container, data, options);'

        camino =""
        llaves = list(camino.keys())

        for i in range(1, len(llaves)):
            camino += "Desde: "
            camino += f"'{str(llaves[i-1])}'" + ' hacia ' + f"'{str(llaves[i])}'" + ' con una distancia de ' + str(camino[llaves[i]]) + ' km\n'
        camino = camino[:-7]
        if mostrarCamino:
            js += '\nvar advertencia = document.getElementById("advertencia");\nadvertencia.innerHTML = "";'
            js += '\nvar camino = document.getElementById("camino");\n camino.innerHTML = "'+camino+'";'
            js += '\nvar weigths = document.getElementById("weights");\n weigths.innerHTML = "Distancia total recorrida: '+str(sum(weigths))+' km";'

        a = open(url , 'w')
        a.write(js)
        a.close()

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
                    out += "ady V" + str(adj._destination+1) + " weigth " + str(adj._weigth) + " -> \n"
            
        print(out)

    
    def __transform_graphLabeled__(self):
        json = "["
        for i in range(0, self.num_vertex):
            adjs = self.adjacent(i)
            json += '\n\t{\n\t\t"labelId":' +f"{str(self.getVertex(self.getLabel(i))+1)},"
            #json += '\n\t\t"label": "' + str(self.getLabel(i)) + '",'
            if not adjs.isEmpty: 
                json += '\n\t\t"destinations": ['
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    json += '\n\t\t\t{\n\t\t\t\t"from":' + f"{str(self.getVertex(self.getLabel(i))+1)}"+', \n\t\t\t\t"to":' + f"{str(self.getVertex(self.getLabel(adj._destination))+1)}"+', \n\t\t\t\t"weigth":' + str(adj._weigth) + '\n\t\t\t},'
                json = json[:-1]
                json += '\n\t\t]'
                json += '\n\t},'
            else:
                json += '\n\t\t"destinations": []\n'
                json = json[:-1]
                json += '\n\t},'
            adjs = self.adjacent(i)          
        json = json[:-1]
        json += '\n]'

        return json

    def save_graph_labeled(self, file='graph.json'):
        url = self.__URLFILEGRAPHJSON + file
        a = open(url , 'w')
        a.write(self.__transform_graphLabeled__())
        a.close()

    def recontruct_graph_labeled_with_lat_long(self, file='graph.json', atype: object = None , model: object = None):
        url = self.__URLFILEGRAPHJSON + file
        a = open(url , 'r')
        data = json.load(a)
        a.close()
        newGraph = atype
        newModel = model()._lista

        modelos = []
        for item in data:
            model = newModel.get(item['labelId']-1)
            newGraph.labelVertex(item['labelId']-1, model)
            modelos.append(model)
        for item in data:
            destination = item['destinations']
            if destination != []:
                for dest in item['destinations']:
                    distancia = calculate_weigth_geographic(modelos[dest['from']-1], modelos[dest['to']-1])
                    newGraph.insert_edges_weigth(dest['from']-1, dest['to']-1, distancia)
        return newGraph
    
    #otener los pesos para generar un json 
    def obtain_weigths(self, graph:object=None, file='graph.json'):
        print(graph)
        out = []
        for i in range(0, graph.num_vertex):
            info = {}
            adjs = graph.adjacent(i)
            if not adjs.isEmpty:
                info['labelId'] =  graph.getVertex(graph.getLabel(i))+1
                info['destinations'] = []
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    info['destinations'].append({
                        'from': graph.getVertex(graph.getLabel(i))+1,
                          'to': adj._destination+1, 
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
       dlon = lon2 - lon1
       dlat = lat2 - lat1
       
       distancia = geopy.distance.distance((lat1, lon1), (lat2, lon2)).km
       return round(distancia, 2)







    # @property
    # def paint_graph_labeled(self, file='d3/grafo.js'):
    #     url = self.__URL + file
    #     js = 'var nodes = new vis.DataSet(['
    #     for i in range(0, self.num_vertex):
    #         js+= '\n{id:'+str(i+1)+', label: "'+str(self.getLabel(i))+'"},'
    #     js = js[:-1]
    #     js += ']);\n'
        
    #     js+= '\n var edges = new vis.DataSet(['
    #     for i in range(0, self.num_vertex):
    #         adjs = self.adjacent(i)
    #         if not adjs.isEmpty:
    #             for j in range(0, adjs._length):
    #                 adj = adjs.get(j)
    #                 js += '{\nfrom: '+str(i+1)+', to: '+str(adj._destination)+', label: "'+str(adj._weigth)+'"},'
    #     js += ']);\n'
    #     js += 'var container = document.getElementById("mynetwork"); \n var data = { nodes: nodes, edges: edges, }; \n var options = {}; \nvar network = new vis.Network(container, data, options);'
    #     a = open(url , 'w')
    #     a.write(js)
    #     a.close()
        
def paint_map_labeled(self, file='d3/mapa.js'):
        url = self.__URL + file
        """ var marker = L.marker([45565, -0.09]).addTo(map);
        marker.bindPopup("<b>Hello world!</b><br>I am a popup.").openPopup(); """
        js = ''
        for i in range(0, self.num_vertex):
            obj = self.getLabel(i)
            print(obj)
            if obj is nan:
                js+= f'var {obj} = L.marker([0,0]).addTo(map);\n'
            else:
                js+= f'var {(obj._nombre).replace(" ","")} = L.marker(['+str(obj._latitud)+','+str(obj._longitud )+']).addTo(map);\n'
                js+= f'{(obj._nombre).replace(" ","")}.bindPopup("<b>{obj._nombre}</b><br>{obj._direccion}").openPopup();\n'
            
        a = open(url , 'w')
        a.write(js)
        a.close()
        
