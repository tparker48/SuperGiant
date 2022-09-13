from lib.graphics import *
from src.constants import *

class Inventory:
    credits = INITIAL_CREDITS
    fuel = INITIAL_FUEL

    def __init__(self, graphics_window):
        self.balance_txt = Text(Point(W//10, H - H//10), '')
        self.balance_txt.draw(graphics_window)
        self.balance_txt.setSize(14)
        self.balance_txt.setStyle('bold')
        self.balance_txt.setTextColor(color_rgb(242, 169, 10))
        self.update_balance_text()
    
    def update_balance_text(self):

        self.balance_txt.setText('Credits: ' + str(int(self.credits)) + '\n' + 'Fuel:    ' + str(self.fuel))

    def add_credits(self, credits):
        self.credits += credits
        self.update_balance_text()

    def deduct_credits(self, credits):
        self.credits -= credits
        self.update_balance_text()

    def add_fuel(self, fuel):
        self.fuel += fuel
        self.update_balance_text()

    def deduct_fuel(self, fuel):
        self.fuel -= fuel
        self.update_balance_text()

    def deduct_find_planet_cost(self, search_mode):
        self.deduct_fuel(PLANET_SEARCH_FUEL_COSTS[search_mode])
        self.update_balance_text()

    def buy_fuel(self, amount):
        self.add_fuel(amount)
        self.deduct_credits(FUEL_PRICE*amount)

    def can_find_planet(self, search_mode):
        return PLANET_SEARCH_FUEL_COSTS[search_mode] <= self.fuel

    def can_afford_planet(self, planet_cost):
        return self.credits >= planet_cost

    def can_buy_fuel(self, amount):
        return FUEL_PRICE*amount < self.credits