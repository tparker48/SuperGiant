from src.gamestate import *


class ActionHandler:
    def __init__(self, save_manager):
        self.save_manager = save_manager
        self.game_state = None

        self.actions = {
            'load': self.save_manager.load_save,
            'new': self.save_manager.new_save
        }

    def connect_actions_to_game_state(self, game_state):
        self.game_state = game_state
        self.actions = {
            'search': game_state.search_planet,
            'fuel': game_state.buy_fuel,
            'buy': game_state.buy_found_planet,
            'process': game_state.process_planets,
            'level' : game_state.increase_tech_level,
            'auto': game_state.purchase_auto_extractor,
            'recycle': game_state.recycle_planet,
            'expand': game_state.increase_orbit_capacity,
            'save': self.save_game
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
        
        if words[0] == 'quit':
            exit(0)

        if action in self.actions and len(words) < 3:
            self.actions[action](args)
            return
        
        TEXT_GUI.set_game_log_text(INVALID_COMMAND)

    
    def save_game(self, save_name):
        if save_name == None:
            TEXT_GUI.set_game_log_text(INVALID_COMMAND)
            return
        
        self.save_manager.save_game(self.game_state ,save_name)


    def show_loadsave_help(self):
        TEXT_GUI.set_actions_text('\n'.join(LOAD_SAVE_INFO))


    def show_actions_help(self):
        TEXT_GUI.set_actions_text('\n'.join(ACTIONS_INFO))


    def hide_help(self):
        TEXT_GUI.set_actions_text('')