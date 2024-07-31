# Importar los módulos necesarios de Flask y otros controles
from flask import Blueprint, jsonify, make_response, request, render_template, redirect, abort
from controls.universidad.UniversidadDaoControl import UniversidadDaoControl
from controls.universidad.universidadgrafo import UniversidadGrafo

from flask_cors import CORS

# Crear un Blueprint para definir rutas específicas
router = Blueprint('router', __name__)

# Ruta para el inicio que renderiza una plantilla HTML
@router.route('/')
def home():
    return render_template('template.html')

# Ruta para el mapa que renderiza una plantilla HTML específica
@router.route('/mapa')
def mapa():
    return render_template('mapa/grafo.html')

# Ruta para ver el grafo de la universidad

@router.route('/universidad/grafo_ver_admin')
def grafo_ver_admin():
    ud = UniversidadDaoControl()
    universidadGrafo = UniversidadGrafo()
    universidadGrafo.DarGrafo
    list = ud._list()
    if not list.isEmpty:
       list.sort_models('_nombre', 2)
    json = universidadGrafo.obtainWeigth
    universidadGrafo.__str__()
    print(json)
    return render_template('universidad/adyacencias.html', lista=ud.to_dic_lista(list), universidadGrafoaux=json)

@router.route('/universidad')
def lista_negocios():
    ud = UniversidadDaoControl()
    list = ud._list()
    if  list.isEmpty:
        return render_template('universidad/lista.html')
    list.sort_models('_id', 1)
    return render_template('universidad/lista.html', lista=ud.to_dic_lista(list))

# Ruta para editar una universidad específica
@router.route('/universidad/editar/<pos>')
def ver_universidad_editar(pos):
    pd = UniversidadDaoControl()
    nene = pd._list().get(int(pos)-1)
    print(nene)
    return render_template('universidad/editar.html', data=nene)

# Ruta para ver el formulario de guardar una nueva universidad
@router.route('/universidad/formulario')
def ver_universidad_guardar():
    return render_template('universidad/guardar.html')

# Ruta para agregar una adyacencia en el grafo de la universidad
@router.route('/universidad/grafo_universidad/agregar_adyacencia', methods=['POST'])
def agregar_adyacencia():
    data = request.form
    un = UniversidadGrafo()
    print(data)
    un.DarGrafo.insert_edges(int(data["origen"])-1, int(data["destino"])-1)
    un.save_graph
    return redirect('/universidad/grafo_ver_admin', code=302)

# Ruta para guardar una universidad
@router.route('/universidad/guardar', methods=['POST'])
def universidad_guardar():
    universidad = UniversidadDaoControl()
    data = request.form
    if not 'nombre' in data.keys():
        abort(404)
    #TODO ...Validar
    # Asignar datos de la universidad desde el formulario
    universidad._universidad._nombre = data['nombre']
    universidad._universidad._direccion = data['direccion']
    universidad._universidad._horario = data['horario']
    universidad._universidad._longitud = float(data['longitud'])
    universidad._universidad._latitud = float(data['latitud'])
    universidad.save
    
    return redirect('/universidad', code=302)

# Ruta para encontrar el camino más corto en el grafo usando Dijkstra o Floyd
@router.route('/universidad/grafo_universidad/<origen>/<destino>/<algoritmo>')
def corto_camino(origen, destino, algoritmo):
    try:
       origen = int(origen)
       destino = int(destino)
       algoritmo = int(algoritmo)
    except ValueError:
        return make_response(
            jsonify({'error': 'Los valores de origen, destino y algoritmo deben ser enteros'}),
            400
        )
    ud = UniversidadDaoControl()
    un = UniversidadGrafo()
    grafo = un.DarGrafo
    grafo.paint_graph()
    list = ud._list()
    camino, distancia = un.caminoCorto(origen, destino, algoritmo)
    return render_template('universidad/grafo.html', lista=ud.to_dic_lista(list), caminoCorto=camino, Distancia=distancia)

    