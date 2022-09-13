from lib.graphics import *
from src.constants import *
from src.planet import *

class Radar:
    found_planet = None
    window = None
    info_txt = None

    def __init__(self, graphics_window):
        self.window = graphics_window
        self.info_txt = Text(Point(W - W//8, H//2 - H//8), '')
        self.info_txt.setTextColor('white')
        self.info_txt.setSize(10)
        self.info_txt.draw(graphics_window)
        
    def find_new_planet(self, search_mode):
        self.pop()
        self.found_planet = PlanetFactory.generate_random_planet(PLANET_SEARCH_MODES.index(search_mode))

        self.found_planet.draw(W - W//8, H - H//10 - H//8, self.window)
        self.update_planet_info()

    def pop(self):
        if self.found_planet != None:
            self.found_planet.undraw()
            self.clear_planet_info()

        self.found_planet = None
    
    def update_planet_info(self):
        self.info_txt.setText('\n'.join([
            '-------------------------------',
            'Size: ' + self.found_planet.planet_mass,
            '-------------------------------',
            'Total Resources: ' + str(self.found_planet.resource_amount),
            '',
            '-------------------------------',
            'Export: ' + self.found_planet.material,
            '-------------------------------',
            'Value: ' + str(self.found_planet.get_material_value()),
            'Sustainable: ' + ('Yes' if self.found_planet.resource_is_sustainable else 'No'),
            '',
            '-------------------------------',
            'Civ. Type: ' + self.found_planet.civilization_type,
            '-------------------------------',
            'Production Rate: ' + str(self.found_planet.get_output()),
            'Efficiency: ' + str(self.found_planet.civ_production_efficiency),
            'Operational Cost: ' + str(self.found_planet.civ_operational_cost),
            '',

            'Cost: ' + str(self.found_planet.get_planet_cost()),


        ]))

    def clear_planet_info(self):
        self.info_txt.setText('')