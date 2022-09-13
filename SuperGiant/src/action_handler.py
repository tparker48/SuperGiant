from src.gamestate import *

class ActionHandler:
    game_state = None
    actions = {}

    def __init__(self, game_state):
        self.game_state = game_state
        self.connect_actions_to_game_state()
    
    def connect_actions_to_game_state(self):
        self.actions = {
            'search': self.game_state.search_planet,
            'fuel': self.game_state.buy_fuel,
            'buy': self.game_state.buy_found_planet,
            'process': self.game_state.process_planets,
            'auto': self.game_state.purchase_auto_extractor,
            'recycle': self.game_state.recycle_planet,
            'expand': self.game_state.increase_orbit_capacity
        }

    def execute_action(self, action):
        if action == None:
            return
        
        words = action.split()

        if len(words) == 1:
            action = words[0]
            args = None
        elif len(words) == 2:
            action = words[0]
            args = words[1]
        
        if action in self.actions and len(words) < 3:
            self.actions[action](args)
            return
        
        self.game_state.game_log = INVALID_COMMAND