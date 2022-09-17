import glob, pickle
from src.globals import *
from src.gamestate import *

SAVE_FOLDER = 'save_files/'
SAVE_FILE_EXTENSION = '.sav'


class SaveManager:
    def __init__(self):
        self.selected_save = None

    def save_select(self, kb_handler, action_handler):
        # new game
        if not self.show_save_selection():
            return GameState()

        # save selection
        while self.selected_save == None:
            kb_handler.read_key()
            action_handler.execute_action(kb_handler.pop_phrase())
            TEXT_GUI.set_input_text(': ' + kb_handler.get_buffer_string())
            
        return self.selected_save


    def show_save_selection(self):
        saves = self.check_for_saves()

        if len(saves) == 0:
            return False
        
        else:
            saves_list = [
                'Save Files',
                '=================='
            ]
            saves_list.extend(saves)
            TEXT_GUI.set_orbit_text('\n'.join(saves_list))
            TEXT_GUI.set_game_log_text('Enter a save file (NEW for new game)')
            return True

    def check_for_saves(self):
        save_files = glob.glob(SAVE_FOLDER + '*' + SAVE_FILE_EXTENSION)
        save_files = [s[len(SAVE_FOLDER) : -len(SAVE_FILE_EXTENSION)] for s in save_files]
        for file in save_files:
            print(file)

        return save_files

    def new_save(self, no_arg):
        self.selected_save = GameState()


    def load_save(self, save_name):
        try:
            with open(SAVE_FOLDER + save_name + SAVE_FILE_EXTENSION, 'rb') as save_file:
                self.selected_save = pickle.load(save_file)
        except:
            print('ERROR: Could not load save')
    

    def save_game(self, game_state, save_name):
        try:
            with open(SAVE_FOLDER + save_name + SAVE_FILE_EXTENSION, 'wb') as save_file:
                pickle.dump(game_state, save_file)
        except:
            print('ERROR: Could not save game')



