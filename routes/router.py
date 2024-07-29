# Importar los módulos necesarios de Flask y otros controles
from flask import Blueprint, jsonify, make_response, request, render_template, redirect, abort
from controls.universidad.UniversidadDaoControl import UniversidadDaoControl
from controls.tda.graph.graphLabeledNoManaged import GraphLabeledNoManaged
from controls.universidad.universidadgrafo import UniversidadGrafo
from controls.tda.graph.algoritmos.dijkstra import Dijkstra
from controls.tda.graph.algoritmos.floyd import Floyd
from flask_cors import CORS

# Crear un Blueprint para el enrutador
router = Blueprint('router', __name__)

# Ruta para la página principal
@router.route('/')
def home():
    return render_template('template.html')

# Ruta para la página del mapa
@router.route('/mapa')
def mapa():
    return render_template('mapa/grafo.html')

# Ruta para ver el grafo de la universidad
@router.route('/universidad/grafo_universidad')
def grafo_universidad():
    # Crear una instancia de UniversidadDaoControl para manejar las universidades
    universidad = UniversidadDaoControl()
    list = universidad._lista
    
    # Ordenar la lista de universidades si no está vacía
    if not list.isEmpty:
        list.sort_models('_nombre')
    
    # Crear una instancia de UniversidadGrafo y obtener el grafo
    un = UniversidadGrafo()
    un.get_graph
    
    # Renderizar la plantilla correspondiente con las universidades y el grafo
    if list.isEmpty:
        return render_template('universidad/grafo.html', universidades=[], grafouniversidad=[])                                             
    return render_template('universidad/grafo.html', universidades=universidad.to_dict_lista())

# Ruta para ver el grafo de la universidad como administrador
@router.route('/universidad/grafo_ver_admin')
def grafo_ver_admin():
    universidad = UniversidadDaoControl()
    universidadgraph = UniversidadGrafo()
    universidadgraph.get_graph
    list = universidad._lista
    
    # Ordenar la lista de universidades si no está vacía y renderizar la plantilla con adyacencias
    if not list.isEmpty:
        list.sort_models('_nombre')
        return render_template('universidad/adyacencias.html', lista=universidad.to_dict_lista(), grafolista=universidadgraph.obtainWeigths)
    return render_template('universidad/adyacencias.html')

# Ruta para ver la lista de universidades
@router.route('/universidad')
def lista_negocios():
    pd = UniversidadDaoControl()
    list = pd._lista
    
    # Ordenar la lista de universidades si no está vacía y renderizar la plantilla con la lista
    if not list.isEmpty:
        list.sort_models('_nombre')
        return render_template('universidad/lista.html', lista=pd.to_dict_lista())
    return render_template('universidad/lista.html', lista=[])	

# Ruta para editar una universidad específica
@router.route('/universidad/editar/<pos>')
def ver_universidad_editar(pos):
    pd = UniversidadDaoControl()
    nene = pd._list().get(int(pos)-1)
    print(nene)
    return render_template('universidad/editar.html', data=nene)

# Ruta para mostrar el formulario de guardar universidad
@router.route('/universidad/formulario')
def ver_universidad_guardar():
    return render_template('universidad/guardar.html')

# Ruta para agregar una adyacencia al grafo de la universidad
@router.route('/universidad/grafo_universidad/agregar_adyacencia', methods=['POST'])
def agregar_adyacencia():
    data = request.form
    print(data)
    un = UniversidadGrafo()
    
    # Redirigir si no hay datos o si el grafo está vacío
    if not data or un.get_graph == []:
        return redirect('/universidad/grafo_ver_admin', code=404)
    
    # Insertar la adyacencia y guardar el grafo
    un.get_graph.insert_edges(int(data['origen']-1), int(data['destino'])-1)
    un.save_graph
    return redirect('/universidad/grafo_ver_admin', code=302)

# Ruta para guardar una universidad
@router.route('/universidad/guardar', methods=['POST'])
def universidad_guardar():
    universidad = UniversidadDaoControl()
    print('----------------------------------')
    data = request.form
    print(data)
    
    # Guardar los datos de la universidad en la base de datos
    universidad._universidad._nombre = data['nombre']
    universidad._universidad._direccion = data['direccion']
    universidad._universidad._horario = data['horario']
    universidad._universidad._longitud = float(data['longitud'])
    universidad._universidad._latitud = float(data['latitud'])
    universidad.save
    
    return redirect('/universidad', code=302)

# Ruta para calcular el camino más corto utilizando Dijkstra o Floyd
@router.route('/universidad/corto_camino', methods=['POST'])
def corto_camino():
    universidadgraph = UniversidadGrafo()
    data = request.form
    
    # Redirigir si no hay datos
    if not data:
        return redirect('/universidad/grafo_universidad', code=404)
    
    # Usar el algoritmo seleccionado para encontrar el camino más corto
    if data['algoritmos'] == '0':
        search = Dijkstra(universidadgraph.get_graph, int(data['origen']), int(data['destino']))
        search.dijsktra
    else:
        search = Floyd(universidadgraph.get_graph, int(data['destino']), int(data['origen']))
        search.floydWarshall
    
    return redirect('/universidad/grafo_universidad', code=302)
