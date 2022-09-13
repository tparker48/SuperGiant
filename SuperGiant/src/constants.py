from lib.graphics import color_rgb

# window dimensions
W = 1200
H = 600

# colors
BG_FILL = color_rgb(20,20,20)
ACTIVE_SELECTION_FILL = color_rgb(100,100,100)
INACTIVE_SELECTION_FILL = color_rgb(60,60,60)
ACTIVE_SELECTION_TEXT_COLOR = color_rgb(255,255,255)
INACTIVE_SELECTION_TEXT_COLOR = color_rgb(120,120,120)

INITIAL_CREDITS = 5000
INITIAL_FUEL = 100
FUEL_PRICE = 50

PLANET_SEARCH_MODES = ['small', 'medium', 'large']

PLANET_SEARCH_FUEL_COSTS = {
    'small' : 10,
    'medium': 50,
    'large': 250
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