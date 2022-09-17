from lib.graphics import color_rgb, GraphWin
from src.textGui import TextGUI

W = 1300
H = 600

BG_FILL = color_rgb(20,20,20)
ACTIVE_SELECTION_FILL = color_rgb(100,100,100)
INACTIVE_SELECTION_FILL = color_rgb(60,60,60)
TEXT_PRIMARY = color_rgb(255,255,255)
TEXT_SECONDARY = color_rgb(190,190,190)
TEXT_SPECIAL = color_rgb(242, 169, 10)

WINDOW = GraphWin(width = W, height = H)
WINDOW.setCoords(0, 0, W, H)
WINDOW.setBackground(BG_FILL)

TEXT_GUI = TextGUI(W, H, TEXT_PRIMARY, TEXT_SECONDARY, TEXT_SPECIAL)

INITIAL_CREDITS = 5000
INITIAL_FUEL = 100
FUEL_PRICE = 50
MAX_TECH_LEVEL = 10
MAX_COOLDOWN = 7.0

PLANET_SEARCH_MODES = ['s', 'm', 'l']

PLANET_SEARCH_FUEL_COSTS = {
    's' : 10,
    'm': 50,
    'l': 250
}

CANT_AFFORD = "Insufficient Credits!"
NOT_ENOUGH_FUEL = "Not Enough Fuel!"
INVALID_COMMAND = "Invalid Command!"
FOUND_PLANET = 'Found Planet: '
BOUGHT_PLANET = 'Bought Planet: '
NO_SUCH_PLANET = 'No Such Planet: '
NO_PLANET_TO_BUY = 'No Planets Have Been Found!'
ORBIT_CAPACITY_REACHED = 'Orbit Capacity Reached!'
PROCESSED_PLANETS = 'Processed Planets For '
PLANET_COOLING_DOWN = 'Cannot Process: Cooling Down!'
NOT_ENOUGH_RESOURCES = 'Cannot Process: Not Enough Materials Left!'
RECYCLED_PLANET = 'Recycled Planet: '
BOUGHT_AUTO_EXTRACTOR = 'Purchased Auto-Extractor'
INCREASED_CAPACITY = 'Increased Orbit Capacity'
BOUGHT_FUEL = 'Purchased Fuel: '
NAME_TOO_LONG = 'Name Too Long! (10 Characters Max)'
MAX_CAPACITY_REACHED = 'Max Orbit Capacity Reached!'
MAX_TECH_LEVEL_REACHED = 'Max Tech Level Reached!'

ACTIONS_INFO = [
    'search [s, m, l]  - search for planets',
    'buy [name]        - buy discovered planet',
    'process           - process owned planets',
    'fuel [amount]     - buy specified amount of fuel',
    'recycle [name]    - recycle a planet for credits',
    'expand            - increase orbit capacity',
    'level [name]      - increase tech level of planet',
    'auto              - buy an auto-extractor',
    'save [name]       - save game',
    'quit              - quit game'
]

LOAD_SAVE_INFO = [
    'load [name]  - load a saved game',
    'new          - new game',
    'quit         - quit game'
]