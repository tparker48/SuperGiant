import random
from lib.graphics import *
from src.constants import *
from src.keyboard_handler import *
from src.action_handler import *
from src.planet import *
from src.gamestate import *

win = GraphWin(width = W, height = H)
win.setCoords(0, 0, W, H)
win.setBackground(BG_FILL)

for i in range(100):
    x = int(random.random()*W)
    y = int(random.random()*H)
    radius = 1 + int(random.random()*3)
    tempC = Circle(Point(x,y), radius)
    intensity = 25 + int(random.random()*55)
    tempC.setFill(color_rgb(intensity,intensity,intensity))
    tempC.setOutline(color_rgb(intensity,intensity,intensity))
    tempC.draw(win)

game_state = GameState(win)
kb_handler = KeyboardHandler(win)
action_handler = ActionHandler(game_state)

game_log = Text(Point(W//2, H//8), '')
game_log.setStyle('italic')
game_log.setTextColor(color_rgb(190,190,190))
game_log.setSize(12)
game_log.draw(win)

input_text = Text(Point(W//2, H//14), '')
input_text.setTextColor('white')
input_text.setSize(13)
input_text.draw(win)

game_state.inventory.credits = 999999999
game_state.inventory.fuel = 999999999

while True:
    kb_handler.read_key()
    phrase = kb_handler.pop_phrase()
    action_handler.execute_action(phrase)

    input_text.setText(': ' + kb_handler.get_buffer_string())
    game_log.setText(game_state.game_log)
    game_state.update()