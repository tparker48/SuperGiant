from planet import *
from constants import *
from math import ceil

class Orbit:
    planets = []
    capacity = 1
    extractors = 0

    def __init__(self, graphics_window):
        self.text_obj = Text(Point(W//2, H//2 + H//20) ,'')
        self.text_obj.setTextColor('white')
        self.text_obj.setSize(11)
        self.text_obj.draw(graphics_window)

    def add_planet(self, planet):
        self.planets.append(planet)
    
    def remove_planet(self, planet_name):
        idx = self.get_planet_idx(planet_name)
        self.planets = self.planets[:idx] + self.planets[idx+1:]

    def get_planet(self, planet_name):
        idx = self.get_planet_idx(planet_name)
        return None if idx == None else self.planets[idx]

    def can_add_planet(self):
        return len(self.planets) < self.capacity
    
    def max_capacity_reached(self):
        return self.capacity == 20

    def get_capacity_increase_cost(self):
        return (self.capacity) * 50000

    def increase_capacity(self):
        self.capacity += 1

    def get_auto_extractor_cost(self):
        return (self.extractors+1) * 1000000
    
    def add_extractor(self):
        self.extractors += 1

    def refresh_text(self):
        planet_text = []
        planet_text.append('Orbit ({}/{})'.format(len(self.planets), self.capacity))
        planet_text.append('===============================================')
        planet_text.append('  Name        Material   Remaining   Cooldown')
        planet_text.append('===============================================')

        for planet in self.planets:
            name_extra_space = ' '*(10 - len(planet.name))
            name = planet.name + name_extra_space
            
            material_extra_space = ' '*(8 - len(planet.material))
            material_info = planet.material + material_extra_space
            
            material_percentage = str(int(100*(planet.resource_amount - planet.resource_drained) / planet.resource_amount)) + '%'
            material_remaining = (material_percentage if not planet.resource_is_sustainable else 'INF%')
            material_remaining_extra_space = ' '*(4 - len(material_remaining))
            material_remaining = material_remaining + material_remaining_extra_space

            cooldown = str(int(ceil(planet.get_cooldown_remaining()))) + 's'

            planet_text.append('> {}  {}   {}        {}'.format(name, material_info, material_remaining, cooldown))

            

        planet_text = '\n'.join(planet_text)
        self.text_obj.setText(planet_text)
    
    def process_all(self):
        profit = 0
        for planet in self.planets:
            print('planet name')
            if planet.can_process():
                print('processing')
                profit += planet.process_materials()
        return profit

    
    def get_planet_idx(self, planet_name):
        for i in range(len(self.planets)):
            if self.planets[i].name == planet_name:
                return i
        return None
