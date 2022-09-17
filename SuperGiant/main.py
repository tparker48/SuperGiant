import random
from lib.graphics import *
from src.globals import *
from src.keyboard_handler import *
from src.action_handler import *
from src.planet import *
from src.gamestate import *
from src.save_manager import *


# draw stars
for i in range(100):
    x = int(random.random()*W)
    y = int(random.random()*H)
    radius = 1 + int(random.random()*3)
    intensity = 25 + int(random.random()*55)
    star = Circle(Point(x,y), radius)
    star.setFill(color_rgb(intensity,intensity,intensity))
    star.setOutline(color_rgb(intensity,intensity,intensity))
    star.draw(WINDOW)

TEXT_GUI.draw(WINDOW)

save_manager = SaveManager()
kb_handler = KeyboardHandler()
action_handler = ActionHandler(save_manager)

action_handler.show_loadsave_help()
game_state = save_manager.save_select(kb_handler, action_handler)

action_handler.connect_actions_to_game_state(game_state)
game_state.update()
action_handler.show_actions_help()

while True:
    kb_handler.read_key()
    action_handler.execute_action(kb_handler.pop_phrase())
    TEXT_GUI.set_input_text(': ' + kb_handler.get_buffer_string())
    game_state.update()