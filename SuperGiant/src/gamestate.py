from unittest.mock import NonCallableMagicMock
from src.planet import *
from src.globals import *
from src.inventory import *
from src.radar import *
from src.orbit import *


class GameState:
    def __init__(self):
        self.game_log = "Welcome!"
        self.radar = Radar()
        self.inventory = Inventory()
        self.orbit = Orbit()
        self.extractors = 0
        

    def update(self):
        self.orbit.refresh_text()
        self.inventory.refresh_text()
        TEXT_GUI.set_game_log_text(self.game_log)
    

    def search_planet(self, search_mode):
        if search_mode == None:
            search_mode = 's'

        if search_mode not in PLANET_SEARCH_MODES:
            self.game_log = INVALID_COMMAND
            return

        if not self.inventory.can_find_planet(search_mode):
            self.game_log = NOT_ENOUGH_FUEL
            return

        self.radar.find_new_planet(search_mode)
        self.inventory.deduct_find_planet_cost(search_mode)
        planet_info = self.radar.found_planet.get_description()        
        self.game_log = FOUND_PLANET + ' ' + planet_info


    def buy_found_planet(self, name):
        if name == None:
            self.game_log = INVALID_COMMAND
            return
        
        if len(name) > 10:
            self.game_log = NAME_TOO_LONG
            return

        if self.radar.found_planet == None:
            self.game_log = NO_PLANET_TO_BUY
            return

        if not self.orbit.can_add_planet():
            self.game_log = ORBIT_CAPACITY_REACHED
            return

        cost = self.radar.found_planet.get_planet_cost()
        if not self.inventory.can_afford_planet(cost):
            self.game_log = CANT_AFFORD
            return
        
        self.inventory.deduct_credits(cost)
        self.radar.found_planet.name = name
        self.orbit.add_planet(self.radar.found_planet)
        self.radar.pop()
        self.game_log = BOUGHT_PLANET + ' ' + name


    def buy_fuel(self, amt):
        if not amt.isnumeric():
            self.game_log = INVALID_COMMAND
            return
        
        amt = int(amt)

        if not self.inventory.can_buy_fuel(amt):
            self.game_log = CANT_AFFORD
            return
        
        self.inventory.buy_fuel(amt)
        self.game_log = BOUGHT_FUEL + ' ' + str(amt)


    def process_planets(self, no_arg):
        profit = self.orbit.process_all()
        self.inventory.add_credits(profit)
        self.game_log = PROCESSED_PLANETS + ' ' + str(profit) + ' credits'
    
    
    def recycle_planet(self, planet_name):
        planet = self.orbit.get_planet(planet_name)

        if planet == None:
            self.game_log = NO_SUCH_PLANET + ' ' + planet_name
            return
        
        value = planet.get_planet_value()
        self.inventory.add_credits(value)
        self.orbit.remove_planet(planet_name)
        self.game_log = RECYCLED_PLANET + ' ' + str(value)


    def increase_orbit_capacity(self, no_arg):
        cost = self.orbit.get_capacity_increase_cost() # (self.capacity) * 50000
        if self.inventory.credits < cost:
            self.game_log = CANT_AFFORD + ' (need {}).'.format(cost)
            return

        if self.orbit.max_capacity_reached():
            self.game_log = MAX_CAPACITY_REACHED
            return

        self.orbit.increase_capacity()
        self.inventory.deduct_credits(cost)
        self.game_log = INCREASED_CAPACITY


    def purchase_auto_extractor(self, no_arg):
        cost = self.orbit.get_auto_extractor_cost()
        if cost > self.inventory.credits:
            self.game_log = CANT_AFFORD + ' (need {}).'.format(cost)
            return
        
        self.inventory.deduct_credits(cost)
        self.orbit.add_extractor()
        self.game_log = BOUGHT_AUTO_EXTRACTOR

    def increase_tech_level(self, name):
        if name == None:
            self.game_log = INVALID_COMMAND
            return
        
        planet = self.orbit.get_planet(name)
        if planet == None:
            self.game_log = NO_SUCH_PLANET
            return

        if not planet.can_increase_tech_level():
            self.game_log = MAX_TECH_LEVEL_REACHED
            return

        cost = planet.get_cost_to_increase_tech_level()
        if cost > self.inventory.credits:
            self.game_log = CANT_AFFORD + ' (need {}).'.format(cost)
            return
        
        self.inventory.deduct_credits(cost)
        planet.increase_tech_level()