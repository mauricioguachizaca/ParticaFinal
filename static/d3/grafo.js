var nodes = new vis.DataSet([
{id: 1, label: "1 Pedro"},
{id: 2, label: "2 Mauricio"},
{id: 3, label: "3 Juan"},
{id: 4, label: "4 Fermin"},
{id: 5, label: "5 Boris"},
{id: 6, label: "6 Ana"}]);

 var edges = new vis.DataSet([{
from: 1, to: 2, label: "5.34"},{
from: 1, to: 3, label: "125.49"},{
from: 1, to: 5, label: "500.1"},{
from: 2, to: 1, label: "5.34"},{
from: 2, to: 4, label: "495.54"},{
from: 2, to: 5, label: "494.84"},{
from: 3, to: 1, label: "125.49"},{
from: 3, to: 6, label: "132.71"},{
from: 4, to: 2, label: "495.54"},{
from: 5, to: 1, label: "500.1"},{
from: 5, to: 2, label: "494.84"},{
from: 6, to: 3, label: "132.71"},]);
var container = document.getElementById("mynetwork"); 
 var data = { nodes: nodes, edges: edges, }; 
 var options = {}; 
var network = new vis.Network(container, data, options);