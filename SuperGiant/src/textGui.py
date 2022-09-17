from lib.graphics import *


class TextGUI:
    def __init__(self, width, height, text_primary, text_secondary, text_special):
        self.input = Text(Point(width//2, height//14), '')
        self.input.setSize(13)
        self.input.setTextColor(text_primary)

        self.game_log = Text(Point(width//2, height//8), '')
        self.game_log.setSize(12)
        self.game_log.setStyle('italic')
        self.game_log.setTextColor(text_secondary)

        self.inventory = Text(Point(width//10, height - height//10), '')
        self.inventory.setSize(14)
        self.inventory.setStyle('bold')
        self.inventory.setTextColor(text_special)

        self.radar = Text(Point(width - width//8, height//2 - height//8), '')
        self.radar.setSize(10)
        self.radar.setTextColor(text_primary)

        self.orbit = Text(Point(width//2, height//2 + height//20) ,'')
        self.orbit.setSize(11)
        self.orbit.setTextColor(text_primary)

        self.actions = Text(Point(width//6, height//6), '')
        self.actions.setSize(10)
        self.actions.setFill(text_secondary)


    def draw(self, graphics_window):
        self.input.draw(graphics_window)
        self.game_log.draw(graphics_window)
        self.inventory.draw(graphics_window)
        self.radar.draw(graphics_window)
        self.orbit.draw(graphics_window)
        self.actions.draw(graphics_window)


    def set_inventory_text(self, text):
        self.inventory.setText(text)


    def set_game_log_text(self, text):
        self.game_log.setText(text)


    def set_input_text(self, text):
        self.input.setText(text)


    def set_radar_text(self, text):
        self.radar.setText(text)


    def set_orbit_text(self, text):
        self.orbit.setText(text)


    def set_actions_text(self, text):
        self.actions.setText(text)
