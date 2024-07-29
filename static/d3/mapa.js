// Inicializar el mapa en el elemento con id 'map'
var map = L.map('map').setView([-3.995, -79.204], 13);

// Añadir la capa de OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: 'Map data © <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Añadir marcadores con coordenadas (0,0)
var nan1 = L.marker([0, 0]).addTo(map);
var nan2 = L.marker([0, 0]).addTo(map);
var nan3 = L.marker([0, 0]).addTo(map);
var nan4 = L.marker([0, 0]).addTo(map);

// Añadir un marcador en las coordenadas especificadas y abrir un popup
var hola = L.marker([-3.995, -79.204]).addTo(map);
hola.bindPopup("<b>hola</b><br>Ambato").openPopup();
