import os.path
import os, json
import geopy.distance

class Graph:
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
    
    def __str__(self) -> str:
        out = ""
        for i in range(0, self.num_vertex):
            out += "V" + str(i) + '\n'
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    out += "ady V" + str(adj._destination+1) + " weigth " + str(adj._weigth) + "\n"
            
        return out
    
    #funcion para obtener el nombre del vertice
    def getVertex(self, label):

        raise NotImplementedError("sin NAME")
    """ def paint_graph(self):
        #url = os.path.abspath('graph.html')
        url = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))+"/static/d3/grafo.js"
        js = 'var nodes = new vis.DataSet(['
        #vertices
        for i in range(0, self.num_vertex):
            js += '{id: '+str(i+1)+', label: "V'+str.get(i+1)+'"},'+'n'
        js += ']);'
        js += 'n'
        
        js += 'var edges = new vis.DataSet([n'
        #edges
        for i in range(0, self.num_vertex):
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    js += '{from: '+str(i+1)+', to: '+str(adj._destination)+', label: "'+str(adj._weigth)+'"},'+'n'
        js += ']);'
        js += 'n'
        js += 'var container = document.getElementById("mynetwork"); var data = {nodes: nodes, edges: edges,};var options = {};var network = new vis.Network(container, data, options);'
        a = open(url, "w")
        a.write(js)
        a.close()
        print(url)
    """
    def paint_graph(self):
        url = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))+"/static/d3/grafo.js"
        print(url)
        js = 'var nodes = new vis.DataSet(['
        for i in range(0, self.num_vertex):
            label = self.getLabel(i)  # Obtener el nombre del vértice
            js += f'\n{{id: {i+1}, label: "{label}"}},'
        js = js[:-1]
        js += ']);\n'
    
        js+= '\n var edges = new vis.DataSet(['
        for i in range(0, self.num_vertex):
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(0, adjs._lenght):
                    adj = adjs.get(j)
                    js += '{\nfrom: '+str(i+1)+', to: '+str(adj._destination+1)+', label: "'+str(adj._weigth)+'"},'
        js += ']);\n'
        js += 'var container = document.getElementById("mynetwork"); \n var data = { nodes: nodes, edges: edges, }; \n var options = {}; \nvar network = new vis.Network(container, data, options);'
        a = open(url , 'w')
        a.write(js)
        a.close()

    
    def save_graph_label(self, filename='grafo.json'):
        url =os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) +'/data/'+filename
        out = []
        for i in range(0, self.num_vertex):
            adjs = self.adjacent(i)
            out.append({"labelId":self.getVertex(self.getLabel(i)), "destinations":[]})
            if not adjs.isEmpty:
                for j in range(0, adjs._lenght):
                    adj = adjs.get(j)
                    out[i]["destinations"].append({"from":self.getVertex(self.getLabel(i)), "to":adj._destination})
        
        out = json.dumps(out)
        a = open(url , 'w')
        a.write(out)
        a.close()





    #funcion para recuperar el grafo
    def load_graph(self, filename='grafo.json', atype: object= None, model: object= None):
        url =os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) +'/data/'+filename
        a = open(url, 'r')
        data = json.load(a)
        a.close()
        grafo = atype
        modelo = model()._lista

        modelos=[]
        for item in data:
            print(item['labelId'])
            modelaux = modelo.get(item['labelId'])
            grafo.label_vertex(item['labelId'], modelaux)
            modelos.append(modelaux)
        
        for item in data:
            for destino in item['destinations']:
                if destino != []:
                    for dest in item['destinations']:
                        distancia = calcular_distancia(modelos[dest['from']], modelos[dest['to']])
                        grafo.insert_edges_weigth(dest['from'], dest['to'], distancia)
        return grafo
        
    #reconstruir el grafo con el mismo formato que el guardado (load_graph_label) pero agregando el peso en label
    def __grafoLabel__(self):
        json = "["
        for i in range(0, self.num_vertex):
            adjs = self.adjacent(i)
            json += '\n\t{\n\t\t"labelId":'+ f"{str(self.getVertex(self.getLabel(i)))},"
            if not adjs.isEmpty:
                json += ',\n\t\t"destinations":['
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    json += '\n\t\t\t{\n\t\t\t\t"from":'+ f"{str(self.getVertex(self.getLabel(i)))}"+', \n\t\t\t\t"to":'+ str(adj._destination)
                json = json[:-1]
                json += '\n\t\t]'
                json += '\n\t},'
            else: 
                json += '\n\t\t"destinations": []\n'
                json += json[:-1]
                json += '\n\t},'
            adjs = self.adjacent(i)
        json = json[:-1]
        json += '\n]'
        return json
            

    def obtain_weigths(self, grafo: object = None, filename='grafo.json'):
        out = []
        for i in range(0, grafo.num_vertex):
            info = {}
            adjs = grafo.adjacent(i)
            if not adjs.isEmpty:
                info['labelId'] = grafo.getVertex(grafo.getLabel(i))+1
                info['destinations'] = []
                for j in range(0, adjs._lenght):
                    adj = adjs.get(j)
                    info['destinations'].append({
                        "from":grafo.getVertex(grafo.getLabel(i))+1, 
                        "to":adj._destination+1, 
                        "weigth":adj._weigth})
                out.append(info)
        return out

    # funcion para verificar si existe el archivo
    def existeArchivo(self, filename):
        url =os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) +'/data/'+filename
        return os.path.exists(url)

    def save_graph_labeled(self, filename='grafo.json'):
        url = self.__URL + '/data/' + filename
        a = open(url, 'w')
        a.write(self.__grafoLabel__())
        a.close()


def calcular_distancia(model1: object = None, model2: object = None):
        R = 6371.01
        lat1 = model1._latitud
        lon1 = model1._longitud
        lat2 = model2._latitud
        lon2 = model2._longitud
        
        distancia = geopy.distance.distance((lat1, lon1), (lat2, lon2)).km
        return round(distancia,2)