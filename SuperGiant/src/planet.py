import random
import time
from src.globals import *
from lib.graphics import *
from src.planetData import *


class PlanetGraphic:
    def __init__(self, material, planet_mass, civilization_type):
        self.color = material_colors[material]
        self.size = 15 + (masses.index(planet_mass)+1)*5
        self.civ_type = civilization_type


    def draw(self, x, y, graphics_window):
        self.planet_circle = Circle(Point(x,y), self.size)
        self.planet_circle.setFill(self.color)
        self.planet_circle.setOutline(self.color)
        self.planet_circle.draw(graphics_window)

        flag_w = 40
        flag_h = 20
        flag_x = x - flag_w//2
        flag_y = y - flag_h//2
        self.flag = Rectangle(Point(flag_x, flag_y), Point(flag_x + flag_w, flag_y + flag_h))
        self.flag.setFill(civilization_colors[self.civ_type])
        self.flag.setOutline(civilization_colors[self.civ_type])
        self.flag.draw(graphics_window)


    def undraw(self):
        self.planet_circle.undraw()
        self.flag.undraw()


class Planet:
    def __init__(self, material_lvl, planet_mass, civilization_type):
        self.material = random.sample(materials[material_lvl], 1)[0]
        self.planet_mass = planet_mass
        self.civilization_type = civilization_type

        self.graphic = PlanetGraphic(self.material, planet_mass, civilization_type)

        self.resource_amount = 25.0 * + (2.0 * (masses.index(planet_mass)+1.0))**3
        self.resource_drained = 0.0
        self.resource_value = material_values[material_lvl]
        self.resource_is_sustainable = self.material in ['Organic', 'Fiber', 'Art', 'Engineering', 'Plasma', '???']

        self.civ_tech_level = 1
        self.civ_production_rate = civilization_production_rates[civilization_type]
        self.civ_production_efficiency = civilization_production_efficiencies[civilization_type]
        self.civ_operational_cost = civilization_operational_costs[civilization_type]

        self.last_process_time = time.time() - self.get_cooldown_time()
    

    def get_output(self):
        return 5.0 * (self.civ_production_rate + self.civ_tech_level)
    

    def get_resource_drain(self):
        if self.resource_is_sustainable:
            return 0.0
        return self.get_output()*(1.0 - self.civ_production_efficiency)


    def get_cost(self):
        return self.resource_value * self.get_output() * self.civ_operational_cost / 2


    def get_profit(self):
        monthly_income = (self.resource_value * self.get_output())
        monthly_cost = self.get_cost()
        return monthly_income - monthly_cost


    def get_processesses_until_empty(self):
        if self.resource_is_sustainable:
            return 'inf'
        return (self.resource_amount - self.resource_drained) / self.get_resource_drain()


    def get_material_value(self):
        return self.resource_value
        

    def get_cooldown_time(self):
        return (MAX_COOLDOWN + 1.0/MAX_TECH_LEVEL) - MAX_COOLDOWN*(self.civ_tech_level/MAX_TECH_LEVEL)


    def get_cooldown_remaining(self):
        return max(0, self.get_cooldown_time() - (time.time() - self.last_process_time))


    def enough_resources_to_process(self):
        resources_remaining = self.resource_amount - self.resource_drained
        if (not self.resource_is_sustainable) and (resources_remaining - self.get_resource_drain() < 0):
            return False

        return True


    def can_process(self):
        return self.enough_resources_to_process() and (self.get_cooldown_remaining() == 0)


    def process_materials(self):
        self.resource_drained += self.get_resource_drain()
        self.last_process_time = time.time()
        return self.get_profit()


    def can_increase_tech_level(self):
        return self.civ_tech_level < MAX_TECH_LEVEL


    def get_cost_to_increase_tech_level(self):
        return 7500.0 * (self.civ_tech_level)


    def increase_tech_level(self):
        self.civ_tech_level+=1


    def get_tech_level(self):
        return self.civ_tech_level


    def get_planet_cost(self):
        return self.resource_value * self.get_output() * (2.0 * (masses.index(self.planet_mass)+1.0))


    def get_planet_value(self):
        drain_percentage = float(self.resource_amount-self.resource_drained)/self.resource_amount
        initial_value = self.get_planet_cost()
        return (initial_value*drain_percentage) + (((self.civ_tech_level-1)**2) * 10000.0)


    def get_description(self):
        return self.planet_mass + ', ' + self.civilization_type + ', ' + self.material


    def draw(self, x, y):
        self.graphic.draw(x, y, WINDOW)


    def undraw(self):
        self.graphic.undraw()


class PlanetFactory:
    def get_random_material_lvl():
        roll = 100.0 * random.random()
        if roll <= 40:
            return 0
        elif roll <= 65:
            return 1
        elif roll <= 80:
            return 2
        elif roll <= 90:
            return 3
        elif roll <= 96:
            return 4
        elif roll <= 99:
            return 5
        else:
            return 6


    def get_random_planet_mass():
        roll = roll = 100.0 * random.random()

        if roll <= 5:
            return 'Molecular'
        elif roll <= 25:
            return random.sample(['Miniscule', 'Tiny'], 1)[0]
        elif roll <= 65:
            return random.sample(['Small', 'Medium', 'Large'], 1)[0]
        elif roll <= 85:
            return random.sample(['Massive', 'Supermassive'], 1)[0]
        elif roll <= 95:
            return random.sample(['Giant', 'Supergiant'], 1)[0]
        else:
            return 'Goliath'


    def generate_random_planet(search_type):
        material_lvl = min(PlanetFactory.get_random_material_lvl() + search_type, 6)
        mass = PlanetFactory.get_random_planet_mass()
        civ_type = random.sample(civilizations, 1)[0]
        return Planet(material_lvl, mass, civ_type)