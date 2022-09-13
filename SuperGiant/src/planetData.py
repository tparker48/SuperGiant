from lib.graphics import *

masses = ['Molecular', 'Miniscule', 'Tiny', 'Small', 'Medium', 'Large', 'Massive', 'Supermassive', 'Giant', 'Supergiant', 'Goliath']

materials = {
    0: ['Rock', 'Dirt', 'Grass', 'Sand', 'Water'],
    1: ['Iron', 'Asphault', 'Organic', 'Molten'],
    2: ['Glass', 'Fiber', 'Plastic'],
    3: ['Gold', 'Art'],
    4: ['Diamond', 'Science'],
    5: ['Plasma'],
    6: ['???']
}

material_colors = {
    'Rock': color_rgb(69, 69, 69) ,
    'Dirt': color_rgb(97, 69, 45) ,
    'Grass': color_rgb(88, 153, 70) ,
    'Sand': color_rgb(210, 212, 140) , 
    'Water': color_rgb(55, 126, 196) ,
    'Iron': color_rgb(64, 56, 50) ,
    'Asphault': color_rgb(125, 125, 125) ,
    'Organic': color_rgb(50, 71, 33) ,
    'Molten': color_rgb(87, 23, 5) ,
    'Glass': color_rgb(149, 168, 186) ,
    'Fiber': color_rgb(196, 94, 176) ,
    'Plastic': color_rgb(136, 156, 128) ,
    'Gold': color_rgb(209, 134, 21) ,
    'Art': color_rgb(170, 115, 209) ,
    'Diamond': color_rgb(155, 210, 232) ,
    'Science': color_rgb(207, 111, 14) ,
    'Plasma': color_rgb(218, 43, 227) ,
    '???': color_rgb(247, 252, 255) 
}

material_values = {
    0: 10.0,
    1: 15.0,
    2: 30.0,
    3: 100.0,
    4: 500.0,
    5: 1500.0,
    6: 5000.0
}

civilizations = ['Utilitarian', 'Utopian', 'Anarchist', 'Communal', 'Fascist']

civilization_production_rates = {
    'Utilitarian': 5.0,
    'Utopian': 5.0,
    'Anarchist': 1.0,
    'Communal': 2.0,
    'Fascist': 8.0
}

civilization_production_efficiencies = {
    'Utilitarian': 0.7,
    'Utopian': 0.5,
    'Anarchist': 0.2,
    'Communal': 0.4,
    'Fascist': 0.0
}

civilization_operational_costs = {
    'Utilitarian': 0.15,
    'Utopian': 0.10,
    'Anarchist': 0.0,
    'Communal': 0.2,
    'Fascist': 0.5
}

civilization_colors = {
    'Utilitarian': color_rgb(219, 186, 18),
    'Utopian': color_rgb(191, 162, 219),
    'Anarchist': color_rgb(15, 15, 15),
    'Communal': color_rgb(50, 199, 122),
    'Fascist': color_rgb(125, 41, 35)
}