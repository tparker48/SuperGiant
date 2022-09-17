from lib.graphics import *
from src.globals import *


class Inventory:
    def __init__(self):
        self.credits = INITIAL_CREDITS
        self.fuel = INITIAL_FUEL
    

    def refresh_text(self):
        TEXT_GUI.set_inventory_text('Credits: ' + str(int(self.credits)) + '\n' + 'Fuel:    ' + str(self.fuel))


    def add_credits(self, credits):
        self.credits += credits


    def deduct_credits(self, credits):
        self.credits -= credits


    def add_fuel(self, fuel):
        self.fuel += fuel


    def deduct_fuel(self, fuel):
        self.fuel -= fuel


    def deduct_find_planet_cost(self, search_mode):
        self.deduct_fuel(PLANET_SEARCH_FUEL_COSTS[search_mode])


    def buy_fuel(self, amount):
        self.add_fuel(amount)
        self.deduct_credits(FUEL_PRICE*amount)


    def can_find_planet(self, search_mode):
        return PLANET_SEARCH_FUEL_COSTS[search_mode] <= self.fuel


    def can_afford_planet(self, planet_cost):
        return self.credits >= planet_cost


    def can_buy_fuel(self, amount):
        return FUEL_PRICE*amount < self.credits